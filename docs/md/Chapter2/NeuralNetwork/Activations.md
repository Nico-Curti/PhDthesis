## Activation Functions

Activation functions (or transfer functions) are linear or non linear equations which process the output of a Neural Network neuron and bound it into a limit range of values (commonly $$\in[0, 1]$$ or $$\in[-1, 1]$$).
The output of a simple neuron [^1] can be computed as dot product of the input and neuron weights (see previous section); in this case the output values ranging from $$-inf$$ to $$+inf$$ and moreover it is just a simple linear function.
Linear functions are very simple to trait but they are limited in their complexity and thus in their learning power.
Neural Networks without activation functions are just simple linear regression model (see the fully connected Neural Network properties in the previous section).
Neural Networks are considered as *Universal Function Approximators* so the introduction of non-linearity allows them to model a wide range of functions and to learn more complex relations in the pattern data.
From a biological point of view the activation functions model the on/off state of a neuron in the output decision process.

Many activation functions were proposed during the years and each one has its characteristics but not an appropriate field of application.
The better activation function to use in a particular situation (to a particular problem) is still an open question.
Each one has its pro and cons in some situations so each Neural Network library implements a wide range of them and it leaves to the user to perform his own tests.
In the following Table we show the list of activation functions implemented in our libraries with mathematical formulation and corresponding derivative (ref. [`activations.py`](https://github.com/Nico-Curti/NumPyNet/blob/master/NumPyNet/activations.py) for the code implementation).
An important feature of any activation function, in fact, is that it should be differentiable since the main procedure of model optimization implies the backpropagation of the error gradients.


**INSERT TABLE HERE**


As can be seen in Table it is easier to compute the activation function derivative as function of it.
This is a (well known) important type of optimization in computation term since it reduces the number of operations and it allows to apply the backward gradient directly.

To better understand the effects of activation functions we can apply these functions on a simple test image and see the results.
This can be easy done using the example scripts inserted inside our library.

<img src="../../../../img/activations_layer.png" width="400px;"/>

In the Figure the effects of the told above functions are reported on a test image.
For each function we show the output of the activation function and its gradient.
For visualization purposes the image values are rescaled $$\in[-1, 1]$$ before the input to the functions.
From the results given in Figure we can better appreciate the differences between the mathematical formulas: a simple Logistic function does not produce evident effects on the test image while a Relu activations tends to overshadow the image pixels.
This features of the Relu activation function are very useful in Neural Network model and they also determine important theoretical consequences which led it to be one of the most prominent solution for many Neural Network models.

The ReLU (Rectified Linear Unit) activation functions are, in fact, the most used into the modern Neural Networks models.
Their diffusion is imputed to their numerical efficiency and to the benefits they bring [[Glorot2011Relu](http://proceedings.mlr.press/v15/glorot11a.html)]:

* Information disentangling: the main purpose of a Neural Network model is to tune a discriminant function able to associate a set of input to a prior-known output classes.
  A dense information representation is considered *entangled* because small differences in input highly modifies the data representation inside the network.
  On the other hand, a sparse representation tends to guarantee a conservation of the learning features.

* Information representation: different inputs can lead different quantities of useful informations.
  The possibility to have null values in output (ref Table) allows a better representation of the representation dimension inside the network.

* Sparsity: sparsity representation of data are exponentially efficient in comparison to dense ones, where the exponential power is given by the number of no-null features [[Glorot2011Relu](http://proceedings.mlr.press/v15/glorot11a.html)].

* Vanish gradient reduction: if the activation output is positive we have a no-bound gradient value.

In the next sections we will discuss about different kind of Neural Network models and in all of them we choose to use Relu activation function in the major part of the layers.


[^1]: We assume for simplicity a fully connected Neural Network neuron.

[**next >>**](./Convolutional.md)
