# Chapter 1
## Feature Selection - DNetPRO algorithm

After the end of the Human Genome Project (HGP, 2003) [[McKinney2012](https://doi.org/10.1108/09504121211211415)] there has been growing interest on biological data and their analysis.
At the same time, the availability of this type of data increased exponentially with the technological improvement of data extractors (High-Throughput technologies) [[Reuter2015](https://doi.org/10.1016/j.molcel.2015.05.004)] and with lower production costs.
Lower costs and efficiency in time extraction are the main factors that allow us to go into the new scientific era of Big Data.
Biological Big Data works with very large and complex datasets which are typically impossible to store, handle and analyze using standard computer and techniques [[Kumari2014](https://pdfs.semanticscholar.org/6cb1/5f5dc5605559230617828dc1dadad5775e85.pdf)].
Just think that we need around 140 Gb for the storage of the DNA of a single person and an Array
Express, a compendium of public gene expression data, contains more than 1.3 million of genomes which have been collected in more than 45000 experiments [[Greene2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5604462/)].
Since the number of available data is getting greater, we need to design several storage databases to organize, classify and moreover to extract informations from them.
The Bioinformatics European Institute (EBI) at Hinxton (UK), which is part of the European Laboratory of Biological Molecular and one of the biggest repositories of biological data, stores 20 petabytes of data and genomics and proteomics back-ups.
The amount of the genomics data is only 2 petabytes, and it doubles every year: it is not worth to remark that these quantities represent about a tenth of data stored by CERN of Ginevra [[Marx2013](https://doi.org/10.1038/498255a)].
On the other hand, the ability of processing data and the computational techniques of analysis do not grow the same way.
Therefore the gap between the great growth of the number of available data and our ability to work with them is getting bigger.

From a computational point of view, the Bioinformatics new-science is looking for new methods to analyze these large amount of data.
The common Machine Learning methods, i.e computational algorithms able to identify significant patterns into large quantities of data, needs to be optimized and modified to increase their computational and statistical performances.
To optimize the computational times we need to extend existing methods and algorithms and to develop new dimensionality reduction techniques.
In Machine Learning, in fact, as the dimensionality of the data increases, the amount of data required to
perform a reliable analysis grows exponentially[^1].
The dimensionality reduction techniques are methods able to identify the more significant variables of a given problem or a combination of them, where means that this smaller number of variables (or features) preserves the information about the problem as much as possible.
So this huge amount of high-dimensional omics data (e.g. transcriptomics through microarray or
NGS, epigenomics, SNP profiling, proteomics and metabolomics, but also metagenomics of gut microbiota) poses enormous challenges as how to extract useful information from them.
One of the prominent problems is to extract low-dimensional sets of variables - signatures - for
classification and diagnostic purposes, for example to better stratify patients for personalized intervention strategies based on their molecular profile [[Scotlandi2009](https://doi.org/10.1200/JCO.2008.19.2542), [Chan2011](https://doi.org/10.1146/annurev-genom-082410-101446), [Johnson2017](https://accpjournals.onlinelibrary.wiley.com/doi/abs/10.1002/phar.1975), [Beckmann2016ReconcilingEM](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5165712/)].


![An example in which single-parameter classification fails in predicting higher-dimension classification performance. Both parameters (*feature1* and *feature2*) badly classify in 1-D, but have a very good performance in 2D. Moreover, classification can be easily interpreted in terms of relative higher/lower expression of both probes.](https://raw.githubusercontent.com/Nico-Curti/PhDthesis/master/img/distributions.svg?token=AF4CJX7XWVY22FIIBN2U7VK5VYJNE&sanitize=true)

![Activity of a biological feature (e.g. a gene) as a function of its expression level: top) monotonically increasing, often also discretized to an on/off state; center, bottom) "windowed" behavior, in which there are two or more activity states that do not depend monotonically on expression level. X axis: expression level, Y axis, biological state (arbitrary scales).](https://raw.githubusercontent.com/Nico-Curti/PhDthesis/master/img/expression.svg?token=AF4CJXY7EMQ24VIPT2D6ATC5VYJ2K&sanitize=true)

Many approaches are used for these classification purposes [[Guyon2002](https://link.springer.com/article/10.1023/A:1012487302797)], such as Elastic Net [[Hughey2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4499117/)],
Support Vector Machine, K-nearest Neighbor, Neural networks and Random Forest [[Pang2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3495190/)].
Some methods select signature variables by means of single-variable scoring methods [[Eckhard2012](https://www.scirp.org/journal/PaperInformation.aspx?PaperID=18585), [Hocking1976](http://www.jstor.org/stable/2529336)]  (e.g. Student's t test for a
two-class comparison), while others search for projections in variable space, and then perform a dimensionality reduction by thresholding the projection weights, but these approaches could fail even in simple
two-dimensional situations (Fig. [1](../../../../img/distributions.svg)).

Methods that select variables for multi-dimensional signatures based on single-variable performance can have limits in predicting
higher-dimensional signature performance.
As shown in Fig. [1](../../../../img/distributions.svg)(a), in which both variables taken singularly perform poorly, but their performance becomes optimal in a 2-dimensional combination, in terms of linear separation of the two classes.

It is known that complex separation surfaces characterize classification tasks associated to image and speech recognition, for which Deep Networks are used successfully in recent times, but in many cases biological data, such as gene or protein expression, are more likely characterized by a up/down-regulation behavior (as shown in Fig. [1](../../../../img/expression.svg)(b) top), while more complex behaviors (e.g. a optimal range of activity, Fig. [1](../../../../img/expression.svg)(b) bottom) are much less likely.
Thus, discriminant-based methods (and logistic regression methods alike) can very likely provide good classification performances in these cases (as demonstrated by our results with DNetPRO) if applied in at least
two-dimensional spaces.
Moreover, the of these methods (that generate very simple class separation surfaces, i.e. linear or quadratic) guarantee that a of a signature based on lower-dimensional signatures is feasible.

This consideration are relevant in particular for microarray data where we face on a small number of samples compared to a huge amount of variables (gene probes).
This kind of problem, often called problem (where `N` is the number of features, i.e variables, and `S` is the number of samples), tend to be prone to overfitting[^2] and they are classified to ill-posed.
The difficulty on the feature extraction can also increase due to noisy variables that can drastically affect the machine learning algorithms.
Often is difficult to discriminate between noise and significant variables and even more as the number of variables rises.

In this thesis I propose a new method of features selection - DNetPRO, *Discriminant Analysis with Network PROcessing* - developed to outperform the mentioned above problems.
The method is particularly designed to gene-expression data analysis and it was tested against the most common feature selection techniques.
The method was already applied on gene-expression datasets but my work focused on the benchmark of it and on its optimization for Big Data applications.
The pipeline algorithm is made by many different steps and only a part of it was designed to biological application: this allow me to apply (part of) the same techniques also in different kind of problems with good results (see next sections).

[^1]: High dimensional data tends to become very sparse and as consequence it is hard to perform robust statistical evaluation on it. This phenomena is commonly called [[bellman1961adaptive](https://books.google.it/books?id=POAmAAAAMAAJ)].

[^2]: A solution to a problem is classified as if small fluctuations on the data variance produce classification errors. This problem arises when the model perfectly fit the training set but it is not able to generalize to new (test) samples.

[**next >>**](./DNetPRO/README.md)
