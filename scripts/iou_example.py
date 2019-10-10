#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from __future__ import print_function

import pylab as plt
import numpy as np
import cv2

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'IoU score example'


if __name__ == '__main__':

  img1 = np.full(shape=(51, 51, 3), fill_value=255, dtype=np.uint8)

  x1, x2 = (2, 30)
  y1, y2 = (2, 30)

  cv2.rectangle(img=img1, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=1)

  x1, x2 = (6, 50)
  y1, y2 = (6, 50)

  cv2.rectangle(img=img1, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=1)

  union = (50-2)*(50-2)
  intersection = (30-6)*(30-6)
  iou1 = intersection/union


  img2 = np.full(shape=(51, 51, 3), fill_value=255, dtype=np.uint8)

  x1, x2 = (2, 40)
  y1, y2 = (2, 40)

  cv2.rectangle(img=img2, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=1)

  x1, x2 = (6, 50)
  y1, y2 = (6, 50)

  cv2.rectangle(img=img2, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=1)

  union = (50-2)*(50-2)
  intersection = (40-6)*(40-6)
  iou2 = intersection/union



  img3 = np.full(shape=(51, 51, 3), fill_value=255, dtype=np.uint8)

  x1, x2 = (2, 48)
  y1, y2 = (2, 48)

  cv2.rectangle(img=img3, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=1)

  x1, x2 = (4, 50)
  y1, y2 = (4, 50)

  cv2.rectangle(img=img3, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=1)

  union = (50-2)*(50-2)
  intersection = (48-4)*(48-4)
  iou3 = intersection/union


  fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(16, 8))

  ax1.imshow(img1)
  ax1.set_title('IoU: {:.3f}'.format(iou1), fontsize=24)
  ax1.axis('off')
  ax1.set_xlabel('Poor', fontsize=24)

  ax2.imshow(img2)
  ax2.set_title('IoU: {:.3f}'.format(iou2), fontsize=24)
  ax2.axis('off')
  ax2.set_xlabel('Good', fontsize=24)

  ax3.imshow(img3)
  ax3.set_title('IoU: {:.3f}'.format(iou3), fontsize=24)
  ax3.axis('off')
  ax3.set_xlabel('Excellent', fontsize=24)


  fig.savefig('../img/iou_example.svg', bbox_inches='tight')
