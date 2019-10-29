## Numerical Implementation

From a computational point-of-view we can exploit each mathematical information and assumption to simplify the computation and improve the numerical stability of our computation.
We would remark that these considerations were taken into account in this work only for the `C++` algorithmic implementation, since these methods are already implemented in high-level programming languages as `Python` and `Matlab` [^1].

In the previous section we highlighted the covariance matrix properties, i.e the covariance matrix is a positive semi-definite and symmetric matrix by definition and these properties allow the matrix inversion.
The computation of the inverse-matrix is a well known complex computational step from a numerical point-of-view and in a general case can be classified as an `O(N^3)` algorithm.
Moreover, the usage of a Machine Learning classifier commonly matches the usage of a cross validation method, i.e multiple subdivision of the dataset in training and test sets.
This involves the computation of multiple inverse matrices and it could represents the performance bottleneck in many real applications (the other computations are quite simple and their algorithmic complexity are certainly less than `O(N^3)`).

Using the mathematical information about covariance matrix we can find the best numerical solution for its inverse that in this case is given by the Cholesky decomposition algorithm.
The Cholesky decomposition or Cholesky factorization allows to rewrite a positive-definite matrix into the product of two triangular matrices (the first is the conjugate transposed of the second)

$$
\mathbf{A} = \mathbf{LL^T} = \mathbf{U^TU}
$$

The algorithmic complexity is still the same but the inverse estimation is simpler using a triangular matrix and the entire inversion can be performed in-place.
It can also be proved that general inverse matrix algorithms suffer of numerical instability issues compared to the output of Cholesky decomposition.
In this case the original inverse matrix can be computed by the multiplication of the two inverses as

$$
\mathbf{A^{-1}} = (\mathbf{L^{-1}})^T(\mathbf{L^{-1}}) = (\mathbf{U^{-1}})(\mathbf{U^{-1}})^T
$$

As second bonus, cross validation methods involve the data splitting in multiple non-independent chunks of the original data.
The extreme case of this algorithm is given by the Leave-One-Out cross validation in which the data superposition between folds is `N-1` (where `N` is the size of the data).
The statistical influence of the swapped data is quite low and the covariance matrix would be quite similar across folds (the inverse matrix would be drastically affected from each slight modification of the original matrix instead).
A second step of optimization can be performed computing the original full-covariance matrix of the whole set of data (`O(N^2)`) and modify it into the right $k$ indexes at each cross-validation step (`O(N*k)`) that in the Leave-One-Out become a single editing case.
This second optimization  can also be performed in the Diag-Quadratic case substituting the covariance matrix with the simpler variance vector.

In the following snippet the implementation of Cholesky decomposition used to invert the covariance matrix is shown.

```c++
#include <iostream>
#include <cmath>

void Cholesky (const int & n, float * mat, float * p)
{
  for (int i = 0; i < n; ++i)
    for (int j = i; j < n; ++j)
    {
      const int idx = i * n + j;
      float sum = mat[i * n + j];

      for (int k = i - 1; k >= 0; --k)
        sum -= mat[i * n + k] * mat[j * n + k];

      if (i == j)
      {
        if ( sum <= 0.f )
        {
          std :: cerr << "Matrix is not positive definite" << std :: endl;
          std :: exit(1);
        }

        p[i] = 1.f / std :: sqrt(sum);
      }
      else
        mat[j * n + i] = sum * p[i];
    }
}

void CholeskyInv (const int & n, float * mat, float * mat_inv)
{
  float * p = new float[n];
  std :: copy_n(mat, n*n, mat_inv);

  Cholesky(n, mat_inv, p);
  for (int i = 0; i < n; ++i)
  {
    mat_inv[i * n + i] = p[i];

    for (int j = i + 1; j < n; ++j)
    {
      float sum = 0.f;

      for (int k = i; k < j; ++k)
        sum -= mat_inv[j * n + k] * mat_inv[k * n + i];

      mat_inv[j * n + i] = sum * p[j];
    }
  }
}
```

Both these two techniques have been used in the \textsf{C++} implementation of the Quadratic Discriminant Analysis classifier and in the Diag-Quadratic Discriminant Analysis classifier used in the `DNetPRO` algorithm implementation (see Chapter [1](../../Chapter1/DNetPRO/README.md)).


[^1]: For sake of completeness we have to highlight that the classification functions provided by `Matlab`, i.e `classify`, are already included into the base software packages, i.e no external Toolbox is needed, while for the `Python` case the most common package which implements these techniques is given by the `scikit-learn` library. `Matlab` allows to set the classifier type as input parameter of the function using a simple string which follows the same nomenclature previously proposed. `Python` has a different imports for each classifier type: in this case we found correspondence between our nomenclature and the `Python` one only in *quadratic* and *linear* cases, while the *Mahalanobis* classifier is not considered as putative classifier. The *diagquadratic* classifier is called `GaussianNB` (*Naive Bayes Classifier*) instead. The last important discrepancy between the two language implementations is found in variance evaluation (and corresponding covariance matrix): `Matlab` proposes the variance estimation only in relation to the mean so the normalization coefficient is given by the number of samples except by one (`N-1`), while `Python` computes the variance with a simple normalization by `N`.

[**next >>**](../Venice/README.md)
