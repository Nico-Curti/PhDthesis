#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from __future__ import print_function

import os
import cv2

import tensorflow as tf
from skimage.measure import compare_ssim

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'Upsampling/Downsampling example'


def compute_score(raw_img, sr_img):
  scale = 4
  boundary = 6 + scale
  ssim = compare_ssim(raw_img[boundary : -boundary, boundary : -boundary, :],
                      sr_img[boundary : -boundary, boundary : -boundary, :],
                      data_range=255, multichannel=True)
  with tf.Session().as_default():
    psnr = tf.image.psnr(raw_img, sr_img, max_val=255).eval()
  return psnr, ssim


if __name__ == '__main__':

  filename = os.path.join(os.path.dirname(__file__), 'sample_img.jpg')
#                          '..', '..',
#                          'NumPyNet', 'data', 'dog.jpg')
  original = cv2.imread(filename)
  original = original[1:, :, ::-1].astype('uint8')

  w, h, c = original.shape
  scale = 2

  down_lanczos = cv2.resize(original, dsize=(h//scale, w//scale),
                            interpolation=cv2.INTER_CUBIC)

  up_nearest = cv2.resize(down_lanczos, dsize=None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_NEAREST)
  up_bicubic = cv2.resize(down_lanczos, dsize=None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_CUBIC)
  up_lanczos = cv2.resize(down_lanczos, dsize=None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_LANCZOS4)

  up_nearest_psnr, up_nearest_ssim = compute_score(original, up_nearest)
  up_bicubic_psnr, up_bicubic_ssim = compute_score(original, up_bicubic)
  up_lanczos_psnr, up_lanczos_ssim = compute_score(original, up_lanczos)

  print('Up   Nearest PSNR : {:.3f}'.format(up_nearest_psnr))
  print('Up   Nearest SSIM : {:.3f}'.format(up_nearest_ssim))
  print('Up   Bicubic PSNR : {:.3f}'.format(up_bicubic_psnr))
  print('Up   Bicubic SSIM : {:.3f}'.format(up_bicubic_ssim))
  print('Up   Lanczos PSNR : {:.3f}'.format(up_lanczos_psnr))
  print('Up   Lanczos SSIM : {:.3f}'.format(up_lanczos_ssim))
