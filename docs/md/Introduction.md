# Introduction

Big Data: these two words are at the heart of many contemporary researches.
Nevertheless, it is yet a loose term and no exhaustive description has been provided.
We commonly associate this term to the description of data generated from several machines and used to describe very complex systems.
We can find Big Data associated to multiple kind of modern research which use this term to highlight the complexity of their projects.
The use of Big Data, in fact, is closely related to the Complexity term (intended with its physical meaning) and to the major part of Artificial Intelligence researches since they seem to be the only way to overcome these problems.
As anticipated, it is difficult to find a satisfactory definition about Big Data and the common sense tends to name them as simply a vast amount of data.
However, this is just a broadly description of them and it simplifies too much their usage and power.
We can find Big Data in more applications and fields than we usually think and a prominent research field is the Biomedical one.

Biomedical data are growing both in size and breath of possible uses.
This growth is driven by the development of newer and cheaper technologies for the acquisition of data which enlarge the availability of them.
At the same time, also the computational power is increasing and we can take advantage of more efficient and complex algorithms and pipelines for the analysis of a such amount of data.
Unfortunately, this second growth is not enough fast to tackle these problems and the development of novel techniques of processing and, moreover, algorithms able to extract informative portions of data is essential in the so-called Big Data Analytics.
This is even more true when we talk about Biomedical Big Data and thus data related to health-care studies which aim to identify the variable responsible for more or less complex diseases or to give a description of the more complex biological processes.
In addition to the novel *Next Generation Sequencing* (NGS) technologies related to the analysis of biological structures like DNA and RNA, the so-called *omics* researches involve a large part of contemporary biomedical researches.
The term *omic* data, also in this case, refers to the wide range of biological studies ending in -omics, like *genomics*, *proteomics* or *metabolomics* which aim to describe and quantify biological processes at different scale levels.
The analysis of these kinds of data poses many challenges to the research community, especially for the vast amount of variables involved.
In general biological research field is used to analyze only few samples compared to the number of variables involved: this is exactly the opposite behavior of common statistical analyses and, moreover, of physics research.
The ability to extract information and reduce the problem dimensionality is crucial to address these problems.

More complex analyses related to high dimensional problems are the image processing ones.
Biomedical imaging is another of the most prominent kind of analysis for the development of novel medical treatments.
The many differences between acquisition methods and data structures/characteristics for different imaging modalities create a zoo of possible studies and analyses.
At the same time, the dimensionality of the involved images requires an adequate computational effort.
These characteristics satisfy all the requirements posed by the modern deep learning training.
It is not always possible to create an appropriate mathematical model to describe the underlying dataset and in many cases we need to handle more general applications.
Standard machine learning methods can not keep up such requirements and they are giving way to deep learning models.
In many applications these models are used as black-boxes and their complexity does not always allow a complete understanding about their learning.
Nevertheless, their efficiency is overcoming standard methods in a vast amount of applications and they are the only tools which give the semblance of an artificial intelligence.

All these data and analyses involve multiple scientific researches which, driven by them, are becoming more accurate but, at the same time, also more specialized.
With a such heterogeneity of data, we can handle very useful analyses of any biological compound with a payback of a loss about the system complexity and interactions.
The absence of a standardized system for sharing biomedical information contributes to the difficulty about merging results provided by different studies.
Several European projects about health-care research has been financed aiming to develop an harmonization between biomedical data sources.
The principal issues about this topic are related to a non rigid nomenclature of medical keywords and data formats.
Relational databases have efficiently driven Big Data research up to now, but the increasing demand of non-trivial connections between different kind of entries is paving the way to different kind of approaches and data management.
At the same time, also the research about novel natural language processing methods are becoming very popular in these applications.

This work of thesis started from these multiple issues about Big Data and it focused on different Biomedical topics.
In each chapter we are going to handle a different aspect of Big Data research and a different kind of data.
For each topic we offer a balanced description between the mathematical/theoretical background and numerical issues/solutions of it.
The main focus of each application remains its algorithmic description and the numerical solutions developed to handle the underlying problem.

We start our trip across Biomedical Big Data introducing a novel feature selection algorithm.
The proposed algorithm is tailored for gene expression analyses and in the various sections of the first chapter we provide a description of all its pros and cons.
The algorithm was already used in earlier scientific publications but, for the first time, a deeper analysis of all its characteristics either from a numerical either from a algorithmic point-of-views is provided.
The algorithm has also undergone an intensive optimization procedure to make it able to handle Big Data problems in a reasonable computational time.
We test our method against a custom toy model and later we compare its efficiency against state-of-art equivalent models and data.
We also show some applications of it to different kind of data, starting from gene expression datasets, passing to protein expression levels up to other type of non-biological data, proving its efficiency in all these topics.
Within the limits of our knowledge about biological processes, we provide also an interpretation about the obtained results where it is possible.

Then, we move to more numerical expensive analyses with the help of modern deep learning models.
Starting from a brief introduction about neural network models we look at the different functions/layers included in the later discussed models.
For each of them we give a theoretical explanation about the mathematical functions and, also in this case, we deeply focus on their numerical implementation.
Three custom libraries are introduced, developed by the author of the thesis, showing the results obtained by them with other state-of-art implementations.
We use deep learning neural network models to handle different kind of image processing analyses with a particular attention to biomedical images.
As previously discussed, there are multiple image sources in the biomedical field and in our applications we use NMR and CT images.
Implementing the most recent Super Resolution algorithms we show their application on NMR images, proving how they can help to increase image quality and how they can be also used to improve object detection tasks.
Other kinds of applications are also shown to prove the versatility of such methods in several biomedical tasks.

We end our discussion introducing a novel database, related to common diseases, their symptoms and other biomolecular entities, obtained by the harmonization of publicly available datasets.
A global description about Big Data sources and how we can handle problems related to the data extraction is discussed before our pipeline of processing.
A key role in our work is played by natural language processing methods and, thus, starting from a brief introduction about them we focus on the developed pipeline.
The work concerned the merging of multiple datasets into a unique network structure able to manage the interactions between different biomedical compounds.
The network-of-networks structure generated during this project allows a wider overview of several diseases pointing out their association to genes, drugs and other biological data.
We also discuss about how this large amount of information can be managed using modern database languages and about the chosen strategy to share our results to the scientific community.

For sake of brevity, not all the developed projects are discussed and some of the remaining ones are bounded in the Appendix of this text.
However, the principal contributions of this work are related to the developed codes.
All the code described in this work are, in fact, publicly available on-line on [Github](https://github.com/Nico-Curti/).
We have paid special attention to the development of our codes, carefully managing their testing and availability.
Each code has been enriched by an adequate on-line documentation either about its usage either about its installation and performances.
A small part of the codes has been written in pure-`Python` while the major part has been written in `C++`: for this reason a continuous integration of them is essential to ensure their usability.
We remark that also the current text is publicly available on [Github](https://github.com/Nico-Curti/PhDthesis) as `Latex` code.

[**next >>**](./Chapter1/README.md)
