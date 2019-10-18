## mRNA data

We applied both training procedure (ref. Fig.[-1](../../../../img/dnet_pipe.pdf)) on the mRNA dataset.
The results are shown, as distribution of AUC (Area under the curve) score, in Fig.[1](../../../../img/mRNA_boxplot.png) (a) for the best signatures obtained with procedure `A` (corresponding to the validation approach used in [Yuan2014](https://www.nature.com/articles/nbt.2940)), while results with the full cross-validation procedure `B` are shown in Fig. [1](../../../../img/mRNA_tables.pdf) (b).

As expected, performances decrease with the introduction of the second cross validation step, but the values remain quite stable showing the robustness of the extracted signatures, and we remark that the validation procedure used in the reference paper by Yuan et al. resembles our approach without the second validation step.

![Results obtained by the DNetPRO algorithm pipeline on four mRNA tumor datasets, as from the Synapse database [Yuan2014](https://www.nature.com/articles/nbt.2940). Distributions of AUC values for the tumor datasets. Green boxplots: results using procedure `A` as described in Fig.[-1](../../../../img/dnet_pipe.pdf); yellow boxplots: results obtained using procedure `B`.](../../../../img/mRNA_boxplot.png)

![Comparison of DNetPRO results with the methods used in the paper of Yuan et al.: max AUC values obtained over the 10-Fold cross-validation procedure.](https://raw.githubusercontent.com/Nico-Curti/PhDthesis/master/img/mRNA_tables.svg?token=AF4CJX6PGROD5AJX4CSQXSK5WBJFG&sanitize=true)

All results are comparable (LUSC) or better (KIRC, GBM) than the results reported in [Yuan2014](https://www.nature.com/articles/nbt.2940), except for the OV dataset, also with the more conservative approach involving a further cross-validation step.
The size of the extracted signatures is quite constant, and smaller than 500 genes in each pipeline execution.

To test the robustness of our method, since each cross-validation procedure may generate different signatures, we measured the overlap of the genes belonging to each mRNA signature over 100 simulations with different training-test data splitting.
We observed an average overlap ranging from 40% to 60%, with a smaller group of genes found across all the 100 cross-validation iterations.

In this application the DNetPRO algorithm has several advantages: easy scalability on parallel architectures, simple signature interpretation allowing a valuable application in a biomedical context and a significant robustness in a highly noisy environment such as genomics measurements.

[**next >>**](./miRNA_RPPA.md)
