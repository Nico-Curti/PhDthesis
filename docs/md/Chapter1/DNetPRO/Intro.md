## DNetPRO algorithm

The DNetPRO algorithm generates multivariate signatures starting from
all couples of variables tested with Discriminant Analysis. For this
reason it can be classified as a combinatorial method and the
computational time for variable space exploration is proportional to the
square of the number of available variables (ranging from `10^3` to
`10^5` in a typical high-throughput omics study). This behavior allows
it to overcome some of the limits of single-feature selection methods,
and provides a hard-thresholding approach at difference with
projection-based variable selection methods. Certainly the combination
evaluation is the most time expensive step of the algorithm and it needs
accurate algorithmic implementation for Big Data applications (see the
next section for further informations about the algorithm implementation
strategy). The algorithm can be summarize as shown
in [pseudo-code](#code:DNetPRO).

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


Divide the data into training and test by an Hold-Out method Sorting of
the couples in ascending order according to their score Threshold over
the couples score (`K`best couples)

So, given an initial dataset, consisting in `S` *samples* (e.g. cells or
patients) with `N` observations each (our *variables*, e.g. gene or
protein expression profiles), the signature identification procedure can
be summarized with the following pipeline:

-   separation of available data into a training and a test set (e.g.
    33/66, or 20/80);

-   estimation of the classification performance on the training set of
    all `S(S-1)/2` variable couples through a computationally fast and
    reproducible cross-validation procedure (leave-one-out cross
    validation was chosen);

-   selection of top-performing couples through a hard-thresholding
    procedure. The performance of each couple constitutes a *weighted
    link* of a network in which nodes are the variables connected at
    least through one link;

-   every *connected component* in which the network is divided into
    constitutes an identified classification signature.

-   (optional) in order to reduce the size of an identified signature,
    the pendant nodes of the network (i.e. nodes with degree equal to
    one) can be removed, in a single step or recursively until the core
    network (i.e. a network with all nodes with at least two links) is
    reached.

-   all signatures are applied onto the test set to estimate their
    performance.

-   a further cross validation step is performed (with a further dataset
    splitting into test and validation sets) to identify the best
    performing signature.

I would stress that this method is completely independent to the chose
of the classification algorithm but from a biological point of view a
simple one is preferred to preserve an easy interpretability of the
results. The geometrical simplicity of the resulting class-separation
surfaces, in fact, allows an easier interpretation of the results, as
compared with very powerful but black-box methods like nonlinear-kernel
SVM or Neural Networks. Moreover the network interaction of variables
can keep an internal ranking score of features importance or possible
features cooperation. These are the reasons that move us to use very
simple classifier methods in our biological application as
diag-quadratic Discriminant Analysis or Quadratic Discriminant Analysis
(Appendix A for more informations about the mathematical background and
implementation in the different languages). Both these methods allow
fast computation and easy interpretation of the results. This linear
separation might not be common in some classification problems (e.g.
image classification) but it is very plausible in biological systems, in
which many responses to perturbation consist in increase or decrease of
variable values (e.g. expression of genes or proteins, see
Fig. [1](#fig:example)(b)).

In a general classification problem (e.g. image analysis) this could not
be the case, since complex non linear separating surfaces may exist
among the classes, but we hypothesize (and our results seem to confirm
so) that in classification problems based on biological data such as
gene expression these situations are not so common. This assumption is
very plausible for biological data, since genes are in general up- or
down-regulated in order to modify their activity, and protein and
metabolites most of the times respond consequently.

A second direct gain by the couples evaluation is related to the network
structure: the DNetPRO network signatures allow a hierarchical ranking
of the features according to their centrality compared to possible Kbest
signatures. This underlying network structure of the signature could
suggest further methods for signature dimensionality reduction based on
network topological properties to fit real application needs and it
could help to evaluate the cooperation of the variables for the class
identification.

In the end we remark that the discriminating signatures have a purely
statistical relevance, being generated with a purpose of maximal
classification performance, but sometimes the selected features (e.g.
genes, DNA loci, metabolites) can be of clinical and biological
interest, helping to improve knowledge on the mechanism associated to
the studied phenomenon [[PMrna](https://genome.cshlp.org/content/early/2013/10/02/gr.155192.113.abstract),
[Scotlandi2009](https://doi.org/10.1200/JCO.2008.19.2542),
[PMgene](https://www.ncbi.nlm.nih.gov/pubmed/26297486),
[Terragna](https://www.ncbi.nlm.nih.gov/pubmed/26575327)].


[**next >>**](./ToyModel.md)