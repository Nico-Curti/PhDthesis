## CHIMeRA

We have discussed about the information stored into the `CHIMeRA` database, but we have ignored how we could manage these data.
More than the realization of a useful database, we have to provide an easy-to-use interface to encourage the research community to manage our processed information.
We have already discussed about how the modern databases are shared along the Internet and how these large quantities of data could be managed using database languages (ref. [Dataset](./Dataset.md)).
Now we have to find the best solution for our application.

We developed a first database version of `CHIMeRA` using `SQL` (*Structured Query Language*) language [^1] and in particular the [`SQLite`](https://www.sqlite.org/index.html) one.
`SQLite` is probably the easier solution for database management and the creation of efficient queries is straightforward.
It is a well performing solution for standard relational databases but it does not provide any facility for network structure.
Moreover, `SQLite` database is not directly comparable to client/server `SQL` database engines such as `MySQL`, `Oracle`, `PostgreSQL` or `SQL Server` since it is designed only for local data storage and individual applications.
It is extremely efficient and simple in its applications but it does not cover the requirements pose by our `CHIMeRA` structure and our needs about sharing information.

![`NoSQL` Performance Benchmark 2018 (source [here](https://www.arangodb.com/2018/02/nosql-performance-benchmark-2018-mongodb-postgresql-orientdb-neo4j-arangodb/)). Absolute & normalize results for ArangoDBD, MongoDB, Neo4j and OrientDB. Comparison of time-performances using different (common) `NoSQL` queries.](../../../../img/arango_perf.svg)

A more efficient solution is provided by the modern graph databases (GDB).
GDB are databases which use graph structures to represent and store information: there are two needed information for the database given by nodes and edges.
They go under the `NoSQL` (*not SQL*, or better "*Not only SQL*") database category which storage data according to more sophisticated models than simple tabular relations (typical model of `SQL` databases)
GDBs allow simple and efficient retrieval of complex hierarchical structures by definition and thus they represent the most efficient solution for our `CHIMeRA` database which is born as a network-of-networks architecture.
Multiple different solutions have been proposed to address graph storages and there are a wide range of possible GDB languages publicly available on-line (e.g `Neo4j`, `OrientDB`, `Sparksee`, `AllegroGraph`, ...).
Based on our experience about these topics and driven by the available documentation, we have chosen to use [`ArangoDB`](https://www.arangodb.com/) in our application.
`ArangoDB` is an open-source and free software released on Github for multi-model database management with a unified query language `AQL` (*ArangoDB Query Language*).
`ArangoDB` database system is `NoSQL` but its queries are very closed to `SQL` ones and thus are easier to write also by no-expert users.
The core is written in `C++` and thus extremely efficient from a numerical point-of-view (ref. Fig.[1](../../../../img/arango_perf.svg)).
Moreover, it provides also a user-friendly web interface for network visualization and query development.
The possibility to have a web interface allows an easy way to share our database on Internet as service increasing the usability of our tool.
Moreover, the query outputs can be also downloaded and used by external tools.
Thus, using `ArangoDB` as service management we can provide a *Software as a Service* (SaaS) interface of our `CHIMeRA` database.
This project is still in work in progress and this SaaS is not yet publicly available [^2].

We re-formatted the `CHIMeRA` network following the `ArangoDB` requirements and we created the graph database structure of our data.
Using this database we were able to perform the first queries and discuss about the results.
The University of Bologna is currently involved into the [HARMONY European project](https://www.harmony-alliance.eu/) for the analysis of hematological data provided by multiple pharmaceutical companies.
The HARMONY project aims to describe, analyze and model multiple the data collected by the various partners producing a personalized medicine framework for the study of hematological diseases.
This project is based on the harmonization of different databases in the same way as our `CHIMeRA` project aims to merge multiple public data sources.
The main focus of the HARMONY project is about the diseases related to the different kinds of *leukemia*.
*Leukemia* is the most common type of cancer in children and it causes hundred of thousands of death every year.
It is a hematological disease and the exact causes of it is still unknown.
The developed `CHIMeRA` project could be used to contribute to this kind of researches giving a wider biological panoramic overview about these diseases.
Thus, we decided to formulate our first query about the *leukemia* disease.

We customized our query to extract only the 2nd neighbors related to this node.

```java
FOR x IN node_type_vertex
  FILTER x.name LIKE "looking_for_entry"
    FOR v, e, p IN 1..3 ANY x GRAPH "CHIMeRA"
      RETURN p
```

The query takes the node-collection (`ArangoDB` nomenclature) related to the searched node type (`node_type_vertex` in the code) and filter all the name which satisfy the `LIKE` condition.
Starting from the founded nodes it returns the output graph preview made by the 1st and 2nd neighbors (range of values `1..3` in the code).

We applied this kind of query for the *leukemia* node and we processed the results using `Gephi` as network viewer.
The obtained network is shown in Fig. [2](../../../../img/leukemia.png): the network involves 9460 nodes and 26646 links.
As can be seen by the plot, just considering the 2nd neighbors the obtained subnetwork is quite large and it highlights the biological complexity of this disease.

![Output of *leukemia* query obtained by `CHIMeRA` graph database using the previous pseudo code. The subnetwork is made by the 2nd neighbors starting from all the nodes which include "leukemia" in their names. The subnetwork includes 291 different types of leukemias clustered into 82 connected components. The giant components is made by 9108 nodes. `CHIMeRA` query is able to give a panoramic biomedical overview of the *leukemia* diseases mapping 838 diseases, 2463 genes, 5195 SNPs, 154 metabolite pathways, 40 metabolites and 5 drugs associated to them.](../../../../img/leukemia.png)

Using the "generic" name of *leukemia* we found 291 different types of leukemia diseases into the `CHIMeRA` network which denote the different facets of this disease.
Despite these multiplicities of results, we noticed that they clustered in only 82 connected components highlighting multiple similitudes between them.
In particular we found a giant components of 9108 nodes and only other 6 components with more than 10 nodes.
The giant component includes 165 different facets of *leukemia* disease while the other connected components describe the remaining ones.
The powerful of `CHIMeRA` network born exactly from these cases, in which we can infer missing information starting from the knowledge about analogous researches given by the full set of information related to the giant component found.
In the giant component we can appreciate a description of the *leukemia* disease given by all the other node types: we have, in fact, 587 diseases related to them, 4 drugs, 2409 genes, 40 metabolites, 154 metabolite pathways, 5195 possible phenotypes related to them a 719 SNPs.
The diseases associated to *leukemia* can help to highlight possible analogies between this "difficult" disease and "easier" ones (cause and related disease connections) or simply provide a bridge to other node types (e.g drugs or genes) which are not directly related to the *leukemia* using the databases individually.
We would stress that, despite the *phenotype* node-type which includes the more general biological information, all the other amount of node-types represent only a small percentage of the available information (disease 0.9%, drug 0.01%, gene 12.8%, metabolite 0.03%, pathway 11.5%, SNP 0.6%, phenotype 39.3%).
It is important to monitor also this kind of percentage because it could bring to possible biases in our description.
A such biomedical panoramic overview could not be found using a single-database approach and, to the best of the author's knowledge, only the `CHIMeRA` database is capable to map them.

The subnetwork extracted has more than half nodes as pendants (5270/9108 or 57%), i.e with degree score equal to `1`.
We have already discussed about this feature of our `CHIMeRA` network and in also in this case we can use this behavior to connect other (possible) kind of information to improve our disease description.
We are still working on the analyses of the extracted information and, especially, about their biomedical interpretation.
Moreover, we have to see how we can combine our data to the HARMONY project samples.
Thus, we conclude this chapter remarking the potential applications of such network-of-networks structure and its capability of give us a more global overview of biomedical compounds in scientific researches.


[^1]: `SQL` is a domain-specific language designed for managing data held in a relational database management system (RDBMS) and it is particularly efficient in handling structured data.

[^2]: As soon as possible we intend to create it jointly to an adequate computational environment ables to support multiple external queries.



[**next >>**](../../Conclusions.md)


