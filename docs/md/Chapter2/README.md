# Chapter 2
## Deep Learning - Neural Network algorithms

In the first chapter we have discussed about the difficulties on extracting information from a huge amount of data, and we have proposed a novel feature extraction algorithm to face these problems.
Those kind of applications go under the wide research field of Machine Learning.
Machine learning algorithms are closely related to a statistical interpretation of the available data.
With the increasing availability of computational power and data it is not always possible to tune and build an accurate model able to describe the heterogeneity of our samples.
Many everyday problems involve very complex tasks, and we are interested on models able to solve many tasks at the same time.
From a machine learning point-of-view this can be achieved building pipelines, i.e work-flows made by multiple steps of processing, which aim to simulate as much close as possible the human intelligence.
This leads us into the Deep Learning research field, in which very computational expensive models have been built to face general purpose problems, often related to real time applications.

The description of a deep learning model is quite often given by a Neural Network architecture, i.e a more or less complex pipeline of functions which takes in input a sample and it applies a series of transformations and filters to obtain the required result.
All these pipelines are very computational expensive and they require appropriate optimization strategies.

In this chapter we introduce some of the most common functions related to deep learning pipelines, giving a very fast mathematical explanation of them and carefully focusing on their numerical issues and solutions.
We start from an introduction about general Neural Network models up to some of modern deep learning applications, involving object detection, image segmentation and image super resolution.
In particular, we describe two custom libraries (`NumPyNet` and `Byron`) developed by the author in this thesis, for education and analytic purposes, respectively.
Both libraries are released with MIT license and the codes are publicly available on my Github page ([Byron](https://github.com/Nico-Curti/Byron) and [NumPyNet](https://github.com/Nico-Curti/NumPyNet)).
These libraries have already used in several applications and in the last sections we show some of the obtained results[^1].

In the last section of this chapter we introduce a different kind of Neural Network model, `Replicated Focusing Belief Propagation` (rFBP) model.
TThis model has solid physical and statistical bases and we discuss about a novel optimized implementation, available on my Github ([Replicated Focusing Belief Propagation](https://github.com/Nico-Curti/rFBP)) and released under MIT license.
This model differs from the standard deep learning neural network changing the updating rule and we show its first application on real data.

[^1]: Both `NumPyNet` and `Byron` libraries have been developed with the collaboration of master degree students and several thesis have their applications as core arguments.


[**next >>**](./NeuralNetwork/Intro.md)
