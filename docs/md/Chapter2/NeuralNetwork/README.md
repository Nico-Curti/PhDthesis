## Neural Network models

Neural Networks are mathematical models commonly used in data analysis.
They are becoming a standard tool in Machine Learning and Deep Learning research and many complex problems can be easily solved by these models.
From a theoretical point-of-view we can define a Neural Network as a series of non-linear multi-parametric functions.
The model parameters are tuned during a so called *training section* in which we feed our model with a set of data with human supervision, i.e we have prior knowledge about the right and desired output of the model.
After the training section we can verify the efficiency of our training using a new set of data, called *test set*, which is never seen by the model.
If we have prior knowledge about the output of our test set we can compute the accuracy (or more generally the score) of our model; in the other case we will simply have an extrapolation of our data.

A wide range of documentations and implementations have been written on this topic and it is more and more hard to move around the different sources.
Leader on this topic are became the multiple open-source `Python` libraries available on-line as [[Tensorflow](http://tensorflow.org/)], [[Pytorch](http://pytorch.org/)] and [[Caffe](http://doi.acm.org/10.1145/2647868.2654889)].
Their portability and efficiency are closely related on the simplicity of the `Python` language and on the simplicity in writing complex models in a minimum number of code lines.
Only a small part of the research community uses more deeper implementation in `C++` or other low-level programming languages.
About them it should be mentioned the *darknet project* of Redmon J. et al. which created a sort of standard in object detection applications using a pure `Ansi-C` library[^1].


In this section we firstly retrace the mathematical background of these models.
To each theoretical explanation we discuss the numerical problems associated and we provide an efficient custom implementation of each algorithm.
The numerical aspects will be traced following two developed custom libraries: `NumPyNet` library [[NumPyNet](https://github.com/Nico-Curti/NumPyNet)] and `Byron` library [[Byron](https://github.com/Nico-Curti/Byron)].

`NumPyNet` was born as educational framework for the study of Neural Network models.
It is written trying to balance code readability and computational performances and it is enriched with a large documentation to better understand the functionality of each script.
The library is written in pure `Python` and the only external library used is `Numpy` [[Numpy](http://www.numpy.org/)]  (a based package for the scientific research).

Despite all common libraries are correlated by a wide documentation is often difficult for novel users to move around the many hyper-links and papers cite in it.
`NumPyNet` tries to overcome this problem with a minimal mathematical documentation associated to each script and a wide range of comments inside the code.

An other "problem" to take in count is related to performances.
Libraries like `Tensorflow` are certainly efficient by a computational point-of-view and the numerous wrappers (like `Keras` library) guarantees an extremely simple user interface.
On the other hand the deeper functionalities of the code and the implementation strategies used are unavoidably hidden behind tons of code lines.
In this way the user can performs complex computational tasks using the library as black-box package.
`NumPyNet` wants to overcome this problem using simple `Python` codes with extremely readability also for novel users to better understand the symmetry between mathematical formulas and code.

The simplicity of this library we will allow to give a first numerical analysis of the model functions and, moreover, to show the results of each function to a simple image to better understand the effects of their applications on real data[^2].
Each `NumPyNet` function was tested against the `Tensorflow` implementation of the same methods with an automatic testing routine through `PyTest` [[Okken:2017:PTP:3176124](https://docs.pytest.org/en/latest/)].
The full code is open-source on the Github page of the project.
Its installation is guaranteed by a continuous integration framework of the code through `Travis CI` for Unix environments and `Appevyor CI` for `Windows` users.
The library supports `Python` version >= 2.6[^3].

As term of comparison we will discuss the more sophisticated implementations into the `Byron` library.
`Byron` (*Build YouR Own Neural network*) library is written in pure `C++` with the support of the modern standard 17.
We deeply use the `C++17` functionality to reach the better performances and flexibility of our code.
What makes `Byron` an efficient alternative to the competition is the complete multi-threading environment in which it works.
Despite the most common Neural Network libraries are optimized for GPU environments, there are only few code implementations which exploit the fully functionality of a multiple CPUs architecture.
This gap discourage multiple research groups on the use of such computational intensive models in their applications.
`Byron` works in a fully parallel section in which each single computational function is performed using the full set of available cores.
To further reduce the time of thread spawn and so optimize as much as possible the code performances, the library works using a single parallel section which is opened at the beginning of the computation and closed at the end[^4].

The `Byron` library is release under MIT license and publicly available on the Github page of the project.
The project also includes a list of common examples like object detection, super resolution, segmentation, ecc. (see the next sections for further details about this models).
The library is also completely wrapped using `Cython` to enlarge the range of users also to the `Python` ones.
The complete guide to its installation is provided; it can be done using `CMake`, `Make` or `Docker` and the `Python` version is available with a simple `setup`.
The testing of each function is performed using `Pytest` automatic framework against the `NumPyNet` implementation (faster and lighter to import than `Tensorflow`).

We will use `Byron` library as term of comparison with the other common library used in Neural Network models and for each function we test its computational efficiency and scalability on multiple cores.
Two machines will be used in the computational testing: a common laptop (8 GB RAM memory and 1 CPU i7-6500U, with 2 cores) and a classical bioinformatics server (128 GB RAM memory and 2 CPU E5-2620, with 8 cores each).

Starting from the next section we introduce the fundamental Neural Network model, the so-called *Simple Perceptron*.
From the simplest model we will add complexity layers to overcome the relative problems (mathematical and numerical), introducing the main functionality of the modern Neural Network architectures.

[^1]: `Darknet` is framework for neural network model developing. It is written in pure `Ansi-C` by a Washington University research group. The library was developed only for Unix OS but in its many branches (literally *forks*) a complete porting for each operative system was provided. The code is particularly optimized for GPUs using the CUDA support, i.e only for NVidia GPUs. It is particularly famous for object detection applications since it firstly theorize a novel approach to multi-scale object detections called Yolo (You Only Look Once). The library developed in this work are all inspired on it. The large part of the original work developed is related to a deep optimization of this library either in terms of functionality and issues either in terms of computational performances.

[^2]: Aware of the author no other example implementations have been done. This makes the `NumPyNet` library a useful tool for neural network study and a virtual laboratory for new neural network functions.

[^3]: The library provides also an `Image` object to load and process images. The object is based on `OpenCV` API [[OpenCV](https://github.com/opencv/opencv)]. `OpenCV` does not yet support `Python` version 2.7 and 3.3 so the whole `NumPyNet` package does not work on these two version of `Python`. You can just exclude the `Image` scripts from the package or use a novel wrap based on different library (e.g `Pillow`).

[^4]: For real-time applications also the time required for the thread spawn must be taken into account.


[**next >>**](./Perceptron.md)
