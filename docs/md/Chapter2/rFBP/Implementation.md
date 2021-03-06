## Algorithm Optimization

The `rFBP` algorithm is a learning algorithm developed to justify the learning process of a binary neural network framework.
The model is based on a spin-glass distribution of neurons put on a fully connected neural network architecture.
In this way each neuron is identified by a spin and so only binary weights (-1 and 1) can be assumed by each entry.
The learning rule which controls the weight updates is given by the Belief Propagation method.

A first implementation of the algorithm was proposed in the original paper [[BaldassiE7655](https://www.pnas.org/content/113/48/E7655)] jointly with an open-source Github repository.
The original version of the code was written in `Julia` language and despite it is a quite efficient implementation the `Julia` programming language stays on difficult and far from many users.
To broaden the scope and use of the method, a `C++` implementation was developed with a joint `Cython` wrap for `Python` users.
The `C++` language guarantees better computational performances against the `Julia` implementation and the `Python` version enlarge its usability.
This implementation is optimized for parallel computing and is endowed with a custom `C++` library called `Scorer` (see [Appendix D](../../Appendix/Scorer/README.md) for further details), which is able to compute a large number of statistical measurements based on a hierarchical graph scheme.
With this optimized implementation we try to encourage researchers to approach these alternative algorithms and to use them more frequently on real context.

As the `Julia` implementation also the `C++` one provides the entire `rFBP` framework in a single library callable via a command line interface.
The library widely uses template syntaxes to perform dynamic specialization of the methods between two magnetization versions of the algorithm.
The main object categories needed by the algorithm are wrapped in handy `C++` objects easy to use also from the `Python` interface.
A further optimization is given by the reduction of the number of available functions: in the original implementation a large amount of small functions are used to perform a single complex computation step, enlarging the amount of call stack; in the `C++` implementation the main functions are re-written with the minimizing the call stack to ease the vectorization of the code.

The full `rFBP` library is released under MIT license and it is open-source on Github [[ReplicatedFocusingBeliefPropagation](https://github.com/Nico-Curti/rFBP)].
The on-line repository provides also a full list of installation instructions which could be performed via [`CMake`](https://github.com/Nico-Curti/rFBP/blob/master/CMakeLists.txt) or [`Makefile`](https://github.com/Nico-Curti/rFBP/blob/master/Makefile).
The continuous integration of the project is guaranteed in every operative system using [`Travis CI`](https://github.com/Nico-Curti/rFBP/blob/master/.travis.yml) and [`Appveyor CI`](https://github.com/Nico-Curti/rFBP/blob/master/appveyor.yml) which test more than 15 different `C++` compilers and environments.

The `Python` wrap guarantees also a good integration with the other common Machine Learning tools provided by `scikit-learn` `Python` package; in this way we can use the `rFBP` algorithm as equivalent alternative also in other pipelines.
Like other Machine Learning algorithm also the `rFBP` one depends on many parameters, i.e its hyper-parameters, which has to be tuned according to the given problem.
The `Python` wrap of the library was written according to `scikit-optimize` `Python` package to allow an easy hyper-parameters optimization using the already implemented classical methods.


![Comparison of time performances between the original `Julia` implementation and our `Cython` one of the `rFBP` algorithm varying the input dimension sizes (number of samples, `M`, and number of variables, `N`). For each input configuration 100 runs of both algorithm were performed and the results were normalized by the `Julia` implementation. In these cases we fixed the magnetization to **MagP64**.](../../../../img/rfbp_magp_timing.svg)

![Comparison of time performances between the original `Julia` implementation and our `Cython` one of the `rFBP` algorithm varying the input dimension sizes (number of samples, `M`, and number of variables, `N`). For each input configuration 100 runs of both algorithm were performed and the results were normalized by the `Julia` implementation. In these cases we fixed the magnetization to **MagT64**.](../../../../img/rfbp_magt_timing.svg)

We firstly test the computational efficiency of our implementation against the original `Julia` one.
The tests were performed comparing our `Cython` version of the code (and thus with a slight overhead given by the `Python` interpreter) and the `Julia` implementation as reference.
Varying the dimension sizes (number of samples, `M`, and number of variables, `N`) we tested the time efficiency over 100 runs of both the algorithms.
We divided our simulation according to the two possible type of magnetizations (`MagP64` and `MagT64` as described by the original implementation available [here](https://github.com/carlobaldassi/BinaryCommitteeMachineFBP.jl)) and the obtained results are shown in Fig. [[1](../../../../img/rgbp_magp_timing.svg), [2](../../../../img/rgbp_magt_timing.svg)], respectively.

As can be seen by the two simulations our implementation always overcome the time performances of the original one, taken as reference in the plot.
However, we can not guarantee a perfect parallel execution of our version: also with multi-threading support the scalability of our implementation does not follow a linear trend with the number of available cores.
In our simulation, in fact, we used 32 cores against the single thread execution of the `Julia` implementation but we gained only a 4x and 2x of speedup for `MagT64` and `MagP64`, respectively.
The network training is a sequential process by definition and thus it is hard to obtain a relevant speedup using a parallel implementation.
In this case it is probably jointed to a not perfect parallelization strategy chosen which bring to a not efficient scalability of our algorithm version.
However, the improvements performed to the code allow us to use this algorithm with bigger dataset sizes.


[**next >>**](./Dataset.md)
