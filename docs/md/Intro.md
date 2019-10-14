# Feature Selection - DNetPRO algorithm

After the end of the Human Genome Project (HGP, 2003) [@McKinney2012]
there has been growing interest on biological data and their analysis.
At the same time, the availability of this type of data increased
exponentially with the technological improvement of data extractors
(High-Throughput technologies) [@Reuter2015] and with lower production
costs. Lower costs and efficiency in time extraction are the main
factors that allow us to go into the new scientific era of Big Data.
Biological Big Data works with very large and complex datasets which are
typically impossible to store, handle and analyze using standard
computer and techniques [@Kumari2014]. Just think that we need around
140 Gb for the storage of the DNA of a single person and an Array
Express, a compendium of public gene expression data, contains more than
1.3 million of genomes which have been collected in more than 45000
experiments [@Greene2014]. Since the number of available data is getting
greater, we need to design several storage databases to organize,
classify and moreover to extract informations from them. The
Bioinformatics European Institute (EBI) at Hinxton (UK), which is part
of the European Laboratory of Biological Molecular and one of the
biggest repositories of biological data, stores 20 petabytes of data and
genomics and proteomics back-ups. The amount of the genomics data is
only 2 petabytes, and it doubles every year: it is not worth to remark
that these quantities represent about a tenth of data stored by CERN of
Ginevra [@Marx2013]. On the other hand, the ability of processing data
and the computational techniques of analysis do not grow the same way.
Therefore the gap between the great growth of the number of available
data and our ability to work with them is getting bigger.

From a computational point of view, the Bioinformatics new-science is
looking for new methods to analyze these large amount of data. The
common Machine Learning methods, i.e computational algorithms able to
identify significant patterns into large quantities of data, needs to be
optimized and modified to increase their computational and statistical
performances. To optimize the computational times we need to extend
existing methods and algorithms and to develop new dimensionality
reduction techniques. In Machine Learning, in fact, as the
dimensionality of the data increases, the amount of data required to
perform a reliable analysis grows exponentially[^1]. The dimensionality
reduction techniques are methods able to identify the more significant
variables of a given problem or a combination of them, where means that
this smaller number of variables (or features) preserves the information
about the problem as much as possible. So this huge amount of
high-dimensional omics data (e.g. transcriptomics through microarray or
NGS, epigenomics, SNP profiling, proteomics and metabolomics, but also
metagenomics of gut microbiota) poses enormous challenges as how to
extract useful information from them. One of the prominent problems is
to extract low-dimensional sets of variables -- signatures -- for
classification and diagnostic purposes, for example to better stratify
patients for personalized intervention strategies based on their
molecular
profile [@Scotlandi2009; @Chan2011; @Johnson2017; @Beckmann2016ReconcilingEM].

![Alt text](https://github.com/Nico-Curti/PhDthesis/blob/master/img/distributions.svg)
<img src="https://github.com/Nico-Curti/PhDthesis/blob/master/img/distributions.svg">
![Alt text](https://github.com/Nico-Curti/PhDthesis/blob/master/img/expression.svg)
<img src="https://github.com/Nico-Curti/PhDthesis/blob/master/img/expression.svg">

Many approaches are used for these classification purposes [@Guyon2002],
such as Elastic Net [@Hughey2015], Support Vector Machine, K-nearest
Neighbor, Neural networks and Random Forest [@Pang2012]. Some methods
select signature variables by means of single-variable scoring
methods [@Eckhard2012; @Hocking1976]  (e.g. Student's t test for a
two-class comparison), while others search for projections in variable
space, and then perform a dimensionality reduction by thresholding the
projection weights, but these approaches could fail even in simple
two-dimensional situations
(Fig. [\[fig:example\]](#fig:example){reference-type="ref"
reference="fig:example"}).

Methods that select variables for multi-dimensional signatures based on
single-variable performance can have limits in predicting
higher-dimensional signature performance. As shown in
Fig. [\[fig:example\]](#fig:example){reference-type="ref"
reference="fig:example"}(a), in which both variables taken singularly
perform poorly, but their performance becomes optimal in a 2-dimensional
combination, in terms of linear separation of the two classes.

It is known that complex separation surfaces characterize classification
tasks associated to image and speech recognition, for which Deep
Networks are used successfully in recent times, but in many cases
biological data, such as gene or protein expression, are more likely
characterized by a up/down-regulation behavior (as shown in
Fig. [\[fig:example\]](#fig:example){reference-type="ref"
reference="fig:example"}(b) top), while more complex behaviors (e.g. a
optimal range of activity,
Fig. [\[fig:example\]](#fig:example){reference-type="ref"
reference="fig:example"}(b) bottom) are much less likely. Thus,
discriminant-based methods (and logistic regression methods alike) can
very likely provide good classification performances in these cases (as
demonstrated by our results with DNetPRO) if applied in at least
two-dimensional spaces. Moreover, the of these methods (that generate
very simple class separation surfaces, i.e. linear or quadratic)
guarantee that a of a signature based on lower-dimensional signatures is
feasible.

This consideration are relevant in particular for microarray data where
we face on a small number of samples compared to a huge amount of
variables (gene probes). This kind of problem, often called problem
(where `N` is the number of features, i.e variables, and `S` is the
number of samples), tend to be prone to overfitting[^2] and they are
classified to ill-posed. The difficulty on the feature extraction can
also increase due to noisy variables that can drastically affect the
machine learning algorithms. Often is difficult to discriminate between
noise and significant variables and even more as the number of variables
rises.

In this thesis I propose a new method of features selection - DNetPRO,
*Discriminant Analysis with Network PROcessing* - developed to
outperform the mentioned above problems. The method is particularly
designed to gene-expression data analysis and it was tested against the
most common feature selection techniques. The method was already applied
on gene-expression datasets but my work focused on the benchmark of it
and on its optimization for Big Data applications. The pipeline
algorithm is made by many different steps and only a part of it was
designed to biological application: this allow me to apply (part of) the
same techniques also in different kind of problems with good results
(see next sections).

[^1]: High dimensional data tends to become very sparse and as
    consequence it is hard to perform robust statistical evaluation on
    it. This phenomena is commonly called  [@bellman1961adaptive].

[^2]: A solution to a problem is classified as if small fluctuations on
    the data variance produce classification errors. This problem arises
    when the model perfectly fit the training set but it is not able to
    generalize to new (test) samples.
