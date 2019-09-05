#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import pylab as plt
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches # pretty labels

__package__ = 'DNetPRO TCGA pipeline - BoxPlot'
__author__  = ['Nico Curti']
__email__   = ['nico.curti2@unibo.it']

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']


def boxplot (dtype, letter, directories):
  '''
  '''

  sns.set_context('paper', font_scale=4)

  procedureA, procedureB = directories

  # load databases
  procedureA_db = pd.concat([pd.read_csv(procedureA + c + '_new_' + dtype + '.best',
                                         sep=',',
                                         usecols=['auc_validation', 'cancer', 'dtype'])
                             for c in cancer])
  procedureA_db['CV'] = ['1stcv']

  procedureB_db = pd.concat([pd.read_csv(procedureB + c + '_new_' + dtype + '.best',
                                         sep=',',
                                         usecols=['auc_validation', 'cancer', 'dtype'])
                            for c in cancer])
  procedureB_db['CV'] = ['2ndcv']

  # join together
  db = pd.concat([procedureA_db, procedureB_db])
  db['cancerCV'] = db['cancer'] + db['CV']

  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20,14))
  fig.subplots_adjust(left=0.15, right=0.9, top=0.8,  bottom=0.2)

  palette2 = sns.color_palette(['forestgreen', 'gold'])

  # simple boxplot
  box = sns.boxplot( x = 'cancer',
                     y = 'auc_validation',
                     hue = 'CV',
                     data = db,
                     palette = palette2,
                     ax=ax,
                     notch = True,
                     saturation = 1.,
                     linewidth=5,
                     )

  # add black line to median
  for i,artist in enumerate(box.artists):
    line = box.lines[i*6 + 4]
    line.set_color('k')
    line.set_linewidth(8)

  # set 0.5 horizontal line
  ax.hlines(.5, -0.5, len(cancer), colors='r', linestyle='dashed', alpha=.5, linewidth=8)
  # set axis limits
  ax.set_xlim(-.5, len(cancer)-.5)
  # set axes labels
  ax.set_ylabel('AUC (Area Under the Curve)', fontsize=40)
  ax.set_xlabel('Cancer', fontsize=40)

  # set cancer names as x ticks
  ax.set_xticklabels(cancer, rotation=0, fontsize=30, fontweight='bold')


  # Compute number of obs per group & median to position labels
  medians = db.groupby(['cancerCV'], sort=False)['auc_validation'].median().values
  mu = db.groupby(['cancerCV'], sort=False)['auc_validation'].mean().values
  mu_str = []
  pos = []
  for i in range(len(mu)//2):
    mu_str.append(r'$\boldsymbol{\mu_{A}}$: \textbf{:.2f}'.format(mu[i]) + '\n' + \
                  r'$\boldsymbol{\mu_{B}}$: \textbf{:.2f}'.format((mu[len(mu) // 2 + i]))
                    )
    pos.append(i)

  for i, tick in enumerate(pos):
    ax.text(tick, db.max()['auc_validation'] + 0.02,#1.01,#medians[tick] + 0.005,
            mu_str[i],
            horizontalalignment='center', size='medium', color='k')#, weight='semibold')

  # pretty labels
  labels = [ mpatches.Patch(facecolor='forestgreen', label='procedure A', edgecolor='k', linewidth=2),
             mpatches.Patch(facecolor='gold',        label='procedure B', edgecolor='k', linewidth=2)
           ]

  # add legend
  ax.legend(handles=labels,
            fontsize=40,
            loc='upper right',
            prop={'weight' : 'semibold',
                  'size':40}
            )

  # add letter for paper figure
  ax.text(-0.85, 0.755, letter, fontsize=60, color='k', weight='bold')

  # despine axis
  sns.despine(ax=ax, offset=10, top=True, right=True, bottom=False, left=False)

  fig.tight_layout()
  # save figure
  plt.savefig('../img/' + dtype + '_box_plot.svg', bbox_inches='tight')


if __name__ == '__main__':

  # letter for paper figure
  dtype = {'mRNA' : 'a',
           'miRNA': 'a',
           'RPPA' : 'c'
           }


