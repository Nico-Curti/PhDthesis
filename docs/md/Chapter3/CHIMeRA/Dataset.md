## CHIMeRA datasets

We have seen how we can extract useful informations also from unstructured databases using a web-scraping pipeline.
The *on-line doctor* web pages could be very useful for a toy model application like the `SymptomsNet` one [^1] but if we want produce scientific relevant results we have to take care about the validity of data.
Since the English datasets availability is easier than the Italian one we moved to more "robust" databases.

As told in the previous sections, there are a lot of studies performed on the disease associations to other biological compounds and in many cases the resulting datasets are public available on Internet.
This is the case of the [DisGeNET](https://doi.org/10.1093/nar/gkw943) or [DrugBank](https://doi.org/10.1093/nar/gkx1037) datasets which contain the relationship between a large number of diseases with genes/variants (SNPs) and drugs, respectively.
The DisGenet allows to download the datasets already stored into a well structured network format (sparse adjacency matrix, with 210498 associations between 117337 SNPs and 10358 diseases) while the DrugBank poses more issues to the treatment of data: the DrugBank database was designed to provide a large set of informations related to each drug inserted using its own website and thus it needs a huge pre-processing of the JSON dataset structure to highlight all the possible network associations (11926 drugs and 18969 drug-targets associations).
Using the DisGenet we can connect the diseases to their related genes and variants.
From the reviewed format of the DrugBank, instead, we can link each disease to the consequential drugs.
Associated to each drug we have also a list of gene and SNP targets which can be merged to the informations provided by DisGenet.
Moreover, we can also connect food treatments to each drug and take care to the interactions between drugs (their synergy or not).
We would stress that, despite the trivial overlaps between the same data sources (genes, diseases and SNPs up to now), just using the rearrangement of these pair of datasets into a network structure, we can already provide a possible extrapolation of the underlying informations using the paths between nodes.
Starting from a disease inside the DisGenet, using a single-database approach we can study the "causality" relationships with the connected genes.
Using a multiple-databases approach we can map that disease to other kind of informations like drugs or foods.
The aim of such a network-of-networks like structure is to unveil relationships hidden by the underwhelming overlap between single-type information across different databases.
The wide array of different informations merged can thus be exploited for applications such as wide-scale drug effect evaluation and design, addressing general diagnostic questions for systems medicine and diseases etiology expansion.
In other words, a network-of-networks structure allows the inference of missing connections using node contraction.

To enlarge our disease informations disease we looked for other on-line data sources.
A very interesting database is given by [HMDB](https://doi.org/10.1093/nar/gkx1089) (*Human Metabolite Data Bank*) which comprises a vast amount of metabolite and metabolite-pathway with the associated drugs and disease (114003 metabolite entries with chemical taxonomies and $$\sim$$25000 human metabolic and disease pathways).
The interconnection with the previous discussed datasets is straightforward but in this case the data are not public available but we had to apply a web-scraping algorithm to get its informations.
An analogous procedure was applied to extract the data included into the [RXList](https://www.rxlist.com/script/main/hp.asp) database.
RXList is an on-line website very similar to the previous discussed auto-diagnosis tools in which we can find associations between diseases and drugs and other several pathogenic associations.
In this case we have a further distinction between diseases: we have diseases related to drugs and diseases connected to other caused-diseases.
We can take care of this kind association using directional links [^2].

All these informations can enrich our database and the description of a given disease but we have to face on the problem of data merging.
As previously discussed we do not have a unique nomenclature for diseases and thus we can find analogous names (periphrases or synonyms) which identify the same concept (disease).
A useful tool to overcome these issues could be given by a synonym dictionary: a powerful example is given by the [CTD](https://doi.org/10.1093/nar/gky868) (*Comparative Toxicogenomics Database*) (7212 diseases with mapped synonyms and 4340 diseases with related phenotypes).
Using the CTD jointly with the [SNAP](http://snap.stanford.edu/biodata) (*Stanford Large Network Dataset Collection*, 8803 disease terms with related synonyms) database we could enlarge the number of synonyms associated to each disease name.

A full list of the informations collected by our web-scraping and rearrangement pipelines is shown in Fig. [1](../../../../img/Chimera_db_sources.png).

![Description of the data mined by the `CHIMeRA` project before merging. The datasets were collected using custom web-scraping pipelines and by a rearrangement of the public data.](../../../../img/Chimera_db_sources.png)

We remember that the crucial point of our merging procedure is given by the disease nodes since they are the node type shared along all the databases.
The help given by the synonym dictionaries certainly increase the overlap between the mined datasets but we chose to maximize it using a pre-processing NLP pipeline.
So, we started our pipeline using a word *standardization*, i.e converting all the words into their lower case formats and replacing all the punctuation characters with a unique one [^3].
Then, we noticed that a not negligible part of words involved into the disease names was useless for the description: words like "syndrome", "disease", "disorder", "deficiency", ... are not descriptive and so we can filter them.
Now, we could split the disease name into a series of token according to the list of words which compose it (*tokenization*) and sort them.

To further increase the overlap we cut the inflected words to their root form using a *stemming* algorithm: the stemmer strength has to be tuned according to the desired result.
A first processing was performed using a `Lancaster` stemmer (more aggressive).
If the resulting output was too short to be compared with other names the starting token was processed by a `Porter Snowball` stemmer (less aggressive).
The stemmer algorithm choice is a very crucial task for NLP because using it we drastically loose informations (it is not reversible).
Other processing steps were performed for critical cases encountered during the analyses: these steps constrain our pipeline and they tuned it for the underlying application.


The work-flow outputs include multiple false-positive matches: the pipeline performs a brute force processing and some informations lost along the steps could be significants.
In these cases we have multiple processed names belonging to different kind of diseases: an example is shown in Fig. [2](../../../../img/chimera_pipeline.png).
Considering the original name and the processed one (pipeline output) we merged two names using a score match.
This can be achieved introducing the standard word metrics: a common distance between words can be evaluated using the *Levenshtein Distance* which follows the equation

$$
d_{a, b}(i, j) = \left\{ \begin{array}{rc}
  \max(i, j)                                                       & \mbox{if   } \min(i, j) = 0 \\
  \mbox{min} \left\{ \begin{array}{r}
      d_{a, b}(i - 1, j) + 1                     \\
      d_{a, b}(i, j - 1) + 1                     \\
      d_{a, b}(i - 1, j - 1) + 1_{(a \neq b)}    \\
    \end{array}
    \right.                                                        & \mbox{otherwise}            \\

  \end{array}
  \right.
$$

where `a` and `b` are two strings of length `|a|` and `|b|` respectively.
The *indicator function* $$1_{(a \neq b)}$$ is equal to `0` when $$a_i = b_j$$ and `1` otherwise.
In this way the Levenshtein distance between `a` and `b` can be computed evaluating the distance between the first `i` characters of `a` and the first `j` characters of `b`.

Using the Levenshtein equation we evaluated the distance between the two original names and we associate the disease to the higher scorer.
A summary scheme of our pipeline is shown in Fig. [2](../../../../img/chimera_pipeline.png).

![Scheme of the NLP pipeline developed in the CHIMeRA project. The disease words are processed in multiple step as showed in the example.](../../../../img/chimera_pipeline.png)

The described NLP pipeline further increases the overlap between databases (e.g CTD-SNAP 24.17%; DisGenet-RXList 19.78%).
We manually supervised and checked the merging procedure taking care to reduce the false positive percentage.
In some cases the overlap percentage remained low also after the application of our pipeline (e.g. RXList-HMDB 8.03%; SNAP-HMDB 0.39%).
This behavior could be due to two factors: the first case is related to a deficiency of our pipeline in processing the contained names; in the second case it proved that we were working with complementary databases and thus the real information overlap should be reasonably low.
We took care of these cases and in our checks we always confirmed the second explanation.
This was a very encouraging results since it proved the efficiency of our pipeline and at the same time it confirmed that the union of multiple data sources could effectively enlarge our knowledge.

![Graphical rendering of the first version of the CHIMeRA network. The visualization was performed before the inclusion of the DrugBank dataset. For computational issues we have not performed newer image of the global structure. In the image we represented disease nodes (azure), gene nodes (orange), SNP nodes (purple), metabolite nodes (light green), drug nodes (pink) and phenotype nodes (dark green). The visualization was obtained by the *Atlas layout* provided by `Gephi`.](../../../../img/chimera_plot.png)


The output of our merging procedure allowed the realization of the `CHIMeRA` network, i.e a network with more than $$3.6\times10^5$$ nodes and more than $$3.8\times10^7$$ links (ref. Fig. [3](../../../../img/chimera_plot.png)).
In our resulting structure we have 7 node types: disease (63974), drug (35161), gene (18799), SNP (117337), metabolite (114100), phenotype (13214), metabolite-pathway (1329) and food (532).
The full network adjacency matrix is still a block matrix, i.e we have not all the combinations of information in our databases.
An emblematic case is given by the food nodes: we have food informations only into the DrugBank dataset and thus they would be connected only with drug types.
On the other hand our network architecture could be easily improved adding new data sources: the same food nodes are pendant nodes that could be easily connected to other kind of data introducing novel node types or just filling the available blocks.
`CHIMeRA` is still a work in progress project so we are still looking for improvements and new databases to add.


[^1]: Also because no other databases were provided for the Italian language!

[^2]: For sake of clarity, we encountered the same issue also into the DrugBank dataset in which we had intra-drug connections.

[^3]: An unexpected issue arise in this step: different databases use different enumeration system. In some entries we found disease names associated to numbers which identify their multiple types. An example could be "Polyendocrine Autoimmune Syndrome type 1" but at the same time in a second database the same disease could be represented by "polyendocrine autoimmune TYPE I". Despite the global differences between the two names, given in this case by upper- and lower-cases of some letters and the deletion of some words, a very critical odds is the enumeration style. The performances of our pipeline dramatically increased using a `roman_number_converter` algorithm.





[**next >>**](./CHIMeRA.md)

