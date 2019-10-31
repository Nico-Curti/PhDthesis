## Network signature

After the rearrangement of feature pairs in ascending order we can start to create the variable network and looking for its connected components as putative signatures.
Each feature represents a node in the network and a given pair is a connection between them (link).
Since the full storage of the network would require a matrix `(N x N)`, we have to chose a better strategy for the processing[^1].

The ordered set of couples computed in the previous section represents a so-called *COO sparse matrix* (Coordinate Format sparse matrix) and we can reasonable assume that the desired signature will be composed by the top ranking of them.
So, in the first step we cut a reasonable percentage of available pairs, focusing only on them.

Moreover, we are interested in a small set of variables unknown at prior.
Loading all the node pairs into the same graph can slow down the computation.
An iterative method (with stop criteria) can perform better and only in worst cases the full set of pair will be loaded.

Since the described algorithm step does not require particular performance efficiency, the main code used in our simulations was written in pure `Python`.
A `C++` implementation of the same algorithm was developed with the help of the Boost Graph Library [[BGL](http://www.boost.org/libs/graph/)], but to not overweight the code installation, it was reserved just for a style exercise.
In this section we discuss about this second version and also about the strategies chosen to implement an efficient version of it.
This version of the algorithm was also used, as stand alone method, for other applications that are discussed in the Appendix of this work.

BGL is a very wide framework for graph analyses based on `template` structures.
The library efficiency discourages users to re-implement the same algorithms and, for the current purpose, it was resulted more than sufficient.
Starting from the top scorer feature pairs, we progressively add each couple of nodes to an empty graph.
At each iteration step, the number of connected components is evaluated up to a desired number of nodes (greater or equal) is not reached[^2].
Two degrees of freedom are left to the user: in order, `pruning` and `merging`.
The first one performs an iteratively remotion of nodes with degree equal (or lower) than 1, i.e pendant nodes, until the graph core is not filtered.
The `merging` clause chooses between the biggest connected component, or the set of all the disjoint connect components, as putative signature.
The output of `merging` step determines the number of nodes in the graph which have to be considered by the stop criteria.

A crucial role in the algorithm optimization is played by the chosen of the BGL graph structure.
Since the two degrees of freedom imply a continuous rearrangement of the graph nodes, we have chosen to apply a filter mask over the main graph structure that highlights the only part of interest.
This can be done using the `boost :: filtered_graph` object of BGL.
In the following code the `C++` snippet is shown.


```c++
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/connected_components.hpp>
#include <boost/graph/filtered_graph.hpp>
#include <boost/function.hpp>
#include <boost/graph/iteration_macros.hpp>

typedef typename boost :: adjacency_list< boost :: vecS, boost :: vecS, boost :: undirectedS, boost :: property< boost :: vertex_color_t, int >, boost :: property < boost :: edge_index_t, int > > Graph;
using V = Graph :: vertex_descriptor;
using Filtered = boost :: filtered_graph < Graph, boost :: keep_all, boost :: function < bool(V) > >;


std :: vector < int > FeatureSelection (int ** couples, const int & min_size, bool pruning=true,  bool merging=true)
{
  Graph G;
  std :: set < V > removed_set;
  Filtered Signature (G, boost :: keep_all {}, [] (V v) {return removed_set.end() == removed_set.find(v);});

  int L = 0, leave, Ncomp, i = 0;

  while ( true ){

    boost :: add_edge (couples[i][0], couples[i][1], G);

    while ( pruning ){

      leave = 0;
      BGL_FORALL_VERTICES (v, Signature, Filtered);
        if ( boost :: in_degree (v, Signature) < 2 ){
          removed_set.insert (v);
          ++ leave;
        }

      if ( leave == 0 )
        break;
    }

    if ( num_vertices (G) - removed_set.size() ){

      components.resize (num_vertices (G));

      Ncomp = boost :: connected_components (Signature, &components[0]);

      if ( merging ){

        BGL_FORALL_VERTICES (v, Signature, Filtered)
          if ( boost :: in_degree(v, Signature) )
            core.push_back ( static_cast < int >(v) );
      }
      else {

        std :: map < int, int > size;
        for ( auto && comp : components ) ++ size[comp];

        auto max_key = std :: max_element (std :: begin(size), std :: end(size),
                                           [] (const decltype(size) :: value_type && p1, const decltype(size) :: value_type && p2)
                                           { return p1.second < p2.second; })->first;

        BGL_FORALL_VERTICES (v, Signature, Filtered)
          if ( components[v] == max_key )
            core.push_back( static_cast < int >(v) );
      }

      components.resize (0);
      L = static_cast < int >(core.size());
    }

    removed_set.clear();

    if ( L >= min_size ) break;

    ++ i;

    core.resize (0);
  }

  return core;
}
```

In the above description, it should be clear that, given any set of ordered (in ascending order) couples of variables, this algorithm allows to extract the core network, independently by the procedure which generate them.
So, it can be used as dimensionality reduction algorithm of general purpose network structures.
An example of this kind of application was reported in [Appendix B - Venice Road Network](../../Appendix/Venice/README.md) in which we summarized the results published in [[Mizzi2018](https://doi.org/10.1140/epjds/s13688-018-0168-2), [CurtiSDPS2018](https://www.sdpsnet.org/sdps/documents/sdps-2018/SDPS%202018%20proceedings%20ver%205.pdf)].


[^1]: We are working in the hypothesis of very large `N`.

[^2]: This procedure is quite similar to put a threshold value on the couple performances or just simpler highlight inside the full network the components linked by weights greater than a given value.


[**next >>**](./Python.md)
