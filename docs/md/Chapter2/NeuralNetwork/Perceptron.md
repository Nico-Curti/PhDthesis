## Simple Perceptron

The fundamental unit of each Neural Network model is the *simple Perceptron* (or single neuron).
The *Perceptron* it the simpler mathematical model of biological neuron and it is based on the Rosenblatt [[Rosenblatt58theperceptron](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.588.3775)] model which identifies a neuron as a computational unit with input, synaptic weights and an activation threshold (or function).
Following the biological model of Hodgkin and Huxley [[HHmodel](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1392413/)]  (H-H model), we have an action potential, i.e the output of the neuron, given by

$$
y = \sigma\left(\sum_{i=1}^{N}w_i x_i + w_0 \right)
$$

where $$\sigma$$ is the activation function, $$w_i$$ are the synaptic weights and $$x_i$$ the inputs.
The $$w_0$$ coefficient identifies the bias of the linear combination and it is left as parameter to be tune by the optimization algorithm (learning phase).

The connection weights $$w_i$$ are tuned during the training section by the chosen updating rule.
The standard updating rule is simply given by

$$
w_i(\tau + 1) = w_i(\tau) + \gamma(t - y)x
$$

where $$\gamma$$ is the gain or step size ($$\gamma \in [0, 1]$$) and `t` is the desired output.
In other words we have to firstly compute the difference between the current output and the desired one, i.e the error or cost function or loss function [^1], and weight this error by the gain factor and the corresponding input.
Repeating the error computation and the updating rule we can bring the weights to convergence.
From a geometrical point-of-view this process is equivalent to an hyper-plane placement defined by $$w_0 + < w, x >$$ which splits an `n-`dimensional space into two half-spaces, i.e two desired classes.

The mathematical formulation already highlights the numerous limits of this model.
The output function is a simple linear combination of the input with a vector of weights and so only linearly separable problems can be learned [^2] by the *Perceptron* [^3].
Moreover we can manage only two classes since an hyper-plane divide the space in only two half-spaces.

A key role is assumed by the activation function.
The classical activation function used in the discrete Perceptron model is the *unit step function* (or *Heaviside step function*).
If we chose a continuous and so differentiable activation function we can treat the problem using a continuous cost function.
In this case we can define it as

$$
E(\mathbf{w}) = \frac{1}{2}\sum_{i=1}^{N}\left( t_i - y_i \right)^2
$$

where in this case both $$t_i$$ and $$y_i$$ are continuous variables, i.e floating point numbers.
Now the updating rule can be given by the gradient of the cost function applied to the original weights as

$$
\mathbf{w} = \mathbf{w} + \Delta\mathbf{w}
$$

where $$\Delta\mathbf{w}$$ is given by

$$
\Delta\mathbf{w_i} = -\gamma\frac{\partial E}{\partial w_i} = -\gamma\sum_{i=1}^{N} \left( t_i - y_i \right)\left(-x_i \right)
$$

which looks identical to previous updating rule but in this case we are managing real numbers and not simple class labels.
Moreover in this way we compute the weight updates according to the full set of training sample and not for each sample (this approach leads to the so-called *batch*-update, i.e small subsets of data).

To implement this kind of model into a pure `Python` application we do not need extra libraries but we can just use the native keyword of the language.
A possible implementation of this model was developed and release in a on-line [gist](https://gist.github.com/Nico-Curti/358b7a2ffed1abbb57ee87a5338ca073).
In this simple snippet we examine the functionality of the Simple Perceptron model across different logical functions and we proof its fast convergence on linear separable datasets [^4].

An equivalent `C++` implementation of the model is also provided and can be found in this other [gist](https://gist.github.com/Nico-Curti/856c3baf523bc5d01b1e7dfe2515c0e2).

The model is too naive for computational efficiency discussions.
Thus we can just observe how a learning algorithm could be easily implemented using basic programming language keywords either in `Python` either in `C++`.


[^1]: There are multiple loss functions in the Neural Network world. We will further discuss their use and their effective on a learning model in the next section.

[^2]: A simple mathematical proof of it can be found [here](http://www.cs.columbia.edu/~mcollins/courses/6998-2012/notes/perc.converge.pdf).

[^3]: A classical example of learning problems is given by the XOR logic function. Since the XOR output is not linearly separable the Perceptron could not converge.

[^4]: The proof the non-linear separable convergence introducing an extra stop criteria during the weights tuning given by a maximum number of step.


[**next >>**](./FullyConnected.md)
