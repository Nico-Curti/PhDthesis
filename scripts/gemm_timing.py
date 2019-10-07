#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from __future__ import print_function

import timeit

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'Gemm testing'

NUM_REPEATS = 10
NUMBER = 500

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
  import numpy as np

  N, M, K = (100, 200, 300)

  times_nn = gemm_nn(N, M, K)
  times_nt = gemm_nt(N, M, K)

  ref = np.asarray(times_nn)
  val = np.asarray(times_nt)

  times_nt = np.asarray(times_nt)/ref
  times_nn = np.asarray(times_nn)/ref

  times_nn = pd.DataFrame(data=times_nn, columns=['Times'])
  times_nn['Gemm'] = 'GEMM_NN'
  times_nt = pd.DataFrame(data=times_nt, columns=['Times'])
  times_nt['Gemm'] = 'GEMM_NT'

  data = pd.concat((times_nn, times_nt), axis=0)

  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))
  sns.despine(ax=ax, offset=1, top=True, right=True, bottom=False,  left=False)

  box = sns.barplot(x=data.index,
                    y='Times',
                    hue='Gemm',
                    data=data,
                    ax=ax,
                   )
  # add legend
  ax.legend(fontsize=24,
            loc='best',
            prop={'weight' : 'semibold',
                  'size':24},
            )
  ax.semilogy()

  for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)

  for tick in ax.yaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
  for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)

  # set axes labels
  ax.set_ylim(None, 1.3)
  ax.set_ylabel('SpeedUp', fontsize=24)
  ax.set_xlabel('Simulations', fontsize=24)

  fig.tight_layout()
  fig.savefig('../img/gemm.svg', bbox_inches='tight')

