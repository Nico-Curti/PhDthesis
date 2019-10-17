## BatchNorm function

A common practice before the training of a Neural Network model is to apply some preprocessing to the input patterns.
A classical example is the normalization of training set, i.e it resembles a normal distribution with zero mean and unitary variance.
The initial preprocessing is useful to prevent the early saturation of non-linear activation functions (see section [activation](./Activations.md)).
Moreover in this case we can ensure that all inputs are in the same range of values.

In a deep neural network architecture we can find the same problem also into the intermediate layers because the distribution of the activations is constantly changing during training.
This behavior produces a slowdown in the training convergence because each layer have to adapt itself to a new distribution of data in every training step (or *epoch*).
This problem is also called *internal covariate shift*.

A second problem arises from the heterogeneity of available input data.
If we tune the model parameters according to a given set of data, which inevitably will be limited, we can meet problems during the generalization, i.e the validation of our model using new data, to new samples if they belongs to an equivalent but deformed distribution: this kind of problem passes under the name of *over-fitting*.
A classical example is given by the image detection: if we train a Neural Network model using gray-scale images we can find generalization problems using colored images.
This problem can be solve using regularization techniques.

BatchNorm function (Batch Normalization) allows to overcome these problems with a continuous rescaling of the Neural Network intermediate values during the training [^1] [[Sergey2015BatchNorm](https://ui.adsabs.harvard.edu/\#abs/2015arXiv150203167I)].
In this way we can ensure more stability of the extracted features [[Lecun2000EffBackProp](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)] during the training and a faster convergence.

In particular, the method processes the input of a given layer in order to fight the internal covariate shift problem removing the batch mean and normalizing by the batch variance:

$$
\mu_B = \frac{1}{m}\sum_{i=1}^{m}x_i \quad\quad {\sigma_B}^2 = \frac{1}{m-1}\sum_{i=1}^{m}(x_i - \mu_B)^2
$$

where `m` represents the batch-size and $$x_i$$ is the value of the pixel `x` in the `i`-th image of the batch ($$\in[0, m]$$).
Thus the input data becomes:

$$
\hat{x_i} = \frac{x_i - \mu_B}{\sqrt{ {\sigma_B}^2 + \epsilon} }
$$

where we add an extra $$\epsilon$$ in the denominator for numerical stability [^2].
After this common rescaling we also a apply a scaling-shift to previous results:

$$
y_i = \gamma\hat{x_i} + \beta
$$

where the $$\gamma$$ and $$\beta$$ coefficients are left as variables to be tuned during the training (they are learned during training).
The updating rule of the function parameters ($$\gamma$$ and $$\beta$$) is given by the derivative of the previous functions:

$$
\delta\beta = \sum_{i=1}^{m}{\delta_i}^l \quad\quad \delta\gamma = \sum_{i=0}^{m} {\delta_i}^l \cdot \mu_B
$$

where $$\delta^l$$ is the error passed from the next layer of the network structure.
To complete the error propagation we have also compute the derivative of the BatchNorm function output:

$$
{\delta_i}^{l-1} = \frac{{m}\cdot \delta\hat{x_i} - \sum_{j=1}^{m}\delta\hat{x_i} - \hat{x_i} \cdot \sum_{j=1}^{m} \delta\hat{x_i} \cdot \hat{x_i}}{m \cdot \sqrt{{\sigma_B}^2 + \epsilon} }
$$

Since the BatchNorm function is became a sort of standard into a deep learning models, an efficient implementation of this algorithm is essential to achieve the best computational performances.
We have also to take into account that the batch-normalization procedure is commonly performed after a fully-connected layer or a convolutional one.
Thus the best performances could be obtained merging the two functionality as much as possible as suggested in [[AlexeyAB](https://github.com/AlexeyAB/darknet)].

The `Byron` library was inspired by the `darknet` library provided by Redmon J. et al. and by its many branches.
Despite in each implementation we can find the BatchNorm function, aware of the author, in any version we can find a right implementation of this function as standalone method.
We have already highlighted that this normalization function can be efficiently joined to other function to increase the computational performances but in these case we have to different manage the dimensions of the involved arrays.
A standalone implementation of the BatchNorm function required a rearrangement of its functions and it was provided into the `Byron` library.
This was one of the various improvements provided by `Byron` against the other `darknet`-like libraries.

Other common regularization techniques are given by the regularization of the neuron outputs with penalty loss functions.
Classical examples are given by the L1 (Laplacian) and L2 (Gaussian) penalties.
Both these functions are implemented either in `NumPyNet` and `Byron` but for sake of brevity we will not discuss about them.


[^1]: The input data to feed the Neural Network model are commonly packed into a series of *batches*, i.e small subsets of data. The BatchNorm function takes its name from this nomenclature and it processes each batch independently.

[^2]: The floating point numbers into a computer have finite precision and the variance can underflow bringing to infinite values in the BatchNorm equation.

[**next >>**](./Dropout.md)
