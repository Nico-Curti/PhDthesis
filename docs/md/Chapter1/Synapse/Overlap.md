## Characterization of signature overlap

In the analysis of the Synapse dataset we used a complex pipeline of cross-validation (ref Fig. [-1](../../../../img/distributions.svg)) to obtain a sufficient statistics.
The DNetPRO algorithm was designed to work on a single dataset since the signature extraction can involve different variables for different data subdivisions.
In our application we divide the dataset into a training-test subdivision and the signature were extracted along a 10-fold cross-validation over the training set.
This kind of setup could produce 10 totally different signatures, in the worst case.
Moreover we replicated our simulation for 100 repetitions and thus a set of 1000 totally independent signatures were extracted.

Starting from this large subset of variables we can evaluate the robustness of the DNetPRO algorithm in the variable identifications studying the overlap between these signatures.
From a statistical point-of-view is quite unlikely that the same set of variables were included into all the extracted signatures, especially on this application, in which the variable roles are assumed by genes.
On the other hand the overlap of these signatures could highlight a statistical significance of some variables and thus genes related to the understudied tumors.

As case study we analyzed only the KIRC mRNA dataset in which the extracted signatures ranged from 4 to 650 genes ($$\mu=382$$ genes).
For each gene we counted its occurrences along the 1000 signatures.
The same analysis was performed taking into account the signatures generated using the `K`-best score variables (ref. [ToyModel](../DNetPRO/ToyModel.md) for further informations) and a random features extraction.
In Fig. [1](../../../../img/DNetPRO_overlap.svg) the genes distribution obtained by the three methods are shown.

![Signatures overlap obtained in the KIRC mRNA datasets. Genes occurrences of the 1000 DNetPRO signatures extracted from the Synapse pipeline (blue). Genes occurrences of the 1000 `K`-best variables extracted from the Synapse pipeline (red): the number of genes (`K`) is the same of the corresponding DNetPRO signature. Genes occurrences of 1000 random signatures (yellow).](https://raw.githubusercontent.com/Nico-Curti/PhDthesis/master/img/DNetPRO_overlap.svg?token=AF4CJX5CU2SS2OSA6BGV7IC5WBL3M&sanitize=true)

Both DNetPRO and `K`-best feature extraction algorithms identified a core set of genes common to the full set of signatures.
The `K`-best algorithm appears more stable than the DNetPRO algorithm and it is easier to find the same genes along the extracted signatures.
This behavior could be associated to the problems highlight also in the toy model simulations (ref.[ToyModel](../DNetPRO/ToyModel.md)): the DNetPRO algorithm is able to identify only one signature but the informative features (genes) could not co-operate in the same network-signature and thus they could be discarded.
The DNetPRO signatures are, in fact, very small compared to the number of variables and thus only small network components were extracted which are very closed to star-networks.
Despite the discrepancy between the signatures we have a core of 18 genes which occurs in at least the 95% of both signatures and 8 of them are in the 99% of both signatures.

The common genes were also mapped on public databases (TISIDB, [10.1093/bioinformatics/btz210](https://doi.org/10.1093/bioinformatics/btz210)) and [Oncotarget](), which link tumors to related genes.
We found 14/18 genes as informative probes for the KIRC tumor in the TISIDB and 7 of them were also found in the Oncotarget database [^1].
Taking into account the core set of 8 genes we found 3 of them on Oncotarget database and 7 of them on the TISIDB.
The only exception was given by the LOC388796 gene which was not found in any database.

The random feature extraction method is not even comparable with the others and it simply represents a null model.

[^1]: The list of genes in the TISIDB cover "only" 988 genes. From our list we have only one gene which was found in the Oncotarget database and not in the TISIDB. This gene misses in the TISIDB so we can not evaluate its importance.


[**next >>**](../Cytokinoma/README.md)
