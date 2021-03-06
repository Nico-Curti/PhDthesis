## The CHIMeRA project

The increasing availability of large-scale biomedical literature under the form of public on-line databases, has opened the door to a whole new understanding of multi-level associations between genomics, protein interactions and metabolic pathways for human diseases.
Many structures and resources aiming at such type of analyses have been built, with the purpose of disentangling the complex relationships between various aspects of the human system relating to diseases [[SymtomsNet](https://www.nature.com/articles/ncomms5212), [HumanPhenotype](https://doi.org/10.1371/journal.pcbi.1000353)].
Such structures, while allowing to study disease-to-some-other-omic associations, may not suffice when trying to bridge the gap of interpreting results and concept proofing clinical studies, when many types of data are involved.
Looking for causation of diseases across different omics has also become a major challenge, with the aim of expanding etiology and obtaining insights on pathogenesis [[Barabasi2007](https://www.ncbi.nlm.nih.gov/pubmed/17625512)].
This task may prove to be particularly hard when dealing with medical ontology strings coming from different sources.
Information of this type are usually provided by brief sentences and periphrases, while synonyms may occur to describe the same concepts thus causing different data source to provide different relationships for similar instances.
Text mining and string processing, thus becomes a required step when trying to exploit medical ontology as a bridge to diffuse information.

All these data come from different kind of studies performed by independent research groups who want to prove their theory about a particular aspect of biological agent interactions.
Modern biological analyses perform very capillary studies on biological compounds: in this way we can easily study the deeper relationships between them but we loose information about what there are around them.
This approach is extremely efficient for the detection of the minimal causal agents of a problem but it tends to loose the global and complex [^1] environment and prospective in which the process occurs.
This is also the main problem of complex systems, i.e a system composed of multiple components with a mutual interactions between them.
The study of an individual aspect, in fact, could give us only a partial overview of the system but we have to take into account the interactions between the multiple components for a global description.

The network structures are acquiring even more importance on this kind of studies.
Complex System and System Biology researches have proposed multiple models about the dynamical and evolutionary interactions of the human system agents aiming to study the hidden relationships between them using network models.
A network model, in fact, is able to highlight and quantify the non-trivial correlations between the system components.
The mathematical definition of network structures is given by the Graph Theory and we define them as a pair `G = (V, E)`, where `V` is a set of elements called nodes (or vertices) and `E` is the set of their pairwise associations (links or edges).
The total number of graph nodes (or cardinality of the graph) is denoted as `N` and it defines the order of the graph.
The graph dimension is given by the number of its edges (`m`).
We define a network as *complete graph* if it has all possible edges (`m = N x N`).
A network model could be described via its adjacency matrix, i.e a matrix `(N x N)` in which each row/column identifies a node of the underlying problem and each link $$e_{ij}$$ quantifies the importance of the interaction between the node $$v_i$$ and the node $$v_j$$.
We can define the importance of a node into the graph using the number of its connections: this is a classical *centrality measure* of a node and it is called the *degree* centrality.
Starting from these definitions we can enrich our model combining multiple network structure: given two graphs `G(V, E)` and `G'(V', E')` we define the combination of them as a new graph in which vertices are given by the intersection of $$V\cap V'$$ and edges given by $$E\cap E'$$.
If $$V\cap V'=\emptyset$$ the two graphs are *disjointed*; in contrary, if $$V'\subseteq V$$ and $$E'\subseteq E$$ then `G'` is a subgraph of `G`.
Combining multiple graphs together we obtain a network-of-networks structure able to map a wide range of interactions from multiple sets of elements.

In real data applications we can often reasonably assume that a wide amount of the matrix entries are null, i.e the interaction between the involved agents is quite sparse, and thus we can use the important properties related to the sparse matrices to manage our network.
However, when the amount of data increases also the management of a such sparse matrix could be difficult.
More efficient solutions are provided by the modern Database formats and languages (e.g `MySQL`, `SQLite`, `InfluxDB`, ...) which store all the information into a binary format and they allow to submit queries to extract the desired portion of data.
A global visualization of these huge amount of data is, in fact, without practical-sense and none valuable information can be extracted from the global representation of the system.
The most important feature of network model is, in fact, the definition of a hierarchy of the interactions: the relationship between two nodes is given by the amount of connections which link them or, in other words, by their paths.
Starting from a node, its nearest neighbors are given by the set of nodes connected to it: re-iterating this concept we can explore all the network structure [^2].
In this way we can study the interactions of each node at different precision orders and causalities.

In light of these considerations we started to develop the `CHIMeRA` project (*Complex Human Interactions in MEdical Records and Atlases*) in which we aim to merge the state-of-art studies and databases about biomedical researches into a unified network structure.
A key role on our network structure is played by the diseases: the major part of biomedical researches are focused on causes and consequences of a given disease and thus the corresponding databases involve the interactions between them and other biological factors.
The diseases are also the most bigger manifestations of biological malfunctions and a large part of biomedical researches are financed on their study looking for their fine grain causes.
Thus, a disease could be a valid "bridge" between multiple data sources: merging the disease nodes derived from different datasets we can provide a unique structure which host all the information.

The crucial point of this project was, in fact, the merging of different kind of information provided by multiple distinct data structured.
As told above, the major part of researches have focused on a partial aspect of the problem and they provide an independent result from the others, reducing the possibility of interactions between the outputs.
Moreover, a lot of time is always spent for the creation of a practical visualization of the results using web pages and on-line services which drastically affect the real usage of these information when we want to use them in scientific research.
The `CHIMeRA` project started from these independent sources and it aims to maximize their overlap and thus the communications between them.

We have to pay a final attention about the format of these data: in physics we are friendly with numerical data but in these context we have to work with words and text strings.
The above told databases include only the research outputs and thus the interpretations of the analyzed numerical data.
For example, if a numerical significant correlation was found between a disease and a gene we would find an association between them into a database (modeled as a link in our network).
The only information available into this database is a link between two words, the disease name and the gene name, without any numeric value.
While numbers have a unique representation (the number 42 is always 42) we can use multiple periphrases, i.e set of strings, to identify the same concept.
The biomedical community, in fact, has not yet provided a unified standard for disease identification or, at least, it has not yet provided a rigid standard as for other kind of data as genes or SNPs.
So, if the diseases could be an efficient way to link together multiple data sources since all the studies prove correlations between them and other biomedical information, they have the payback of an extreme variability in their nomenclature.
The `CHIMeRA` project tried to overcome this issue using a Natural Language Processing (NLP) approach.

In the next sections we are going to discuss about the multiple steps which bring us to the formulation of our unified `CHIMeRA` database.
We will start from the preliminary studies performed into the INFN FiloBlu project which allow the creation of the `SymptomsNet` structure, i.e a "smaller" network based on Italian words which connects diseases to related symptoms.
Then we will briefly introduce the most common NLP techniques, also used into the `CHIMeRA` pipeline and finally we will show the main developed features of `CHIMeRA` network.

[^1]: From a physical point-of-view.

[^2]: We assume that our network structure has not isolated nodes and it has only undirected connections.



[**next >>**](./SymptomsNet.md)
