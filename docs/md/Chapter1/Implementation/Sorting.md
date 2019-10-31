## Pair sorting

The sorting algorithm starts at the end of variable couple evaluation and it re-orders the variable-pairs in ascending order to ease the next steps of signature identification [^1].
This step is performed in the same code (and same parallel section) introduced in the previous section, but it deserves an own topic for a better focus on the parallelization strategy chosen.
There are many common parallel implementation of sorting algorithms and, to reach the best performances, we have to chose the more appropriate one.

Serial version of sorting algorithms can be found in the major part of the languages (`Python` and `C++` included).
Also naive versions of this algorithm are quite optimized and they perform the computation with an algorithmic complexity equal to `(O(N log(N)))`[^2].
In this case we have not to re-invent any sorting technique, but we have to insert as well as possible this algorithm into our parallel section, using the variable format chosen for couple performances storage.
Since we work with SoA objects we need to re-order all the structure arrays in the same way.
We can not use a simple sort function, but we can compute the set of indexes that allows the reordering of the arrays, the so-called `argsort` method.
o rearrange the indexes according to a given array of values, we use `template`s in `C++`.

![Parallel merge-sort algorithm scheme. Starting from the original array, the master thread splits the work (sub-arrays) along two slave threads (`split` step in the graph). The split recursion is applied up to a required size of sub-arrays is reached. Each slave-thread applies a sort function (`sort` step in the graph). Then, the full array is recombined following back the thread recursion and applying an `inplace-merge` function (`merge` step in the graph).](../../../../img/merge_sort.png)

As parallelization strategy we can yet invoke the new \emph{keywords} of OpenMP libraries, applying a *divide-and-conquer* architecture using a tree of independent `tasks`[^3].
Using the maximum power of two of the available threads, we split the computation in equal size sub-arrays and perform independent `argsort`s.
Then, going backward to the subdivisions at each step, we merge the sub-arrays two-by-two up to the master thread (ref Fig.[3](../../../../img/merge_sort.png)).


[^1]: We are talking about couple performances meaning the classification accuracy of the feature pair up to now. In some cases the simple accuracy is useless, especially when we are working with unbalanced population classes. In this case we can use a statistical score which takes in count the balancing between right classifications of our samples and classes (e.g Matthews Correlation coefficient, MCC). The developed code evaluates either the global accuracy of classification either the MCC and, with slight changes, it allows to perform the pair re-ordering according to the desired score. Since in the next section we will discuss about the application of the `DNetPRO` algorithm to real data using only the classification accuracy as score, we will focus only on it in the next sections.

[^2]: We are considering only un-stable sort in which the preserving order of equivalent elements in the array is not guaranteed.

[^3]: Tasks in OpenMP are code blocks that the compiler wraps up and makes available to be executed in parallel.


[**next >>**](./FeatSel.md)
