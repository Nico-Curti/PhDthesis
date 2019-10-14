
## Synthetic dataset benchmark

Standard feature selection algorithms evaluate the single-variable performances.
Starting from the ranked variables according to their score, a signature is obtained selecting the top scorer ones according to an hard thresholding or by an iteratively add of variables until a desired output score is reached.
This method is called `K`-best algorithm and it allows to filter the number of variables without any constrain on their mutual interaction or correlation.
On the other hand, the proposed DNetPRO algorithm tries to extract the more statistically significant variables considering the interaction between them, i.e the combination of variable-pairs.
Thus, while the `K`-best algorithm scaled according to the number of variables, the DNetPRO algorithm is more computational expensive and its used can be justify only if its efficiency can be proofed.

We developed a toy model simulation to compare the performances of the standard `K`-best algorithm with the DNetPRO one, considering either the number of samples either the number of variables.
Since the DNetPRO algorithm was designed to gene expression dataset applications our toy model should consider a large number of variables with only a relative small number of samples.
To simulate a so like synthetic dataset we used the toy model generator provided by the [scikit-learn package](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html).
This model generator allows to set a precise number of classes and distinguish between *informative features*, i.e. features which easily separate the class populations, and \emph{redundant features}, i.e. features which represent noise in our problem.
The number of informative features should be realistically small compared to the noise, so in our simulations we chose to introduce a maximum of 1\% informative features in each simulation.

We randomly generated data from Gaussian distributions with an increasing number of samples and variables, i.e dimensions.
In each simulation we split the number of samples in training and test sets (Hold-Out method, with 2/3 of data as training and 1/3 as test) and we applied the DNetPRO algorithm.
From each simulation the extracted signatures were tested against the test set and the best performing one was kept.
On the same data we applied the `K`-best algorithm and we kept the same number of variables of the DNetPRO best signature, i.e `K` equal to the number of nodes in the DNetPRO best signature.
In this way we can compare the performances obtained on the test set by the two methods.
We would highlight that in general there is not a stop criteria on the `K`-best algorithm, so the number of variables selected could be smaller or greater than the number of DNetPRO signature nodes.
However we can reasonably assume that according to the `K`-best interpretation the selected features should be the most performing ones and adding more variables should introduce only small quantity of noise.
This justify the use of the same number of variables between the two algorithms using the DNetPRO signature as reference.
In Fig.2 we show the results obtained in our simulations: the results are obtained keeping fixed the number of variables/samples and varying the number of samples/variables, Fig.2(a) and Fig.2(b) respectively.

| <img src="../../../img/samples_toy.svg" width="400px;"/> | <img src="../../../img/features_toy.svg" width="400px;"/> |
| :----: | :----: |

For the same number of variables (Fig.2(a)) we can noticed as the two methods performs quite similarly but the DNetPRO is able to reach better performances as the number of samples increase.

This trend can be explained also in statistical terms: with small samples the variability of our (random) data is large and thus the performance distributions is more unstable.
With a greater number of samples the variances of our classes is reduced and also the statistical quantities involved in the computation of the discriminant curve can be evaluated with more accuracy.
As the number of samples increase the statistically evaluation of the variables becomes easier and increase the correspondence between the top scorer variables and the true-informative ones.
In low sample cases the quantity of noise is bigger and in an high dimensional space is harder to find the most informative directions and also noise variables could reach performances higher than informative ones.

Despite the simplicity of our toy model the DNetPRO is able to highlight its efficiency in terms of performances against the single-feature method.

A slight different behavior is shown varying the number of variables and keeping fixed the number of samples (Fig.2(b)).
In this case we have a median accuracy (black line in the plot) always higher for the DNetPRO algorithm.
With a small number of variables (left part of the plot) the `K`-best algorithm performances are more stable and only from a statistical point-of-view we can justify the efficiency of the DNetPRO algorithm (the median of the distribution is still higher compared to the `K`-best one).
As the number of variables increase also the efficiency of the DNetPRO algorithm increase until it exceeds the `K`-best algorithm (and its distribution is narrowed).
We reached this situation quite faster in our simulation since we constrained our toy model with a forced unbalance between number of samples and variables, i.e the so-called ill-posed problems.
The DNetPRO was designed to work in this situations and it is able to reach high accuracy results also in critical ill-posed problems.
The evaluation of pair of variables could be helpful to find good variables which are penalized in the single score ranking but which can demonstrate a good performance-interaction with other variables.
In this cases the DNetPRO results could be helpful also to understand the variable interactions due to the network structure of the signature that can bring to deeper considerations on the fine grain interaction of the variables in a real problem context.

This kind of toy model is considered a standard for feature extraction algorithm testing but it puts several disadvantages for the DNetPRO evaluation.
We started our discussion about the DNetPRO taking into account the two distributions of data shew in Fig.1(a).
The DNetPRO algorithm was designed to face on that kind of situations in the better way.
The limits of our algorithm are so bounded to the sample distributions: if the informative variables are totally independent one from each other the couples evaluation does not guaranteed the best approach to the problem.
An informative variable could work better with noise data than with another informative one: in this way we could expect a star-network signature in which the central node would be the informative variable connected to a series of noise variables.
Considering the signatures extracted by the DNetPRO algorithm we noticed this kind of behavior: the core of our signatures was principally composed by informative variables (which were manually introduced so easily traced).

We have to face on also the problem of multiple putative (disjointed) signatures: the DNetPRO algorithm takes into account only the connected components with the highest score as putative signature.
If the informative variables are disjointed the corresponding star-networks will be disjointed until a common noise-variable creates a bridge between the two connected components.
This means that we have to enlarge the quantity of nodes in our signature and thus increase the difficulty in the filtering of noise.

We evaluated both these situations in our toy model simulations.
In the first case we introduced only two informative variables obtained by a sampling of the distribution shew in Fig.1(a).
In all our simulations the DNetPRO algorithm was able to identify the couple of these variables as best putative signature.
At the same time the `K`-best algorithm find with more difficulty those variables, especially when the number of variables become greater.
Considering the distribution of single-variable scores, in fact, we could noticed as the informative variables, despite they are manually introduced, were not always the top scoring ones: in large dimensional spaces also noise-variables produced high(er) performances.

Using the same sample distributions for informative features, we manually introduced multiple couples in our dataset.
As expected the DNetPRO algorithm is not able to identify in a single connected components, and thus a single putative signature, the full set of informative variables, while the `K`-best algorithm easily find them in the top scoring ranking.
To guarantee the full set of informative features into the DNetPRO signature we had to enlarge the number of nodes and thus we had to introduce multiple noise-variables.
This highlights the limits of the DNetPRO algorithm and also the need of a (optional) filter procedure to apply to the putative signatures for these critical cases[^1].


[^1]: In the algorithm description we discussed about the possibility of removing pendant nodes as optional filter procedure.
  In the case described above this step can help but not completely solve the problems: if there are two disjointed signatures we have to enlarge the number of nodes until we create a connection between them but this connection would be probably due to a noise variable.
  The pendant nodes remotion can help to reduce the amount of node but the link which connects the two components would be preserved

[**next >>**](../Implementation/Intro.md)