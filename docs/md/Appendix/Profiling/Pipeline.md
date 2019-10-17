## GATK-LODn pipeline

|                | **Coverage** | **No. of Reads** | **Read Lenght** | **BAM file size** | **NGS size** |
|:--------------:|:------------:|:----------------:|:---------------:|:-----------------:|:------------:|
|**Whole genome** | 37.7x       | 975,000,000      | 115             | 82 GB             | 104 GB       |
|**Whole genome** | 38.4x       | 3,200,000,000    | 36              | 138 GB            | 193 GB       |
|**Exome**        | 40x         | 110,000,000      | 75              | 5.7 GB            | 7.1 GB       |

The pipeline used in this work, GATK-LODn, has been developed in 2016 by Do Valle et al. [DoValle2016](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-1190-7), and codifies a new approach aimed to Single Nucleotype Polimorphism (SNP) identification in tumors from Whole Exome Sequencing data (WES).
WES is a type of "next generation sequencing" data [[Zwolak2008](https://arxiv.org/abs/0708.2724), [Behjati2013](http://ep.bmj.com/lookup/doi/10.1136/archdischild-2013-304340), [Shendure2008](http://www.nature.com/doifinder/10.1038/nbt1486)], focused on the part of the genome that actually codifies proteins (the exome).
Albeit known that non-transcriptional parts of the genome can affect the dynamic of gene expression, the majority of cancers inducing mutations are known to be on the exome, thus WES data allow to focus the computational effort on the most interesting part of the genome.
Being the exome in human approximately 1% of the total genome, this approach helps significantly in reducing the number of false positives detected by the pipeline.
The different sizes of next generation sequencing dataset are shown in Table.

The GATK-LODn pipeline is designed to combine results of two different SNP-calling softwares, GATK [McKenna2010](http://genome.cshlp.org/cgi/doi/10.1101/gr.107524.110) and MuTect [Cibulskis2013](http://www.nature.com/doifinder/10.1038/nbt.2514).
These two softwares employ different statistical approaches for the SNP calling: GATK examines the healthy tissue and the cancerous tissue independently, and identifies the suspect SNPs by comparing them; Mutect compares healthy and cancerous tissues at the same time and has a more strict threshold of selection.
In identifying more SNPs, GATK has a higher true positive calling than Mutect, but also an higher number of false positives.
On the other end Mutect has few false positives, but often does not recognize known SNPs.
The two programs also call different set of SNPs, even when the set size is similar.
The pipeline therefore uses a combination of the two sets of chosen SNPs to select a single one, averaging the strictness of Mutect with the recognition of known variants of GATK.

The pipeline work-flow includes a series of common steps in bioinformatics analysis and in the common bioinformatics pipelines.
It includes also a sufficient representative sample of tools for the performances statistical analysis.
In this way the results extracted from the single steps analysis could be easily generalized to other standard bioinformatics pipelines.

With the increasing demand of resources from ever-growing datasets, it is not favorable to focus on single server execution, and is better to distribute the computation over cluster of less powerful nodes.
The computational pipeline also has to manage a high number of subjects, and several steps of the analyses are not trivial to be done in a highly parallel way.
Thus, the importance of system statistics management as the efficiency usage of available resources are crucial to reach a compromise between computational execution time and energy cost.
For these reasons our main focus is on the performance evaluation of a single subject without using all the available resources, as these could be more efficiently allocated to concurrently execute several subjects at the same time.
Due to the nature of the employed algorithms, not all steps can exploit the available cores in a highly efficient way: some scales sub-linearly with the number of cores, some have resource access bottleneck.
Other tools are simply not implemented with parallelism in mind, often because they are the result of the effort of small teams that prefer to focus their attention on the scientific development side rather than the computational one.

Moreover in order to obtain an optimal execution of bioinformatics pipelines, each analysis step might need very different resources.
This means that any suboptimal component of a server could act as a bottleneck, requiring bleeding edge technology if all the steps are to be performed on a single machine.
Hybrid systems could be a possible solution to these issues, but designing them requires detailed information about how to partition the different steps of the pipeline.

[**next >>**](./Environment.md)
