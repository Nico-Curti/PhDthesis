## Cost function

A machine learning algorithm is used to minimize or maximize a cost function.
In other words when we implement a machine learning algorithm we want to know how good is our result according to prior knowledge about the desired results.
So we have to establish a function ables to represent the error of our model.
This kind of function are commonly called *error functions* or *loss functions* or just simply *cost function*.
In the previous sections we have shown many algorithms used into a Neural Network model and we have talked about how to update the functional parameters according to the evaluated error.
This error is provided by the cost function.

The cost function represents the final output of our Neural Network model so it is reasonable to talk about it at the end of this chapter.
There are many kinds of loss functions and there is not a particular one able to works with all kinds of data.
So we have to pay attention to chose the right one in our problems.
In particular we have to take in count the possible presence of outliers, the structure of our model, the computational efficiency of our algorithm and most of all the number of classes that we want to predict.
Broadly, we can classify the loss functions into two major categories: the classification losses and the regression losses.
In the first case we want to predict a finite number of categorical values (classes).
In the second case the prediction is performed on a series of continuous values.
Since in this work we are focusing only on classification problems we will only talk about the first case.

The most common cost function is given by the *Mean Square Error* (MSE) or *L2 loss* (very closed to the regularization function hinted at the end of [BatchNorm](./BatchNorm.md)).
Its mathematical formulation is quite simple and it is given by

$$
MSE = \frac{\sum_{i=1}^{N}\left( y - t \right)^2}{N}
$$

where we follow the nomenclature given in [perceptron](./Perceptron.md) and `N` is the number of output which is equivalent to the number of classes.
It is one of the most used cost function due to its simplicity either from a mathematical either from a numerical point of view.
The possible range of values ranged from 0 to $$\infty$$.
With MSE function the predictions which are far away from actual values are heavily penalized, due to the squaring.

A slight different function is given by the *Mean Absolute Error* (MAE) or *L1 loss* in which we replace the squaring with a module of the error.

$$
MAE = \frac{\sum_{i=1}^{N}|\left( y - t \right)|}{N}
$$

With MAE we loose the information about the error direction (preserved by the squaring in MSE) and just simply evaluate the absolute value of it.

The main differences between these two functions can be summarized as follow: using the MSE function we can easily solve the problem but the MAE function is more robust against possible outliers.
Despite both functions reach the minimum in a perfect classification configuration (error equal to zero), in presence of outliers we have to manage with large differences in the numerator of the function.
With large differences, the square values are greater than the absolute values but while the MSE tries to adjust its performance to minimize those cases, the other samples pay the higher cost.

A problem related to the MAE function arises during the gradient evaluation.
Its gradient, in fact, is the same throughout, which means that we will have large gradient values also with small differences which is a worse configuration during the training.
A simple possible workaround is to introduce a shrinking parameter, given by a dynamic learning rate, when we move closer to the minimum.

When we have to manage multi-class problems there are other common cost functions based on likelihood scores.
The simpler one is the *Cross Entropy loss* or *Log loss*:

$$
CrossEntropyLoss = -(y\cdot\log(t) + (1 - y)\cdot\log(1 - t))
$$

This function just multiply the log of the actual predicted probability by the ground truth class.
In this way when we have two classes (e.g $$t \in [0, 1]$$) we can alternatively nullify the two parts of the function [^1].
In this way the loss function heavily penalizes the predictions that are confident but wrong.
This function works with binary classification problems where the output classes are binned in `[0, 1]`.
For this reason the output of the model must be constrained into the `[0, 1]` domain and thus a proper activation function should be provided.
Classically this loss function is used jointly to the sigmoid activation (ref. [Activations](./Activations.md)) which constrains the output of the model in the desired interval.
For this reason in our implementation of the algorithm we chose to merge the sigmoid function and the Log Loss function into a single object [^2].

A last duty to mention loss function is the extension of the Log loss to multiple classes, the so-called *Categorical Cross Entropy Loss*.

$$
CategoricalCrossEntropyLoss = -\sum{i=1}^{N}\left( y\cdot\log(t) \right)
$$

This function generalized the previous one for multiple-classes, i.e for problems where the correct output can be only one.
The loss compare the distribution of the predictions, i.e output of the model, with the prior known distribution.
In this way only the probability of the true class will be 1 and all the other classes will be set to 0.
Also in this case we have to pay attention to the output of our model which is intended as a probability value ranging in `[0, 1]`.
In particular this function commonly works jointly to a softmax activation function.
As in the previous case we chose to implements this loss function in a separated object associated to the softmax transformation.

Many other loss function can be mentioned to overcome different kind of problems.
The list of presented loss function was related to the implementation of the `darknet`-like library which are ported also into the `NumPyNet` and `Byron` libraries, i.e either in `Python` and `C++`.
`NumPyNet` and `Byron` libraries also provided a wider list of loss functions to improve the usability of them and improve their computation (and fixed some `darknet` issues).
A full list of available loss functions can be found in the [on-line](https://github.com/Nico-Curti/Byron/blob/master/src/cost_layer.cpp) version of the libraries with a list of easily visual examples.

A further improvements was given from a numerical point-of-view: many mathematical formulas needs expensive math operations as logarithms and trigonometric functions.
An efficient (but approximated) math formulas was implemented both in the `C++` and Python to reach faster computational performances.
These numerical math operations are widely used into the `Byron` library to increase the performances despite their used can be turned off by user at compile time in `Byron`.
The full set of functions, in fact, is enclosed into a `macro` definition (`__fmath__`) that can be enabled at compile-time.

A classical example of this faster math operation is given by the *fast inverse square root* algorithm, firstly introduced in 1999 in the source code of *Quake III Arena*, a first-person shooter video game.
The method is based on a Newton algorithm which can be stopped at the desired precision order: less precision is associated to faster execution, obviously.
In our `fast math` implementation we provide a set of Newton algorithms associated to the most common mathematical operations, like `exp`, `log`, `sqrt` and so on.
We tested these implementations against the common standards (`Numpy` package for `Python` and `std::` for `C++`) and we compare the time execution performances (we required a precision of at least `10^-4`).
The obtained results are shown in Fig. [1](../../../../img/fmath_timing.svg) where we normalized the execution time taking `Numpy` implementation as reference.

![Time performances of standard mathematical operations implemented through Newton approximations. We compare the results obtained with the `Numpy` library (blue, reference) and the standard `C++` library (`CMath`) to their equivalent into the custom `FMath` version. In the comparison we have to take in mind that the `Numpy` library is based on a `C++` wrap and that the `Python` version of the `FMath` is written in pure `Python` language. In all the cases the `FMath` version of the functions performs better or at-least-equal to the standard one.](../../../../img/fmath_timing.svg)

As can be see all the results obtained by the `fast math` algorithms are faster or at least equals to the standard ones.
The `C++` version of the `fast math` is certainly the better choice for an efficient implementation of the algorithms in all the cases and it is interesting to notice how some functions (`pow2` and `log10`) are drastically slower in `C++` than in `Python`, despite the intrinsic overhead of the `Python` language.
This is probably due to particularly optimizations performed by the `Numpy` package in the implementation of these special cases: if we compare those functions to the general ones (`pow` and `log`), in fact, the results confirm the efficiency of the `C++` language.

These results highlight the importance of code testing before release it: we have to pay always attention in writing a code and query also the standard choices.


[^1]: When the actual label is equal to 1, i.e `y=1`, the second half of the Log Loss function disappears whereas in case of actual label is equal to 0 the first half is null.

[^2]: We also try to prevent wrong uses of this loss function for laypersons. This implementation was already suggested by the `darknet` library so we simply propagate it in our implementations.


[**next >>**](../SuperResolution/Intro.md)
