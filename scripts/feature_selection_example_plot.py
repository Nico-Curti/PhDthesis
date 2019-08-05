#!/usr/bin/env python
# -*- coding: utf-8 -*-

import seaborn as sns
import numpy as np
import pandas as pd
import pylab as plt
import matplotlib.lines as mlines

sns.set_context('paper', font_scale=2)

__package__ = 'DNetPRO-FeatureSelection-example'

__author__  = ['Nico Curti',
               'Enrico Giampieri',
               'Daniel Remondini'
               ]

__email__ = ['nico.curit2@unibo.it',
             'enrico.giampieri@unibo.it',
             'daniel.remondini@unibo.it'
             ]


if __name__ == '__main__':

  np.random.seed(123)

  # data left plot
  data_left = np.random.multivariate_normal(mean=[0, 0],
                                            cov=[(1.5,.002), (.002, 1.5)],
                                            size=500)

  nonlinear_left = np.random.multivariate_normal(mean=[5,-3],
                                                 cov=[(7.5,5.), (5., 5.5)],
                                                 size=500) @ np.asarray([[1,0],[0,-1]])

  df1_left = pd.DataFrame(data_left, columns=['x', 'y'])
  df2_left = pd.DataFrame(nonlinear_left, columns=['x', 'y'])
  del data_left
  del nonlinear_left

#  # data right plot
#
  data_right = np.concatenate([ np.concatenate([np.random.multivariate_normal(mean=[0, 0], cov=[(1.5,.002), (.002, 1.5)], size=100),
                                                np.random.multivariate_normal(mean=[6, 4], cov=[(1.5,.002), (.002, 1.5)], size=100)
                                                ]),
                                np.concatenate([np.random.multivariate_normal(mean=[0, 0], cov=[(1.5,.002), (.002, 1.5)], size=50),
                                                np.random.multivariate_normal(mean=[6, 6], cov=[(1.5,.002), (.002, 1.5)], size=100),
                                                np.random.multivariate_normal(mean=[10, 0], cov=[(1.5,.002), (.002, 1.5)], size=50)
                                                ])
                              ])

  types = np.concatenate([['\nmonotonically increasing']*200, ['\n"windowed" behavior\n(case 1)']*200 ])
  exp = np.concatenate([np.concatenate([['OFF']*100, ['ON']*100]),
                        np.concatenate([['OFF']*50,  ['ON']*100, ['OFF2']*50]),
                        ])

  data_right = pd.DataFrame( data_right, columns = ['expression level', 'biological state'])
  data_right['Gene expression'] = types
  data_right['expression'] = exp

  del types
  del exp

  func = pd.DataFrame(np.concatenate([1. / (1. + np.exp(-np.arange(-6, 6, .06))) *6,
                      np.concatenate([1. / (1. + np.exp(-np.arange(-6, 6, .12))), -1. / (1. + np.exp(-np.arange(-6, 6, .12)))+1])*6,
                      ]), columns=['expression\nlevel'])
  func['genes'] = np.concatenate([np.arange(0, 6, .03), np.arange(0, 10, .05) ])

  data_right = pd.concat([data_right, func], axis=1)

# plot
# ========================================
# ======================================== left

  graph_left = sns.jointplot(x=df1_left.x,
                             y=df1_left.y,
                             color=sns.xkcd_rgb['denim blue'],
                             stat_func=None,
                             edgecolor="k"
                             ).set_axis_labels('feature1', 'feature2')

  graph_left.x = df2_left.x
  graph_left.y = df2_left.y
  graph_left.plot_joint(plt.scatter, marker='D', edgecolor='k', c=sns.xkcd_rgb['pale red'], s=50)
  graph_left.plot_marginals(sns.distplot, kde=False, color=sns.xkcd_rgb['pale red'], axlabel=False)
  graph_left.ax_joint.set_xticks([])
  graph_left.ax_joint.set_yticks([])
  graph_left.ax_joint.text(-8, 12, 'a',
                           fontsize=30, color='k', weight='bold')


# ========================================= right

  graph_right = sns.FacetGrid(data_right,
                              row='Gene expression',
                              hue='expression',
                              size=4,
                              aspect=2,
                              hue_kws={'marker':['o', 'D', 'o']},
                              legend_out=False,
                              palette=[sns.xkcd_rgb['denim blue'],
                                       sns.xkcd_rgb['pale red'],
                                       sns.xkcd_rgb['denim blue']])

  graph_right = (graph_right.map(plt.scatter, 'expression level',
                                 'biological state',
                                 edgecolor='k'))
  graph_right = (graph_right.map(plt.plot, 'genes', 'expression\nlevel', lw=4, alpha=.5))
  graph_right.fig.subplots_adjust(left  = 0.1,
                                  bottom=0.1,
                                  right=0.85,
                                  top=0.9,
                                  wspace=0.3,
                                  hspace=0.6
                                  )

  blue_s = mlines.Line2D([], [], color=sns.xkcd_rgb['denim blue'], marker='o', linestyle='None',
                            markersize=10, label='OFF')
  red_s = mlines.Line2D([], [], color=sns.xkcd_rgb['pale red'], marker='D', linestyle='None',
                            markersize=10, label='ON')


  graph_right.axes[1][0].legend(handles=[blue_s, red_s],
                                bbox_to_anchor=(1.2, 1))
  graph_right.set_xticklabels([])
  graph_right.set_yticklabels([])
  graph_right.axes[1][0].get_xaxis().set_ticks([])
  graph_right.axes[0][0].text(-5, 12, 'b',
                              fontsize=30, color='k', weight='bold')


#------------------------ save figure
  graph_left.fig.savefig('../img/distributions.svg', bbox_inches='tight')
  graph_right.fig.savefig('../img/expression.svg', bbox_inches='tight')
