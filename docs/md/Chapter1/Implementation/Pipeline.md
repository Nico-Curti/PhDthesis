## DNetPRO in Snakemake

The starting (silent) hypothesis done up to now is that we want to run the `DNetPRO` algorithm on a single dataset (or better on a single Hold-Out subdivision of data).
On this configuration it is legal to stress as much as possible the available computational resources and parallelize each step of the algorithm.

If we want to use our algorithm into a larger pipeline, in which we compare the resulting obtained over a Cross-Validation, we have to re-think about the parallelization done.
In this case, each fold of the cross validation can be interpreted as an independent task and, following the main programming rule *"parallelize the outer, vectorize the inner"* we should spawn a thread for each fold and perform the couple evaluation in sequential mode.
Certainly, the optimal solution would be to separate our jobs across a wide range of inter-connected computers, performing the same computation in parallel, but it would required to implement our hybrid (`C++` and `Python`) pipeline into a Message Passing Interface (MPI) environment.

The easier solution to overcome all these problems can raise by the use of `SnakeMake` [[snakemake](https://snakemake.readthedocs.io/en/stable/)] rules.
`SnakeMake` is an intermediate language between `Python` and Make.
Its syntax is almost like the `Make` language, but with the help of the easier and powerful `Python` functions.
It is widely used for bioinformatics pipeline parallelization, since it can be easily applied over single or multi-cluster environments (master-slave scheme) with a simple change of command line.

![Example of `DNetPRO` pipeline on a single cross validation. It is highlighted the independence of each fold from each other. This scheme shows a possible distribution of the jobs on a multi-threading architecture or for a distributed computing architecture. The second case allows further parallelization scheme (hidden in the graph) for each internal step (e.g. the evaluation of each pair of genes).](../../../../img/qdanet_pipe_single.png)

So, to improve the scalability of our algorithm we implemented the benchmark pipeline scheme using Snakemake rules and a work-flow example for a single cross-validation is shown in Fig. [1](../../../../img/qdanet_pipe_single.png).
In this case each step of Fig.[1](../../../../img/qdanet_pipe_single.png) can be performed by a different computer-unit, preserving the multi-threading steps with a maximum scalability and possibility to enlarge the problem size (number of variables).


[**next >>**](./Timing.md)
