#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import time
import json
import argparse
import paramiko
import pylab as plt

__author__ = 'Nico Curti'
__email__ = 'nico.curti2@unibo.it'


def parse_args ():

  description = 'SR compare images'

  parser = argparse.ArgumentParser(description=description)
  parser.add_argument('--configfile', dest='configfile', required=True, type=str, action='store', help='SSH config filename')
  parser.add_argument('--imagefile', dest='imagefile', required=True, type=str, action='store', help='Image filename')

  args = parser.parse_args()

  return args


def main ():

  args = parse_args()

  with open(args.configfile, 'r') as fp:
    config = json.load(fp)

  img = cv2.imread(args.imagefile)

  if img.shape[0] > 1000 or img.shape[1] > 1000:
    w, h, _ = img.shape
    nw, nh = (w % 10, h % 10)
    img = cv2.resize(img, dsize=None, fx=0.1, fy=0.1)


  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect('137.204.48.15', port=22,
              username=config['username'],
              password=config['pwd'])

  ftp_client = ssh.open_sftp()

  showCrosshair = False
  fromCenter = False

  try:
    while True:

      cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
      roi = cv2.selectROI('Image', img, fromCenter, showCrosshair)
      roi = img[roi[1] : roi[1] + roi[3], roi[0] : roi[0] + roi[2], :]
      cv2.imwrite('selected_roi.png', roi)

      print('Selected ROI: {}'.format(roi.shape[:2]), flush=True)

      bc = cv2.resize(roi, dsize=None, fx=4, fy=4)
      bc = cv2.cvtColor(bc, cv2.COLOR_BGR2RGB)

      ftp_client.put('selected_roi.png', 'Byron/selected_roi.png')

      print('Super Resolve ROI...', flush=True)

      cmd = ' && '.join(('export LD_LIBRARY_PATH=~/Byron/build:$LD_LIBRARY_PATH',
                         'cd Byron',
                         './bin/SR_test -d data/wdsrx4.data -f selected_roi.png'))
      stdin, stdout, stderr = ssh.exec_command(cmd)

      time.sleep(1)

      ftp_client.get('Byron/selected_roi.png_sr.png', 'selected_roi_sr.png')

      sr = cv2.imread('selected_roi_sr.png')
      sr = cv2.cvtColor(sr, cv2.COLOR_BGR2RGB)


      fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
      ax1.axis('off')
      ax2.axis('off')
      ax1.set_title('Bicubic Zoom', fontsize=24)
      ax1.imshow(bc)
      ax2.set_title('Super Resolution Zoom', fontsize=24)
      ax2.imshow(sr)

      fig.tight_layout()

      plt.show()

  except KeyboardInterrupt:
    pass

  ftp_client.close()
  ssh.close()

  return 0


if __name__ == '__main__':

  main()
