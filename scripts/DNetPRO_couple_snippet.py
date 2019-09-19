#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import LeaveOneOut, cross_val_score

import itertools
import multiprocessing

__package__ = 'Couples Evaluation'
__author__  = ['Nico Curti']
__email__   = ['nico.curti2@unibo.it']

def couple_evaluation (couple):
  f1, f2 = couple

  samples = data.iloc[[f1, f2]].values
  score = cross_val_score(GaussianNB(), samples.T, labels,
                          cv=LeaveOneOut(), n_jobs=1).mean()
  return (f1, f2, score * 100.)

def read_data (filename):

  data = pd.read_csv(filename, sep='\t', header=0)
  labels = data.columns.astype('float').astype('int')
  data.columns = [data.columns, labels]

  return (data, labels)

if __name__ == '__main__':

  from time import time as now

  start_time = now()

  filename = 'data.txt'

  global data, labels

  data, labels = read_data(filename)
  classes = set(labels)
  Nfeature, Nsample = data.shape

  print('Nfeature: {}\nNsample: {}\nNcombination: {}'.format(Nfeature, Nsample, Nfeature*(Nfeature-1)//2))

  couples = itertools.combinations(range(0, Nfeature), 2)

  nth = multiprocessing.cpu_count()

  with multiprocessing.Pool(nth) as pool:
    score = zip(*pool.map(couple_evaluation, couples))

  #score = [couple_evaluation(c) for c in couples]

  print('Couples evaluation: {:.3f}'.format(now() - start_time))

  print(score)