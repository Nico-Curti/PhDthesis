## Combinatorial algorithm

The most computational time-expensive step of the algorithm is certainly the couples evaluation.
From a computation point-of-view this step requires `(O(N^2))` operations for the full set of combinations.
Since we want to perform also an internal Leave-One-Out cross validation for the couple performances estimation, we have to add a `(O(S-1))` to the algorithmic complexity.
Let's focused on some preliminary considerations before discuss about the proposed implementation:

* **Performance:** we aim to apply our method on large datasets and thus we have to take care about code time-performances of this step (identified as bottleneck).
  To reduce as much as possible the call stack inside our code, we should perform the entire code with the smaller number of functions as possibly.
  Moreover, we have to simplify for loops and take care about the automatic code vectorization performed by the optimizer at compile time (SIMD, *Single Instruction Multiple Data*).
  A further optimization step to take in count is related to the cache accesses: the use of custom objects inside the code should benefit from cache accesses (AoS vs SoA, *Array of Structure* vs *Structure of Arrays*).

* **Interdependence:** the variable couple performances evaluation is a set of completely independent computational processes and it can be faced on as `N^2` separately tasks.
  Thus, it can be easily parallelizable to increase speed performance.

* **Simplify:** the use of a simple classifier for performance evaluation simplifies the computation and the storage of the relevant statistical quantities.
  In the discussed implementation, we focused on a Diag-Quadratic classifier (see [Appendix A](../../Appendix/DiscriminantAnalysis/README.md) for further information) in which only means and variances of data play a role in its computation.

* **Cross Validation:** the use of a Leave-One-Out cross validation allows to perform substantially optimizations in the statistical quantities evaluations across the folds (see discussion in [Appendix A - Numerical Implementation](../../Appendix/DiscriminantAnalysis/README.md)).

* **Numerical stability:** we have also to take in care about the numerical stability of the statistic quantities, since we are working under the assumption of a reasonable small number of samples compared to the amount of variables.
  This hypothesis affects the variance estimation: the chose of a numerical stable formula for this quantity plays a crucial role for the computation because the classifier score has to be normalized by this.


With these ideas in mind, we have written a `C++` code ables to optimize this step in a multi-threading environment, aiming to test its scalability over multi-core machines.

Starting from the first discussed point, we have chosen to implement the full code inside a unique main function with the help of only a single SoA custom object and one external function (*sorting algorithm* discussed in the next section).
This allows us to implement the code inside a single parallel section, reducing the time of thread spawning.
We have chosen to import the data from file in sequential mode, since the I/O is not (particularly) affected by parallel optimizations (in our simulations).

Following the instructions suggested in [Appendix A - Numerical Implementation](../Appendix/DiscriminantAnalysis/README.md), we compute the statistical quantities on the full set of data before starting the couples evaluation.
Taking a look to the variance equation

$$
\sigma^2 = \frac{\sum_{i=1}^{S}(x_i - \mu)^2} {S - 1} = \frac{\sum_{i=1}^{S}({x_i}^2)} {S - 1} - \mu^2
$$

we can see that the first equation involves the mean computation as a simple sum of elements, using a large number of subtractions that are numerically unstable for data outliers (moreover because they are elevated to square).
The better choice, in this case, is given by the second formula that allows to compute the both quantities in the formula inside a single parallel loop[^1].
At each cross validation, we used the two pre-computed sums of variables, removing the only data points excluded by the Leave-One-Out.
Another precaution to take in care is to add a small epsilon to the variance before its use in the denominator into the classifier function to prevent numerical underflow.

The set of pair variables can be obtained only by two nested for loops in `C++` and a naive optimization can be simply obtained by reducing the number of iterations following the triangular indexes of the full matrix (by definition the score of the couple `(i, j)` is equal to the score of `(j, i)`).
This precaution easily allows the parallelization of the external loop and drastically reduce the number of iterations, but it also creates a link between the two iteration variables.
The new release of OpenMP libraries [[OpenMP](https://www.openmp.org/)]  [^2]  (from OpenMP 4.5) introduces a new *keyword* in the language, that allows the collapsing of nested for loops into a single one (whose number of iterations is given by the product of the single dimensions), in the only exception of a completely independence of iteration variables.
So, the best strategy to use in this case is to perform the full set of `N^2` iterations with a single `collapse` clause in the external loop [^3].


```python
import pandas as pd
import itertools
import multiprocessing
from functools import partial

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import LeaveOneOut, cross_val_score

def couple_evaluation (couple, data, labels):
  f1, f2 = couple

  samples = data.iloc[[f1, f2]]
  score = cross_val_score(GaussianNB(), samples.T, labels,
                          cv=LeaveOneOut(), n_jobs=1).mean() # nested parallel loops are not allowed

  return (f1, f2, score)

def read_data (filename):
  data = pd.read_csv(filename, sep='\t', header=0)
  labels = data.columns.astype('float').astype('int')
  data.columns = labels

  return (data, labels)

if __name__ == '__main__':

  filename = 'data.txt'

  data, labels = read_data(filename)

  Nfeature, Nsample = data.shape

  couples = itertools.combinations(range(0, Nfeature), 2)
  couples_eval = partial(couple_evaluation, data=data, labels=labels)

  nth = multiprocessing.cpu_count()

  with multiprocessing.Pool(nth) as pool:
    score = zip(*pool.map(couple_eval, couples))

```

In this section we provide an "equivalent" `Python` implementation with the use of common machine learning libraries and parallel settings (ref. [code](https://github.com/Nico-Curti/DNetPRO/blob/master/timing/timing.py)).
In the next sections we will discuss the computational performances of this naive implementation with `C++` one discussed above.



[^1]: To facilitate the SIMD optimization the code is written using only float (single precision) and integer variables.
  This precaution takes in care the register alignment inside the loops and facilitate the compile time optimizer.

[^2]: The OpenMP library is the most common non-standard library for `C++` multi-threading applications.

[^3]: Obviously the iteration where the inner loop variable is lower than the outer one will be skipped by an if condition.



[**next >>**](./Sorting.md)