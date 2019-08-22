#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import random
from operator import mul
from operator import add

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'Simple Perceptron'


class Perceptron (object):

  def __init__ (self, num_inputs=2, seed=123):
    '''
    Simple Perceptron Classifier

    The simple Perceptron is the computational unit of each
    fully connected Neural Networks.
    It represents the simplest mathematical model of a biological
    neuron.

    The given input is weighted by the internal set of parameter
    of the model through a simple linear combination (+ bias).

    The model is able to discriminate only linear separable data.
    To obtain more complex discriminant functions you can just
    put multiple Perceptron into a graph interation (connected NN).

    A classical example impossible to solve by this model is given by
    the simple XOR logical function.
    Try yourself if you do not trust me.
    '''
    # reproducibility
    random.seed(seed)

    self._bias = random.uniform(a=0.,b=1.)
    self._weights = [random.uniform(a=0., b=1.)
                     for _ in range(num_inputs)]

  def predict (self, X):
    '''
    Evaluate Perceptron output

    Parameters
    ----------
      x : array-like
          1D array of inputs as array of float

    Returns
    -------
      res : int (0 or 1)
           The predicted belonging class

    Notes
    -----
    The perceptron function computes the output following the formula

    $$
    y = \sum_{i=1}^{N}{w_i x_i} + w_0
    $$

    where $w_i$ are the weights array and $w_0$ the bias.
    '''
    return sum(map(mul, self._weights, X), 0.) + self._bias > 0.

  def fit (self, X, y, max_iters=100, gamma=.1):
    '''
    Optimization of the Perceptron parameters

    Parameters
    ----------
    X : array of shape [n_samples, n_features]
        The input samples.

    y : array of shape [n_samples]
        The target values.

    max_iters : int (default=100)
        Maximum number of iteration to perform (stop criteria)
        A second stop criteria is given by the number of errors.

    gamma : float (default=.1)
        Learning rate parameter

    Results
    -------
      self

    Notes
    -----
    The perceptron learning rule follows the equation

    $$
    w_i(\tau + 1) = w_i (\tau) + \gamma * x_i * (t_i - y_i)
    $$

    where $t_i$ are the true labels and $y_i$ the predicted ones.
    '''

    number_of_errors = -1 # default initialization
    iteration = -1 # default initialization to start the iterations

    while number_of_errors != 0 and iteration <= max_iters:

      iteration += 1 # increase here to print the right result
      number_of_errors = 0

      for xi, yi in zip(X, y):
        error = yi - self.predict(xi) # error function

        if error:
          # update bias
          self._bias += gamma * error
          weights_update = map(lambda xi : gamma * error * xi, xi)
          # update weights
          self._weights  = list(map(add, self._weights, weights_update))

          number_of_errors += 1

    # just print some infos
    print('# errors : {:d}'.format(number_of_errors))
    print('# iterations : {:d}'.format(iteration))

    return self


if __name__ == '__main__':

  def nand (X):
    return [not ( x and y ) for x, y in X]

  def xor (X):
    return [bool(x) ^ bool(y) for x, y in X]

  import itertools

  num_inputs = 2
  neuron = Perceptron(num_inputs=num_inputs)

  X = list(itertools.product([0, 1], [0, 1]))
  y = nand(X)

  neuron.fit(X, y)

