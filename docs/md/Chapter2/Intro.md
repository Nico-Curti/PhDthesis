# Chapter 2
## Deep Learning - Neural Network algorithms

In the first chapter we have discussed about the difficulties on extracting informations from a huge amount of data and we have proposed a novel feature extraction algorithm to face on these problems.
Those kind of applications go under the wide research field of Machine Learning.
Machine learning algorithms are closely related to a statistical interpretation of the theoretical background of the available data.
With the increasing of computational power and the quantity of available data it is not always possible to tune and build an accurate model able to describe the heterogeneity of our samples.
Many everyday problems involve very complex tasks and looking for an automatic solution for each of them we are interesting on models able to solve many tasks at the same time.
From a machine learning point of view this can be achieved building pipelines, i.e work-flow made by multiple step of processing, of algorithms which aims to simulate as much closed as possible the human intelligence.
This bring us into the Deep Learning research field, in which very computational expensive models were build to face on general purposes problems, often related to real time applications.

The description of a deep learning model is quite often given by a Neural Network architecture, i.e a more or less complex pipeline of functions which takes in input a sample and it applies a series of transformations and filters to obtained the required result.
All these pipelines are very computational expensive and they require appropriated optimization strategies to be improve or at least usable.
The numerical component is becoming even more crucial for modern applications and many researches are focusing on that.

In this chapter we will only summary introduce some of the most common functions related to these deep learning pipelines, giving a very fast mathematical explanation of them and carefully focusing on their numerical issues and solutions.
We will start from an introduction about general Neural Network models until some of the modern deep learning applications, involving object detections, image segmentation and the new image super resolution tasks.
In each section we will discuss about the more or less new numerical solutions developed to overcome the issues related to that task and developed during this work of thesis.
In particular we will help in the description by two custom libraries (`NumPyNet` and `Byron`) developed in this work, for educational and performances purposes, respectively.
Both libraries are released with MIT license and the codes are public available on my Github page ([Byron](https://github.com/Nico-Curti/Byron) and [NumPyNet](https://github.com/Nico-Curti/NumPyNet)).
These libraries have already used in different kind of applications and in the last sections we will show some of the obtained results[^1].

In the last section of this chapter we will also introduce a different kind of Neural Network model.
This model starts from a complex and theoretically proofed physical and statistical model and we will discuss about a novel custom implementation also in this case public available on my Github page ([Replicated Focusing Belief Propagation](https://github.com/Nico-Curti/rFBP)) and release under MIT license.
This model differs from the standard deep learning neural network changing the updating rule to tune the model parameters and in this work we will show its first application on real data.

[^1]: Both the `NumPyNet` and `Byron` libraries have been developed by the collaboration of master degree students and multiple thesis have taken their use as main argument.


[**next >>**](./NeuralNetwork/Intro.md)
