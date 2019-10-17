## The CHIMeRA project

The increasing availability of large-scale biomedical literature under the form of public on-line databases, has opened the door to a whole new understanding of multi-level associations between genomics, protein interactions and metabolic pathways for human diseases via network approaches.
Many structures and resources aiming at such type of analyses have been built, with the purpose of disentangling the complex relationships between various aspects of the human system relating to diseases [[SymtomsNet](https://www.nature.com/articles/ncomms5212), [HumanPhenotype](https://doi.org/10.1371/journal.pcbi.1000353)].
All these data come from different kind of studies performed by independent research groups who want to prove their theory about a particular aspect of biological agent interactions.
Modern biological analyses perform very capillary studies on biological agents: in this way we can easily study the deeper relationships between them but we completely ignoring what are around them.
This approach is certainly extremely efficient for the detection of the minimal causal agents of the problem but it tends to loose the global and complex [^1] environment and prospective in which the process occurs.
This is also the main problem of complex systems, i.e a system composed of multiple components with a mutual interactions between them.
The study of an individual aspect, in fact, could give us only a partial overview of the system but we have to take in account the interactions between the multiple components for a global description.

The network structures are acquiring even more importance on this kind of studies.
Complex System and System Biology researches have proposed multiple models about the dynamical and evolutionary interactions of the human system agents aiming to study the hidden relationships between them using network models.
A network model, in fact, is able to highlight and quantify the non-trivial correlations between the system components.
The main problem of this kind of approach is certainly the increasing dimensionality of the involved data: a network model could be described via its adjacency matrix, i.e a matrix `(N x N)` in which each row/column identifies an agent/node of the underlying problem and each entry `(i, j)` quantifies the importance of the interaction between the agent/node `i` and the agent/node `j`.
In real data applications we can often reasonably assume that a wide amount of the matrix entries are null, i.e the interaction between the involved agent is quite sparse, and thus we can used the important properties related to the sparse matrices to manage our network.
However, when the amount of data increase also the management of a such sparse matrix could be difficult.
More efficient solutions are provided by the modern Database formats and languages (e.g MySQL, SQLite, InfluxDB, ...) which store all these informations into a binary format and they allow to submit queries to extract the desired portion of data.
A global visualization of these huge amount of data is, in fact, without practical-sense and none valuable informations can be extracted from the global representation of the system.
The most important feature of network model is, in fact, the definition of a hierarchy of the interactions: the relationship between two nodes is given by the amount of connections which link them or, in other words, by their path.
Starting from a node its nearest neighbors are given by the set of nodes connected to it: re-iterating this concept we can explore all the network structure [^2].
In this way we can study the interactions of each node at different precision orders and causalities.

In light of these considerations we started to develop the CHIMeRA project (*Complex Human Interactions in MEdical Records and Atlases*) in which we aim to merge the state-of-art studies and databases about biomedical researches into a unified network structure.
A key role on our network structure is played by the diseases: the major part of biomedical researches are focused on causes and consequences of a given disease and thus the corresponding databases involve the interactions between them and other biological factors.
The diseases are also the most bigger manifestations of biological malfunctions and a large part of biological researches are financed on their study looking for their fine grain causes.
Thus a disease could be a valid "bridge" between multiple data sources: in each database we can find the associations between a disease and a series of multiple biological aspects related to it which can be merged together using disease nodes.

The crucial point of this project was, in fact, the merging of different kind of informations provided by multiple distinct data structured.
As told above, the major part of researches have focused on a partial aspect of the problem and they provide an independent result from the others, reducing the possibility of interactions between the outputs.
Moreover, a lot of time is always spent for the creation of a practical visualization of the results using web pages and on-line services which drastically affect the real usage of these informations when we want to combine multiple sources.
The CHIMeRA project started from these independent sources and it aims to maximize their overlap and thus the communications between them.

A final attention has to be payed about the format of these data: in physics we are friendly with numerical data but in these context we have to work with words.
The above told databases include only the research outputs and thus the performed interpretations of numerical data studied.
For example, if a numerically significant correlation was found between a disease and a gene we would found an association between them into a database and thus we can model it as a link.
The only information available into this database is a link between two words, the disease name and the gene name, without any numeric value.
While numbers have a unique representation (the number 2 is always 2) we can use multiple periphrases, i.e set of words, to identify the same concept.
The biomedical community, in fact, has not yet provided a unified standard for disease identification or, at least, it has not yet provided a rigid standard as for other kind of data as genes or SNPs.
So, if the diseases could be an efficient way to link together multiple data sources since all the studies prove correlations between them and other biomedical informations, they have the payback of an extreme variability in their nomenclature.
The CHIMeRA project tried to overcome this issue using a Natural Language Processing (NLP) approach.

In the next sections we will discuss about the multiple steps which bring us to the formulation of our unified CHIMeRA database.
We will start from the preliminary studies performed into the INFN FiloBlu project which allow the creation of the SymptomsNet structure, i.e a "small" network based on Italian words which connects diseases to related symptoms.
Then we will briefly introduce the most common NLP techniques, also used into the CHIMeRA pipeline and finally we will show the main developed features of CHIMeRA.

[^1]: From a physical point-of-view.

[^2]: We assume that our network structure has not isolated nodes and undirected connections.

[**next >>**](./SymptomsNet.md)