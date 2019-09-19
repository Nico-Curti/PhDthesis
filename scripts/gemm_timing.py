#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from __future__ import print_function

import timeit

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'Gemm testing'

NUM_REPEATS = 500
NUMBER = 1000

def gemm_nn (N, M, K):

  SETUP_CODE = '''
import numpy as np
np.random.seed(123)

N, M, K = ({N}, {M}, {K})

a = np.random.uniform(low=0., high=1., size=(N, M))
b = np.random.uniform(low=0., high=1., size=(M, K))
  '''.format(**{'N' : N,
                'M' : M,
                'K' : K
                })

  TEST_CODE = '''
c = np.einsum('ij, jk -> ik', a, b, optimize=True)
  '''

  times = timeit.repeat(setup=SETUP_CODE,
                        stmt=TEST_CODE,
                        repeat=NUM_REPEATS,
                        number=NUMBER)
  return times


def gemm_nt (N, M, K):

  SETUP_CODE = '''
import numpy as np
np.random.seed(123)

N, M, K = ({N}, {M}, {K})

a = np.random.uniform(low=0., high=1., size=(N, M))
b = np.random.uniform(low=0., high=1., size=(M, K))
bt = b.T
  '''.format(**{'N' : N,
                'M' : M,
                'K' : K
                })

  TEST_CODE = '''
c = np.einsum('ij, kj -> ik', a, bt, optimize=True)
  '''

  times = timeit.repeat(setup=SETUP_CODE,
                        stmt=TEST_CODE,
                        repeat=NUM_REPEATS,
                        number=NUMBER)
  return times

if __name__ == '__main__':

  import seaborn as sns
  import pylab as plt
  import pandas as pd
  import matplotlib.patches as mpatches


  N, M, K = (100, 200, 300)

  times_nn = gemm_nn(N, M, K)
  times_nt = gemm_nt(N, M, K)

  times_nn = pd.DataFrame(data=times_nn, columns=['Times'])
  times_nn['Gemm'] = 'GEMM_NN'
  times_nt = pd.DataFrame(data=times_nt, columns=['Times'])
  times_nt['Gemm'] = 'GEMM_NT'

  ref = times_nn.Times.mean()

  data = pd.concat((times_nn, times_nt), axis=0)
  data.Times /= ref

  palette = sns.color_palette(['forestgreen', 'gold'])

  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
  sns.despine(ax=ax, offset=1, top=True, right=True, bottom=False,  left=False)

  box = sns.boxplot(x='Gemm',
                    y='Times',
                    #hue='Gemm',
                    palette=palette,
                    data=data,
                    ax=ax,
                    notch=True,
                    saturation=.75,
                    linewidth=3,
                   )
  for i,artist in enumerate(box.artists):
    line = box.lines[i*6 + 4]
    line.set_color('k')
    line.set_linewidth(5)

  labels = [ mpatches.Patch(facecolor='forestgreen', label='GEMM NN', edgecolor='k', linewidth=2),
             mpatches.Patch(facecolor='gold',        label='GEMM NT', edgecolor='k', linewidth=2)
           ]

  # add legend
  ax.legend(handles=labels,
            fontsize=24,
            loc='best',
            prop={'weight' : 'semibold',
                  'size':24},
            )

  for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)

  for tick in ax.yaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
  for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)

  # set axes labels
  ax.set_ylabel('SpeedUp', fontsize=24)
  ax.set_xlabel('Gemm Algorithm', fontsize=24)

  fig.tight_layout()
  fig.savefig('../img/gemm.svg', bbox_inches='tight')

