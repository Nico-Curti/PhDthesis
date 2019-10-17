## Dropout function

Many times along this work we have been talked about the *over-fitting* problem.
The over-fitting problems arise when the complexity of our model becomes too high regard the amount of available data, i.e when the number of parameters of our model is comparable to the number of available data.
A classical example is given by the polynomial fitting problem.
Given an initial set of `N` data points we can always find a polynomial curve of degree equal to `N-1` which can perfectly fit our data.
In this case the model flexibility is minimum and new additional data points difficulty lies on the same curve.
In other words we tuned each model parameter according to the given data set but we completely lose the possibility of generalization.

In Neural Network models we have to manage a large quantities of parameters and it is quite easy to stumble on this problem.
Possible workaround could be given by the regularization techniques told in the previous section (ref. [BatchNorm](./BatchNorm.md) for further informations) or by a Dropout function.
This function simply dropping out some neuron units into a Neural Network during the training phase.
Ignore some neurons means that they will not be considered during a particular (single) forward/backward step.
So, given a set of neurons we have a probability `p` to keep the neuron and `1-p` to remove it.
In this way we can reduce the co-dependency of nearest neurons inside the network and so reduce the possibility of over-fitting.

The above description bring us to a straightforward implementation of the algorithm into the `NumPyNet` library (ref. [code](https://github.com/Nico-Curti/NumPyNet/blob/master/NumPyNet/layers/dropout_layer.py)).

```python
import numpy as np

class Dropout_layer(object):

  def __init__(self, prob):

    self.probability = prob
    self.scale = 1. / (1. - prob) if prob != 1 else 1.

    self.out_shape = None
    self.output, self.delta = (None, None)

  def forward(self, input):

    self.out_shape = input.shape

    self.rnd = np.random.uniform(low=0., high=1., size=self.out_shape) < self.probability
    self.output = self.rnd * input * self.scale
    self.delta = np.zeros(shape=input.shape)

  def backward(self, delta=None):

    if delta is not None:
      self.delta = self.rnd * self.delta * self.scale
      delta[:] = self.delta.copy()

```

The above code numerically reproduce the theoretical formulation given.
After the initialization of the private object variables, the forward function generates a set of random positions and apply them (if they are less than the given probability) to the output: these positions will be turned off and the others will be multiply by a scale probability factor to increase their importance.
The backward function simply invert the transformation on the back-propagated gradient `delta`.

Despite this straightforward implementation we have to carefully manage some crucial points into the `C++` equivalent.
The `Byron` library works into a single parallel region so after the (sequential) initialization of the layer object the forward/backward phases are evaluated by all the available threads in parallel.
This bring us to a standard problem in multi-threading programming: the generation of independent random numbers among threads.
Inside a parallel region all the declared variables are (by definition) shared among all the available threads.
Thus, if we simply create a random number generator we have to face on the thread-concurrency.
As consequence the random number generated will not be independent but (most probably [^1]) repeated by each thread.
The simple workaround implemented into the `Byron` library is given by assigning a random number generator to each thread (with its own seed and indexed by the thread ID).
In this way we can ensure a totally independence of the random numbers generated during the forward phase (ref. [on-line](https://github.com/Nico-Curti/Byron/blob/master/src/dropout_layer.cpp)).

![Dropout function applied on a testing image. The 10% of image pixels are turned off by the forward function. The corresponding gradient is back-propagated only on the previously activated pixels.](https://raw.githubusercontent.com/Nico-Curti/PhDthesis/master/img/dropout_layer.svg?token=AF4CJX2WAIDBKZFH4DICDJ25WGETY&sanitize=true)

As visualization example we can use our simple test image and apply our transformation (see Fig.[1](../../../../img/dropout_layer.svg)).
Our input image shows many pixel turned off according to the given probability, as expected.
On the other hand, the backward output turns on only the same pixel [^2].

A usage example of this functions is provided into the `NumPyNet` [examples](https://github.com/Nico-Curti/NumPyNet/tree/master/examples): in those simple examples we can easily compare the learning performances of standard neural network models with and without the Dropout function on classical datasets.


[^1]: The deterministic generation of random number is hard to reproduce into a parallel environment despite the seed initialization. The "probability" of repeating the same sequence is related to the affinity of each thread to the given process.

[^2]: For visualization purposes we manually set the gradient to a uniform value.


[**next >>**](./Shortcut.md)
