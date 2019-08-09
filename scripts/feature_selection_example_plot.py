#!/usr/bin/env python
# -*- coding: utf-8 -*-

import seaborn as sns
import numpy as np
import pandas as pd
import pylab as plt

sns.set_context('paper', font_scale=2)

__package__ = 'DNetPRO-FeatureSelection-problematic-example'

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

#------------------------ save figure
  graph_left.fig.savefig('../img/distributions.svg', bbox_inches='tight')
