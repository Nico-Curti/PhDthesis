## DNetPRO algorithm

The `DNetPRO` algorithm produces multivariate signatures starting from all the couples of variables analyzed by a Discriminant Analysis.
For this reason, it can be classified as a combinatorial method and the computational time for the exploration of variable space is proportional to the square of the number of underlying variables (ranging from `10^3` to `10^5` in a typical high-throughput omics study).
This behavior allows to overcome some of the limits of single-feature selection methods and it provides a hard-thresholding approach compared to projection-based variable selection methods.
The combinatorial evaluation is the most time-expensive step of the algorithm and it needs an accurate algorithmic implementation for Big Data applications (see the next section for further information about the algorithm implementation strategy).
A summary of the algorithm is shown in the following pseudo-code.

```
Data matrix (N, S) -> List of putative signatures
  Divide the data into training and test by an Hold-Out method;
  For {couple <- (feature_1, feature_2) in Couples}{
    Leave-One-Out cross validation;
    Score estimation using a Classifier;
  }
  Sorting of the couples in ascending order according to their score;
  Threshold over the couples score (K-best couples);
  For {component in connected_components}{
    If {reduction}{
      Iteratively pendant node remotion;
    }
    Signature evaluation using a Classifier;
  }
```

So, given an initial dataset, with `S` *samples* (e.g. cells or patients) each one described by $N$ observations (our *variables*, e.g. gene or protein expression profiles), the signature identification can be summarized with the following steps:

- separation of available data into a training and test sets (e.g. 33/66, or 20/80);

- estimation of the classification performance on the training set of all `S(S-1)/2` variable couples through a computationally fast and reproducible cross-validation procedure (leave-one-out cross validation was chosen);

- selection of top-performing couples through a hard-thresholding procedure.
  The performance of each couple constitutes a *weighted link* of a network, where the nodes are the variables connected at least through one link;

- every *connected component* which composes the network identifies a putative signature.

- (optional) in order to reduce the size of an identified signature, the pendant nodes of the network (i.e. nodes with degree equal to one) can be removed, in a single step or recursively up to the core network (i.e. a network with all nodes with at least two links).

- all signatures are evaluated onto the test set to estimate their performances.

- a further cross validation step is performed (with a further dataset splitting into test and validation sets) to identify the best performing signature.

We would stress that this method is completely independent to the choose of the classification algorithm, but, from a biological point-of-view, a simple one is preferable to keep an easy interpretability of the results.
The geometrical simplicity of the resulting class-separation surfaces, in fact, allows an easier interpretation of the results, as compared to very powerful but black-box methods like nonlinear-kernel SVM or Neural Networks.
These are the reasons which lead us to use very simple classifier methods in our biological applications as diag-quadratic Discriminant Analysis or Quadratic Discriminant Analysis ([Appendix A](../../Appendix/DiscriminantAnalysis/README.md) for more information about the mathematical background and implementation in the different languages).
Both these methods allow fast computation and an easy interpretation of the results.
A linear separation might not be common in some classification problems (e.g. image classification), but it is very likely in biological systems, where many responses to perturbation consist in an increase or decrease of variable values (e.g. expression of genes or proteins, see Fig.[1](../../../../img/expression.svg)(b)).

A second direct gain by the couples evaluation is related to the network structure: the `DNetPRO` network signatures allow a hierarchical ranking of features according to their centrality compared to other methods.
The underlying network structure of the signature could suggests further methods to improve its dimensionality reduction based on network topological properties to fit real application needs, and it could help to evaluate the cooperation of variables for the class identification.

In the end, we remark that our signatures have a purely statistical relevance by being generated with a purpose of maximal classification performance, but sometimes the selected features (e.g. genes, DNA loci, metabolites) can be of clinical and biological interest, helping to improve knowledge on the mechanism associated to the studied phenomenon [[PMrna](https://genome.cshlp.org/content/early/2013/10/02/gr.155192.113.abstract), [Scotlandi2009](https://doi.org/10.1200/JCO.2008.19.2542), [PMgene](https://www.ncbi.nlm.nih.gov/pubmed/26297486), [Terragna](https://www.ncbi.nlm.nih.gov/pubmed/26575327)].


[**next >>**](./ToyModel.md)
