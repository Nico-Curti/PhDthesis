#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
import multiprocessing

from time import time as now

__package__ = 'Couples Evaluation'
__author__  = ['Nico Curti']
__email__   = ['nico.curti2@unibo.it']


def merge_argsort_parallel (arr, nth):

  N = np.size(arr)
  chunk = N // nth
  arr = np.reshape(arr, newshape=(-1, chunk))

  with multiprocessing.Pool(nth) as pool:
    idx = pool.map(np.argsort, arr)

  idx = np.asarray(idx)
  # merge sort


  return idx


if __name__ == '__main__':

  np.random.seed(123) # reproducibility

  N = 120000
  array = np.random.uniform(low=0., high=1., size=(N, ))
  idx = np.arange(0, N)

  nth = multiprocessing.cpu_count()

  start_time = now()

  np_idx = np.argsort(array, kind='quicksort')

  print('Sorting: {:.3f}'.format(now() - start_time))

#  start_time = now()
#
#  parallel_idx = merge_argsort_parallel(array, nth)
#
#  print('Sorting: {:.3f}'.format(now() - start_time))
#
#  assert np.allclose(np_idx, parallel_idx)
