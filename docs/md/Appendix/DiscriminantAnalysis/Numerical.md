## Numerical Implementation

From a numeric point of view we can exploit each mathematical information and assumption to simplify the computation and improve the numerical stability of our computation.
I would remark that this consideration were taken into account in this work only for the `C++` algorithmic implementation since these methods are already implemented in the high-level programming languages as `Python` and `Matlab` [^1].

In the previous section we highlight that the covariance matrix is a positive semi-definite and symmetric matrix by definition and this properties allows the matrix inversion.
The computation of the inverse-matrix is a well known complex computation step from a numerical point-of-view and in a general case can be classified as an `O(N^3)` algorithm.
Moreover the use of a Machine Learning classifier commonly match the use of a cross validation method, i.e multiple subdivision of the dataset in a training and test sets.
This involves the computation of multiple inverse matrix and it could represent the performance bottleneck in many cases (the other computations are quite simple and the algorithm complexity is certainly less than `O(N^3)`).

Using the information about the covariance matrix we can find the best mathematical solution for the inverse matrix computation that in this case is given by the Cholesky decomposition algorithm.
The Cholesky decomposition or Cholesky factorization allows to re-write a positive-definite matrix into the product of two triangular matrix (the first is the conjugate transpose of the second)

$$
\mathbf{A} = \mathbf{LL^T} = \mathbf{U^TU}
$$

The complexity of the algorithm is the same but the inverse estimation is simpler using a triangular matrix and the entire inversion can be performed in-place.
It can also be proved that general inverse matrix algorithms have numerical instability problems compared to the Cholesky decomposition.
In this case the original inverse matrix can be computed by the multiplication of the two inverses as

$$
\mathbf{A^{-1}} = (\mathbf{L^{-1}})^T(\mathbf{L^{-1}}) = (\mathbf{U^{-1}})(\mathbf{U^{-1}})^T
$$

As second bonus, the cross validation methods involve the subdivision of the data in multiple non-independent chunks of the original data.
The extreme case of this algorithm is given by the Leave-One-Out cross validation in which the superposition of the data between folds are `N-1` (where `N` is the size of the data).
The statistical influence of the swapped data is quite low and the covariance matrix will be quite similar between one fold to the other (the inverse matrix will be drastically affected from each slight modification of the original matrix instead).
A second step of optimization can be performed computing the original full-covariance matrix of the whole set of data (`O(N^2)`) and at each cross-validation step evaluate the right set of `k` indexes needed to modify the matrix entrances (`O(N*k)`) that in the Leave-One-Out case are just one.
This second optimization consideration can also be performed in the Diag-Quadratic case substituting the covariance matrix with the simpler variance vector.

Both these two techniques were used in the custom `C++` implementation of the Quadratic Discriminant Analysis classifier and in the Diag-Quadratic Discriminant Analysis classifier for the DNetPRO algorithm implementation (see Chapter [1](../../Chapter1/DNetPRO/README.md)).



[^1]: For completeness we have to highlight that for the `Matlab` case classification functions, i.e `classify`, is already included in the base packages of the software, i.e no external Toolbox are needed, while for the `Python` case the most common package which implements these techniques are given by the *scikit-learn* library. `Matlab` allows to set the classifier type as input parameter in the function using a simple string which follows the same nomenclature previously proposed. `Python` has a different import for each classifier type: in this case we find correspondence between our nomenclature and the `Python` one only in *quadratic* and *linear* cases, while the *Mahalanobis* is not considered a putative classifier. The *diagquadratic* classifier is called `GaussianNB` (*Naive Bayes Classifier*) instead. The last important discrepancy between the two language implementation is in the computation of the variance (and the corresponding covariance matrix): `Matlab` proposes the variance estimation only in relation to the mean so the normalization coefficient is given by the number of sample except by one (`N-1`), while `Python` compute the variance with a simple normalization by `N`.

[**next >>**](../Venice/README.md)
