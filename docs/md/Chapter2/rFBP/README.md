## Replicated Focusing Belief Propagation

Up now we have implicitly talked about Neural Network models based on the standard updating rule of back-propagation.
Other learning rule for weight updates were proposed and the choice of the best one it is still an open-problem.
The final purpose is to obtain a feasible learning rule ables to model the biological learning of the human brain.

The learning problem could be faced through statistical mechanic models joined with the so-called Large Deviation Theory.
In general, the learning problem can be split in two sub-parts: the classification problem and the generalization one.
The first aims to completely store a pattern sample, i.e a prior known ensemble of input-output associations (*perfect learning*).
The second one corresponds to compute a discriminant function based on a set of features of the input which guarantees a unique association of a pattern.

From a statistical point-of-view many Neural Network models have been proposed and the most promising seems to be spin-glass models based.
Starting from a balanced distribution of the system, generally based on Boltzmann distribution, and under proper conditions, we can prove that the classification problem becomes a NP-complete computational problem.
A wide range of heuristic solutions to that type of problems were proposed.

In this section we show one of these algorithms developed by Zecchina et al. [[BaldassiE7655](https://www.pnas.org/content/113/48/E7655)] and called *Replicated Focusing Belief Propagation* (rFBP).
The theoretical background of the algorithm is beyond the scope of this thesis so we focus on its numerical implementation and optimization.

Moreover, despite their proved theoretical efficiency, the applications on real data are still few.
Thus, we show the application of the optimized version of the rFBP algorithm on a Genome Wide Association (GWA) dataset provided by the European [COMPARE project](https://www.compare-europe.eu/).
This work was also presented on the 2019 CCS-Italy (Conference of Complex System).

[**next >>**](./Implementation.md)
