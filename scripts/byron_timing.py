#!/usr/bin/env python

import pandas as pd
import seaborn as sns
import pylab as plt

__package__ = "Byron times plot"
__author__  = "Nico Curti (nico.curit2@unibo.it)"


if __name__ == '__main__':

  filename = 'byron_times.dat'
  data = pd.read_csv(filename, sep=',', header=0)
  n_version = len(data.Method.unique())

  ref = data[data.Method == 'darknet']['Time']
  ref = pd.concat([ref]*n_version).reset_index()
  ref = ref.Time

  data.Time /= ref


  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 8))
  fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

  sns.despine(ax=ax, offset=1, top=True, right=True, bottom=False,  left=False)

  bars = sns.barplot(x='Simulation',
                     y='Time',
                     hue='Method',
                     data=data,
                     ax=ax,
                     )
  for i, bar in enumerate(bars.patches):
    bar.set_edgecolor((0., 0., 0., 0.25))

  ax.set_ylabel('SpeedUp',   multialignment='center', fontsize=24,
                labelpad=20)
  ax.set_xlabel('Simulation', multialignment='center', fontsize=24,
                labelpad=20)

  for tick in ax.yaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
  for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)

  for tick in ax.xaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
  for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)

#  ax.semilogy()
  ax.legend(fontsize='x-large')

  ax.hlines(1, -n_version/2, n_version**2,
            linestyle='dashed', colors='k',
            lw=4, alpha=.25)
  ax.set_xlim(-.5, 4.5)

  #plt.show()
  fig.savefig('./byron_timing.svg', bbox_inches='tight')
