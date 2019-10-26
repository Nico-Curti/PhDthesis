# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import networkx as nx
import pylab as plt
from collections import Counter

__package__ = "leukemia analysis"
__author__  = "Nico Curti"
__email__   = "nico.curit2@unibo.it"


type_size = {
              'disease': 63974,
              'drug': 35161,
              'gene': 18799,
              'snp': 117337,
              'metabolite': 114100,
              'phenotype': 13214,
              'pathway': 1329,
              'food': 532,
            }


if __name__ == '__main__':

  net = nx.read_gexf('leukemia_full.gexf') # 9460 nodes, 26646 edges

  graphs = list(nx.connected_component_subgraphs(net)) # 82 cc
  sizes = [len(g.nodes) for g in graphs]
  '''
  '9108,15,14,12,12,11,11,9,8,8,8,8,8,7,7,6,6,6,6,6,\
   6,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,3,3,3,3,3,\
   3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,\
   2,2,2,2,2,2,2,2,2,2,1,1'
  '''

  degree = net.degree()
  pendant = {k : v for k, v in degree if v <= 1} # 5270 nodes

  giant_pos = np.argmax([len(g.nodes) for g in graphs])
  giant = graphs[giant_pos]

  node_types = [v for _, v in nx.get_node_attributes(giant, 'type').items()]
  occ_types = Counter(node_types)
  '''
  'disease': 587,
  'drug': 4,
  'gene': 2409,
  'metabolite': 40,
  'pathway': 154,
  'phenotype': 5195,
  'snp': 719
  '''

  perc = {k: (v / type_size[k])*100 for k, v in occ_types.items()}
  '''
  'disease': 0.9175602588551599,
  'drug': 0.011376240721253662,
  'gene': 12.814511410181392,
  'metabolite': 0.035056967572304996,
  'pathway': 11.587659894657637,
  'phenotype': 39.31436355380657,
  'snp': 0.6127649420046533
  '''

  names = [v.lower() for _, v in nx.get_node_attributes(giant, 'name').items()]
  num_leukemias = sum([1 if 'leukemia' in n else 0 for n in names]) # 165

  deg = dict(giant.degree())
  names = dict(nx.get_node_attributes(giant, 'name'))
  deg = {names[k].lower() : v for k, v in deg.items()}

  y = sorted(deg.values(), reverse=True)
  pos = [(k, v) for k, v in deg.items()]
  pos = sorted(pos, key=lambda x : x[1], reverse=True)
  pos = [(i, v) for i, (yi, v) in enumerate(pos) if 'leukemia' in yi]

  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
  ax.plot(y, color='blue')
  ax.scatter(*zip(*pos), marker='o', facecolors='none', lw=2, color='red')
  ax.fill_between(np.arange(len(deg)), y, alpha=.5)



