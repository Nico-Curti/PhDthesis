#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from __future__ import print_function

import os
import cv2
import pylab as plt
from matplotlib import gridspec

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'Upsampling/Downsampling example'


if __name__ == '__main__':

  filename = os.path.join(os.path.dirname(__file__), 'sample_img.jpg')
#                          '..', '..',
#                          'NumPyNet', 'data', 'dog.jpg')
  original = cv2.imread(filename)
  original = original[..., ::-1].astype('uint8')

  w, h, c = original.shape
  scale = 2

  dim = 40
  minh, minw = (120, 60)
  maxh, maxw = (minh + dim, minw + dim)

  dim2= 80
  minh2, minw2 = (20, 80)
  maxh2, maxw2 = (minh2 + dim2, minw2 + dim2)

  down_nearest = cv2.resize(original, dsize=(h//scale, w//scale),
                            interpolation=cv2.INTER_NEAREST)
  down_bicubic = cv2.resize(original, dsize=(h//scale, w//scale),
                            interpolation=cv2.INTER_CUBIC)
  down_lanczos = cv2.resize(original, dsize=(h//scale, w//scale),
                            interpolation=cv2.INTER_LANCZOS4)

  up_nearest = cv2.resize(original, dsize=None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_NEAREST)
  up_bicubic = cv2.resize(original, dsize=None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_CUBIC)
  up_lanczos = cv2.resize(original, dsize=None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_LANCZOS4)

  cv2.rectangle(original, pt1=(minw, minh), pt2=(maxw, maxh), color=(255, 0, 0), thickness=2)
  cv2.rectangle(original, pt1=(minw2, minh2), pt2=(maxw2, maxh2), color=(0, 0, 255), thickness=2)

  fig = plt.figure(figsize=(16, 10))
#  fig.suptitle('Up-Down sampling example\nScale factor: {:d}'.format(scale),
#               fontsize=26)

  outer = gridspec.GridSpec(1, 2, width_ratios=(.2, .5),
                            wspace=.05, hspace=0)

  left = gridspec.GridSpecFromSubplotSpec(1, 1,
                                          subplot_spec=outer[0],
                                          wspace=.1, hspace=.1)
  right = gridspec.GridSpecFromSubplotSpec(2, 3,
                                           subplot_spec=outer[1],
                                           wspace=.1, hspace=.1)


  minh2 /= scale
  maxh2 /= scale

  minw2 /= scale
  maxw2 /= scale

  minh2 = int(minh2)
  minw2 = int(minw2)
  maxh2 = int(maxh2)
  maxw2 = int(maxw2)

  axl = plt.Subplot(fig, left[0])
  axl.axis('off')
  axl.set_title('Original image', fontsize=24)
  axl.imshow(original)
  fig.add_subplot(axl)

  ax0 = plt.Subplot(fig, right[0])
  ax0.axis('off')
  ax0.set_title('Nearest', fontsize=24)
  ax0.imshow(down_nearest[minh2 : maxh2, minw2 : maxw2, :])
  fig.add_subplot(ax0)

  ax1 = plt.Subplot(fig, right[1])
  ax1.axis('off')
  ax1.set_title('Bicubic', fontsize=24)
  ax1.imshow(down_bicubic[minh2 : maxh2, minw2 : maxw2, :])
  fig.add_subplot(ax1)

  ax2 = plt.Subplot(fig, right[2])
  ax2.axis('off')
  ax2.set_title('Lanczos', fontsize=24)
  ax2.imshow(down_lanczos[minh2 : maxh2, minw2 : maxw2, :])
  fig.add_subplot(ax2)

  minh *= scale
  maxh *= scale

  minw *= scale
  maxw *= scale

  ax3 = plt.Subplot(fig, right[3])
  ax3.axis('off')
  ax3.imshow(up_nearest[minh : maxh, minw : maxw, :])
  fig.add_subplot(ax3)

  ax4 = plt.Subplot(fig, right[4])
  ax4.axis('off')
  ax4.imshow(up_bicubic[minh : maxh, minw : maxw, :])
  fig.add_subplot(ax4)

  ax5 = plt.Subplot(fig, right[5])
  ax5.axis('off')
  ax5.imshow(up_lanczos[minh : maxh, minw : maxw, :])
  fig.add_subplot(ax5)

  fig.savefig('../img/up_down_sampling.svg', bbox_inches='tight')


