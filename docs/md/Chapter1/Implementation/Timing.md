## Time performances

As described in the above sections, the `DNetPRO` is a combinatorial algorithm and thus it requires a particular accuracy in the code implementation to optimize as much as possible the computational performances.
The theoretical optimization strategies, described until now, have to be proved by quantitative measures.

We tested the computational performances of our `Cython` (`C++` wrap) implementation against the pure `Python` (naive) implementation shown in the previous snippet.
The time evaluation was performed using the `timing` `Python` package in which we can easily simulate multiple run of a given algorithm [^1].
In our simulations, we monitored the three main parameters related to the algorithm efficiency: the number of samples, the number of variables and (as we provided a parallel multi threading implementation) the number of threads used.
For each combination of parameters we performed 30 runs of both algorithms and we extracted the minimum execution time.
The tests were performed on a classical bioinformatics server (128 GB RAM memory and 2 CPU E5-2620, with 8 cores each).
The obtained results are shown in following Figure.
In each plot, we fixed two variables and we evaluated the remaining one.

![Execution time of `DNetPRO` algorithm. We compare the execution time between pure-`Python` (orange) and `Cython` (blue, `C++` wrap) implementation. Execution time in function of the number of variables (the number of samples and the number of threads are kept fixed).](../../../../img/features_timing.svg)

![Execution time of `DNetPRO` algorithm. We compare the execution time between pure-`Python` (orange) and `Cython` (blue, `C++` wrap) implementation. Execution time in function of the number of samples (the number of variables and the number of threads are kept fixed).](../../../../img/samples_timing.svg)

![Execution time of `DNetPRO` algorithm. We compare the execution time between pure-`Python` (orange) and `Cython` (blue, `C++` wrap) implementation. Execution time in function of the number of threads (the number of variables and the number of samples are kept fixed).](../../../../img/nth_timing.svg)

In all our simulations, the efficiency of the (optimized) Cython version is easily visible and the gap between the two implementations reached more than `10^4` seconds.
On the other hand, it is important to highlight the scalability of the codes against the various parameters.
While the code performances scales quite well with the number of features (Fig. [1](../../../../img/features_timing.svg)) in both the implementations, we have a different trend varying the number of samples (Fig. [2](../../../../img/samples_timing.svg)): the `Cython` trend starts to saturate almost immediately while the computational time of the `Python` implementation continues to grow.
This behavior highlights the results of the optimizations performed on the `Cython` implementation which allows the application of the `DNetPRO` algorithm also to larger datasets without loosing performances.
An opposite behavior is found monitoring the number of threads (ref Fig. [3](../../../../img/nth_timing.svg)): the `Python` version scales quite well with the number of threads [^2], while `Cython` trend is more unstable.
This behavior is probably due to a not optimized schedule in the parallel section: the work is not equally distributed along the available threads and it penalizes the code efficiency creating a bottleneck related to the slowest thread.
The above results are computed considering a number of features equal to 90 and, thus, the parallel section distributes the 180 `(N x N)` iterations along the available threads: when the number of iterations is proportional to the number of threads used (12, 20 and 30 in our case), we have a maximization of the time performances.
Despite of this, the computational efficiency of the `Cython` implementation is much better than the `Python` one, of which the usage is indisputable.


[^1]: We would stress that we can use the `timing` `Python` package only because we provided a `Cython` wrap of our `DNetPRO` algorithm implementation. We would also highlight that, albeit minimal, the Python superstructure penalizes the computational performances and the best results can be obtained using the pure C++ version of the code.

[^2]: The optimal result should be a linear scalability with the number of threads but it is always difficult to reach this efficiency. Thus, a reasonable good result is given by a progressive decrease with increasing the number of threads.

[**next >>**](../Synapse/README.md)