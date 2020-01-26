#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

import os
import cv2
import argparse
import numpy as np
from PIL import Image
import networkx as nx
from PIL import ImageDraw
import matplotlib.pylab as plt

__author__ = 'Nico Curti'
__email__ = 'nico.curti2@unibo.it'
__package__ = 'Research Group Graph plot'


class Group (object):


  COORDS = {
              'Logo UniBO'         : (None, None, None,    None,       'logo_unibo.png'),
              'Nico Curti'         : ( 770, 500 , 'DIMES', 'Dott.',    'group.jpg'),
              'Enrico Giampieri'   : (1640, 4362, 'DIMES', 'Dott.',    'group.jpg'),
              'Carlo Mengucci'     : ( 854, 4669, 'DIFA',  'Dott.',    'group.jpg'),
              'Daniel Remondini'   : (1445, 1582, 'DIFA',  'Prof.',    'group.jpg'),
              'Gastone Castellani' : (1593, 2611, 'DIMES', 'Prof.',    'group.jpg'),
              'Alessandra Merlotti': ( 800, 2100, 'DIFA',  'Dott.ssa', 'group.jpg'),
              "Daniele Dall'Olio"  : (None, None, 'DIFA',  'Dott.',    'danieledallolio.jpg'),
              'Armando Bazzani'    : (None, None, 'DIFA',  'Prof.',    'armandobazzani.jpg'),
              'Emanuela Marcelli'  : (None, None, 'DIMES', 'Prof.ssa', 'emanuelamarcelli.jpg'),
              'Alessandro Fabbri'  : (None, None, 'DIFA',  'Dott.',    'alessandrofabbri.png'),
              'Chiara Mizzi'       : (None, None, 'DIFA',  'Dott.ssa', 'chiaramizzi.jpg'),
            }

  COLORS = {
              'DIFA' : (0, 255, 0),
              'DIMES': (255, 0, 0)
           }

  CMAP = {
           (0, 255, 0) : 'lightgreen',
           (255, 0, 0) : 'red'
          }

  AVAILABLE_NAMES = COORDS.keys()

  def __init__ (self, members, img_folder=''):

    self._group_image = Image.open(os.path.join(img_folder, 'group.jpg')).convert('RGB')
    self._group_image = np.asarray(self._group_image)

    self.graph = nx.Graph()
    self.members = members
    self.img_folder = img_folder

  def _get (self, name, width=600):

    if name not in self.AVAILABLE_NAMES:
      raise NameError('Invalid member group. Available members are only {}'.format(self.AVAILABLE_NAMES))

    print('Processing {} image...'.format(name), end='', flush=True)

    if self.COORDS[name][-1] != 'group.jpg':
      photo = Image.open(os.path.join(self.img_folder, self.COORDS[name][-1])).convert('RGB')
      photo = cv2.resize(np.asarray(photo), dsize=(width, width))

    else:
      photo = self._group_image

    w, h, _ = photo.shape
    alpha = Image.new('L', photo.shape[:2][::-1], 0)

    x, y = self.COORDS[name][:2]

    draw = ImageDraw.Draw(alpha)

    if x is not None and y is not None:
      draw.pieslice([y - 50, x - 50, y + width + 50, x + width + 50], 0, 360, fill=255)
    else:
      draw.pieslice([0, 0, w, h], 0, 360, fill=255)

    alpha = np.asarray(alpha)
    result = np.dstack((photo, alpha))

    if x is not None and y is not None:
      result = result[x - 50 : x + width + 50, y - 50 : y + width + 50, :]

    # draw circle around the image

    half_w = width // 2
    if x is not None and y is not None:
      cv2.circle(result, (half_w + 50, half_w + 50), (width + 50)//2, color=(*self.COLORS[self.COORDS[name][2]], 255), thickness=50, lineType=8, shift=0)
    else:
      cv2.circle(result, (half_w, half_w), (width - 50)//2, color=(*self.COLORS[self.COORDS[name][2]], 255), thickness=50, lineType=8, shift=0)

    print('[done]')

    return result


  def _get_logo (self):

    w, h, _ = self._group_image.shape
    size = min(w, h)

    photo = Image.open(os.path.join(self.img_folder, self.COORDS['Logo UniBO'][-1])).convert('RGB')
    photo = cv2.resize(np.asarray(photo), dsize=(size, size))

    w, h, _ = photo.shape
    alpha = Image.new('L', photo.shape[:2], 0)

    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, w, h], 0, 360, fill=355)

    alpha = np.asarray(alpha)
    return np.dstack((photo, alpha))


  def compute_network_group (self):

    people_images = [self._get(member) for member in self.members]

    logo = self._get_logo()
    people_images.append(logo)

    labels = {i : '\n\n\n\n{0}\n{1}\n{2}'.format(self.COORDS[member][3], *member.split(' ')) for i, member in enumerate(self.members)}
    labels[len(self.members)] = '' # logo tag

    graph = nx.Graph()

    for (_, v), im in zip(labels.items(), people_images):
      graph.add_node(v, image=im)

    for v in list(labels.values())[:-1]: # exclude logo image
      graph.add_edge(v, '') # link to logo tag

    self.graph = graph

  def view (self):

    scale = 20
    pos = nx.spring_layout(self.graph, scale=scale, center=(0, 0), dim=2)

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))
    fig.subplots_adjust(left=.05, right=.95, top=.95, bottom=.05)

    ax.set_aspect('equal')

    labels  = {n : n for n in self.graph.nodes}
    pos_lbl = {n : (x, y - 5.5) for n, (x, y) in pos.items()}
    edge_color = [self.CMAP[self.COLORS[self.COORDS[member][2]]] for member in self.members]
    legend = set(edge_color)

    nx.draw_networkx_edges(self.graph, pos=pos, width=10., alpha=1, edge_color=edge_color, ax=ax)
    #nx.draw_networkx_labels(self.graph, pos=pos_lbl, labels=labels, font_size=18, ax=ax, font_weight='bold')

    scale += .5
    ax.set_xlim(-scale, scale)
    ax.set_ylim(-scale, scale)

    trans_fig = ax.transData.transform
    trans_axs = fig.transFigure.inverted().transform

    img_size = .2
    p2 = img_size * .5

    for n in self.graph:

      xx, yy = trans_fig(pos[n])
      xa, ya = trans_axs((xx, yy))

      im = plt.axes([xa - p2, ya - p2, img_size, img_size])
      im.set_aspect('equal')
      im.imshow(self.graph.nodes[n]['image'])
      im.axis('off')

    for color in legend:
      label = [k for k, v in self.CMAP.items() if v == color][0]
      label = [k for k, v in self.COLORS.items() if v == label][0]
      ax.scatter([], [], c=color, alpha=1, s=200, label=label, facecolor='none', edgecolor=color)

    ax.axis('off')
    #ax.legend(loc='best', fancybox=True, framealpha=1, shadow=True, borderpad=1, fontsize=24, prop={'size': 24})

    return (fig, ax)



def parse_args ():

  description = 'Research Group Acknowledgement plot'

  parser = argparse.ArgumentParser(description=description)

  parser.add_argument('--members',    required=True,  type=str, nargs='+', help='Members name')
  parser.add_argument('--output',     required=False, type=str, action='store', default='group',  help='Output filename of image group (without extension)')
  parser.add_argument('--img_folder', required=False, type=str, action='store', default='../img', help='Path/directory in which the images are stored')

  args = parser.parse_args()

  return args


def main ():


  args = parse_args()

  group = Group(members=args.members, img_folder=args.img_folder)
  group.compute_network_group()

  fig, ax = group.view()
  fig.savefig(args.output + '.png', bbox_inches='tight', transparent=False)


if __name__ == '__main__':

  main ()
