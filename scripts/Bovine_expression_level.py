#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd

import pylab as plt
import seaborn as sns

__package__ = 'Bovine expression levels'
__author__  = ['Nico Curti']
__email__   = ['nico.curti2@unibo.it']


if __name__ == '__main__':

  filename = 'Bovini_ALL_cpm_log2_NonZero.txt'
  data = pd.read_csv(filename, sep='\t', header=0)
  label = [x.split('.')[0] for x in data.columns]
  data.columns = label


  signature_filename = 'Best_Signature_Net10.txt'
  signature = pd.read_csv(signature_filename, header=0)

  signature = data.loc[signature.ProbeId].values
  Nprobe, Nsample = signature.shape

  probe = ['RDM1', 'TRPV4', 'EPHX1', 'RIC8B', 'STAU1',
           'TLE1', 'IL5RA', 'ASB8', 'ERF', 'CDC40']

  points = ['o', 's', 'v']
  colors = ['k', 'r', 'g']
  size = 200
  str_label = set(label)

  fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(14, 8), sharex=True)
  fig.subplots_adjust(left=0.05, right=0.95, top=0.8,  bottom=0.1,
                      hspace=0.7)
  x = np.arange(0, Nsample)

  for ax, expr, name in zip(axes.ravel(), signature, probe):
    ax.set_title('{}'.format(name), fontsize=24, fontweight='normal')
    ax.scatter(x[ 0: 5], expr[ 0: 5], marker=points[0], s=size, edgecolors=colors[0], facecolors='none', linewidth=2)
    ax.scatter(x[ 5:10], expr[ 5:10], marker=points[1], s=size, edgecolors=colors[1], facecolors='none', linewidth=2)
    ax.scatter(x[10:15], expr[10:15], marker=points[2], s=size, edgecolors=colors[2], facecolors='none', linewidth=2)

    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_ticks(range(0, Nsample + 1, 5))

    sns.despine(ax=ax, offset=10, top=True, right=True, bottom=False, left=False)

  fig.text(0.5, 0.02,
           'Samples',
           horizontalalignment='center',
           size=24,
           #weigth='semibold',
           color='k')

  fig.text(0.03, 0.5,
           'Expression level',
           horizontalalignment='right',
           verticalalignment='center',
           size=24,
           rotation='vertical',
           #weigth='semibold',
           color='k')

  fig.text(0.0, 0.9, 'b',
           size=30,
           color='k',
           #weight='bold'
           )

  fig.legend(str_label, scatterpoints=1,
             fontsize=24, ncol=3)

  fig.savefig('../img/Bovine_expression_level.svg', bbox_inches='tight')

