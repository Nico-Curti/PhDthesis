## Synthetic dataset benchmark

Standard feature selection algorithms test single-variable performances.
Starting from the ranked variables according to their scores, a signature is obtained selecting the top scorer ones according to an iterative addition of variables until a desired output score is reached.
These methods-like are called `K`-best algorithms and they filter the number of variables without any constrain on their mutual interaction or correlation.
On the other hand, the proposed `DNetPRO` algorithm tries to extract the more statistically significant variables considering the interaction between them, i.e the combination of variable-pairs.
Thus, while the `K`-best algorithm scaled according to the number of variables, the `DNetPRO` algorithm is more computational expensive and its usage can be justify only if its efficiency can be proved.

We developed a toy model simulation to compare the performances of the standard `K`-best algorithm with the `DNetPRO` , considering either the number of samples and the number of variables.
Since the `DNetPRO`  algorithm was designed to gene expression dataset applications, our toy model should consider a large number of variables with only a relative small number of samples.
To simulate a so like synthetic dataset, we used a toy model generator provided by the [scikit-learn package](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html).
i.e. variables which easily separate the class populations, and *redundant features*, i.e. variables which represent noise in our problem.
The number of informative features should be realistically small compared to the noise, so in our simulations we chose to introduce a maximum of 1% informative features in each simulation.

We randomly generated data from Gaussian distributions with an increasing number of samples and variables, i.e dimensions.
In each simulation we split the number of samples in training and test sets (Hold-Out method, with 2/3 of data as training and 1/3 as test) and we applied the `DNetPRO` algorithm.
From each simulation we tested the extracted signatures on the test set, keeping the best performing one.
On the same data-subdivision we applied the `K`-best algorithm, filtering the same number of variables of the `DNetPRO` best signature, i.e `K` equal to the number of nodes in the `DNetPRO` best signature.
In this way, we can compare the performances obtained on the test set by the two methods.
We would highlight that, in general, there is not a stop criteria for the `K`-best algorithm, so the number of variables selected could be smaller or greater than the number of `DNetPRO` signature nodes.
However, we can reasonably assume that, according to the `K`-best interpretation, the selected features should be the most performing ones, and the addition of more variables should introduce only a small quantity of noise.
In Fig. [2](../../../../img/samples_toy.png) we show the results obtained in our simulations, keeping fixed the number of variables/samples and varying the number of samples/variables (Fig. [2](../../../../img/samples_toy.svg)(a) and Fig.[2](../../../../img/features_toy.svg)(b) respectively).

![Synthetic dataset simulation. Comparison of accuracy performances obtained by the `DNetPRO` algorithm and the `K`-best algorithm. Performances obtained in function of the number of samples, keeping fixed the number of variables.](../../../../img/samples_toy.svg)

![Synthetic dataset simulation. Comparison of accuracy performances obtained by the `DNetPRO` algorithm and the `K`-best algorithm. Performances obtained in function of the number of variables, keeping fixed the number of samples.](../../../../img/features_toy.svg)

For the same number of variables (Fig.[2](../../../../img/samples_toy.svg)(a)) we noticed as the two methods perform quite similar but the `DNetPRO` is able to reach better performances as the number of samples increase.
This trend can be explained also in statistical terms: with small samples the variability of our (random) data is large and the performance distributions are more unstable.
With a greater number of samples, the variances of our classes are reduced, and the statistical quantities involved in the computation of the discriminant curve can be evaluated with more accuracy.
As the number of samples increase, the statistical evaluation of variables becomes easier and the correspondence between the top scorer variables and the true-informative ones increases.
In low sample cases, the quantity of noise is big and in a high dimensional space is hard to find the most informative directions: noise variables could reach higher performances than the informative ones in these cases.

Despite of the simplicity of our toy model, the `DNetPRO` is able to highlight its efficiency in terms of performances against the single-feature method.
A slight different behavior is shown by varying the number of variables and keeping fixed the number of samples (Fig.[2](../../../../img/features_toy.svg)(b)).
In this case we noticed that the median accuracy (black line in the plot) of the `DNetPRO` algorithm always outperforms the `K`-best one.
With a small number of variables (left part of the plot) the `K`-best algorithm performances are more stable and, only from a statistical point-of-view, we can prove the efficiency of the `DNetPRO` algorithm (the median of the distribution is still higher compared to the `K`-best one).
As the number of variables increase, also the efficiency of the `DNetPRO` algorithm increases up to it exceeds the `K`-best algorithm (and its distribution is narrowed).
We reached this situation quite faster in our simulation since we constrained our toy model with a forced unbalance between the number of samples and variables, i.e the so-called ill-posed problems.
The `DNetPRO` was designed to work in these situations and it is able to reach high accuracy results also in critical ill-posed problems.
The pair-variables evaluation could be helpful to find good variables which are penalized in the single score ranking, but which can prove a good performance-interaction with the others.
In these cases, the `DNetPRO` results could be helpful also to understand the variable interactions, due to the network structure of the signature that can bring to deeper considerations on the fine grain cooperation of variables in a real problem context.

This kind of toy model is considered as a standard for feature selection testing but it puts several disadvantages for the `DNetPRO` evaluation.
We started our discussion about the `DNetPRO` taking into account the two distributions of data showed in Fig.[1](../../../../img/expression.svg)(a).
The `DNetPRO` algorithm was designed to face that kind of situations in better way.
The limits of our algorithm are so bounded to the sample distributions: if the informative variables are totally independent one from each others, the couples evaluation does not guaranteed the best approach to the problem.
Considering the signatures extracted by the `DNetPRO` algorithm we noticed this kind of behavior: the core of our signatures was principally composed by informative variables (which were manually introduced so easily traced) into a star-network structure.

We have to face also the problem of multiple putative (disjointed) signatures: the `DNetPRO` algorithm takes into account only the connected components with the highest score as putative signature.
If the informative variables are disjointed, the corresponding star-networks will be disjointed.
This means that we have to enlarge the amount of nodes in our signature.

We evaluated both these situations in our toy model simulations.
In the first case, we introduced only two informative variables obtained by a sampling of the distribution showed in Fig.[1](../../../../img/expression.svg)(a).
In all our simulations, the `DNetPRO` algorithm was able to identify the couple of these variables as the best putative signature.
At the same time the `K`-best algorithm find with more difficulty those variables, especially when the number of variables become greater.
Considering the distribution of single-variable scores, in fact, we could notice as the informative variables, despite they were manually introduced, were not always the top scoring ones: in large dimensional spaces also noisy-variables produced high(er) performances.

Using the same sample distributions for informative features, we manually introduced multiple couples in our dataset.
As expected the `DNetPRO` algorithm is not able to identify into a single connected component, and thus a single putative signature, the full set of informative variables, while the `K`-best algorithm easily find them in the top scoring ranking.
To guarantee the full set of informative features into the `DNetPRO` signature, we had to enlarge the number of nodes and thus we had to introduce multiple noisy-variables.
This highlights the limits of the `DNetPRO` algorithm and the need of a (optional) filtering procedure to face these critical cases[^1].


[^1]: In the algorithm description we discussed about the possibility of removing pendant nodes as optional filtering procedure.
  The case described above this step can help but not completely solve the problem: if there are two disjointed signatures we have to enlarge the number of nodes and create a connection between them, but this connection would be probably due to a noisy variable.
  The pendant node remotion can help to reduce the amount of nodes, but links which connect the two components would be preserved.

[**next >>**](../Implementation/README.md)
