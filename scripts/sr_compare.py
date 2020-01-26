#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import argparse
import numpy as np
import pylab as plt
from glob import glob

__author__ = 'Nico Curti'
__email__ = 'nico.curti2@unibo.it'


def parse_args ():

  description = 'SR compare images'

  parser = argparse.ArgumentParser(description=description)
  parser.add_argument('--sr_dir', dest='sr_dir', required=True, type=str, action='store', help='Directory of SR images')
  parser.add_argument('--lr_dir', dest='lr_dir', required=True, type=str, action='store', help='Directory of original images')
  parser.add_argument('--out_dir', dest='out_dir', required=False, type=str, action='store', help='Output directory', default='gif')
  parser.add_argument('--out', dest='out', required=False, type=str, action='store', help='Output filenames without extension', default='sr_imgs')
  parser.add_argument('--fmt', dest='fmt', required=False, type=str, action='store', help='Output image format', default='png')
  parser.add_argument('--up', dest='upscale', required=False, type=int, action='store', help='Upscale factor', default=4)

  args = parser.parse_args()

  return args


def main ():

  args = parse_args()

  lr_files = sorted(glob('/'.join((args.lr_dir, '*.{}'.format(args.fmt)))))
  sr_files = sorted(glob('/'.join((args.sr_dir, '*.{}'.format(args.fmt)))))

  print('Found {:d} original images'.format(len(lr_files)))
  print('Found {:d} super-resolved images'.format(len(sr_files)))

  lr_imgs = (cv2.imread(f) for f in lr_files)
  sr_imgs = (cv2.imread(f) for f in sr_files)

  bc_imgs = (cv2.resize(lr, None, fx=args.upscale, fy=args.upscale, interpolation=cv2.INTER_CUBIC)
             for lr in lr_imgs)

  fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
  ax1.set_title('Bicubic Upsample', fontsize=24)
  ax2.set_title('Super Resolution Upsample', fontsize=24)
  ax1.axis('off')
  ax2.axis('off')

  out = '/'.join((args.out_dir, args.out))

  for (i, bc), sr in zip(enumerate(bc_imgs), sr_imgs):
    if bc.shape != sr.shape:
      raise ValueError('Incosinstent shape found! Pay attention to the upscale factor')

    print('\rProcessing {}'.format(i), end='', flush=True)
    ax1.imshow(np.rot90(bc))
    ax2.imshow(np.rot90(sr))
    fig.savefig(out + '-{}.png'.format(i), bbox_inches='tight')


if __name__ == '__main__':

  main()
