#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from __future__ import print_function

import numpy as np

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']
__package__ = 'PixelShuffle example'


class Shuffler_layer(object):

  def __init__(self, scale):
    '''
    Shuffler Layer, performs a Pixel Shuffle.

      input shape (batch, w, h, c) -> (batch, w * scale, h * scale, c // scale**2) out shape

    Paramenters:
      scale : int, scale of the shuffler.
    '''
    self.scale = scale
    self.scale_step = scale * scale

    self.batch, self.w, self.h, self.c = (0, 0, 0, 0)

    self.output, self.delta = (None, None)

  def __str__(self):
    batch, out_width, out_height, out_channels = self.out_shape()
    return 'Shuffler x {:3d}            {:>4d} x{:>4d} x{:>4d} x{:>4d}   ->  {:>4d} x{:>4d} x{:>4d} x{:>4d}'.format(
           self.scale,
           batch, self.w, self.h, self.c,
           batch, out_width, out_height, out_channels)

  def out_shape(self):
    return (self.batch, self.w * self.scale, self.h * self.scale, self.c // (self.scale_step))

  def _phase_shift(self, inpt, scale):
    '''
    Shuffles of the pixel in a given input

    Parameters:
      inpt : the input of this function is not the entire batch of images, but only
        a N channels at a time taken from every image, where N = out_c // scale**2
      scale : int, scale factor of the layer
    '''
    b, w, h, c = inpt.shape
    X = inpt.transpose(1, 2, 3, 0).reshape(w, h, scale, scale, b)
    X = np.concatenate(X, axis=1)
    X = np.concatenate(X, axis=1)
    X = X.transpose(2, 0, 1)
    return np.reshape(X, (b, w * scale, h * scale, 1))

  def _reverse(self, delta, scale):
    '''
    Reverse function of _phase_shift

    Parameters:
      delta : input batch of deltas with shape (batch, out_w, out_h, 1)
      scale : int ,scale factor of the layer
    '''
    # This function apply numpy.split as a reverse function to numpy.concatenate
    # along the same axis also

    delta = delta.transpose(1, 2, 0)

    delta = np.asarray(np.split(delta, self.h, axis=1))
    delta = np.asarray(np.split(delta, self.w, axis=1))
    delta = delta.reshape(self.w, self.h, scale*scale, self.batch)

    # It returns an output of the correct shape (batch, in_w, in_h, scale**2)
    # for the concatenate in the backward function
    return delta.transpose(3, 0, 1, 2)

  def forward(self, inpt):
    '''
    Forward function of the shuffler layer: it recieves as input an image in
    the format ('batch' not yet , in_w, in_h, in_c) and it produce an output
    with shape ('batch', in_w * scale, in_h * scale, in_c // scale**2)

    Parameters:
      inpt : input batch of images to be reorganized, with format (batch, in_w, in_h, in_c)

    '''

    self.batch, self.w, self.h, self.c = inpt.shape

    channel_output = self.c // self.scale_step # out_C


    # The function phase shift receives only in_c // out_c channels at a time
    # the concatenate stitches toghether every output of the function.

    self.output = np.concatenate([self._phase_shift(inpt[:, :, :, range(i, self.c, channel_output)], self.scale)
                                  for i in range(channel_output)], axis=3)

    # output shape = (batch, in_w * scale, in_h * scale, in_c // scale**2)

  def backward(self, delta):
    '''
    Backward function of the shuffler layer: it reorganize the delta to match the
    input shape, the operation is the exact inverse of the forward pass.

    Parameters:
      delta : global delta to be backpropagated with shape (batch, out_w, out_h, out_c)
    '''

    channel_out = self.c // self.scale_step  #out_c

    # I apply the reverse function  only for a single channel
    X = np.concatenate([self._reverse(self.delta[:, :, :, i],self.scale)
                                      for i in range(channel_out)], axis=3)


    # The 'reverse' concatenate actually put the correct channels toghether but in a
    #  weird order, so this part sorts the 'layers' correctly
    idx = sum([list(range(i, self.c, channel_out)) for i in range(channel_out)], [])
    idx = np.argsort(idx)

    delta[:] = X[:, :, :, idx]


if __name__ == '__main__':


  from PIL import Image
  from PIL import ImageDraw
  import seaborn as sns
  import pylab as plt
  from matplotlib.colors import ListedColormap


  def draw_grid (image):
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / 5)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=0)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=0)
    return image

  colors = sns.color_palette('hls', 9)

  # suppose img1 and img2 are your two images
  imgs = [Image.new('RGB', size=(51, 51), color=(int(colors[i][0]*255),
                                                 int(colors[i][1]*255),
                                                 int(colors[i][2]*255)
                                                 ))
          for i in range(9)]

  sx, sy = (3, 3)

  nw, nh = ( imgs[0].size[0] + sx*(len(imgs)-1),
             imgs[0].size[1] + sy*(len(imgs)-1)
             )

  imgs = [draw_grid(im) for im in imgs]

  res = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
  for i, im in enumerate(imgs):
    res.paste(im, (sx*i, sy*i))

  # Pixel shuffle

  input = np.arange(0, 50 * 50 * 9).reshape(1, 9, 50, 50)
  input = input.transpose(0, 2, 3, 1) # Nice visualizations with the transpose arange

  cmap = ListedColormap(colors.as_hex())

  layer = Shuffler_layer(scale=3)

  layer.forward(input)
  forward_out = layer.output

  plt.rc('grid', linestyle="-", color='black')

  fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 7))
  fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.,
                      wspace=0.3)
  fig.suptitle('scale = {}'.format(3), fontsize=24, y=0.075)

  ax1.imshow(res)
  ax1.set_title('Original Image\n($scale^2$ channels)', fontsize=24, y=1.1)
  ax1.axis('off')

  ax2.imshow(forward_out[0,:10,:10,0], cmap=cmap)
  ax2.set_title('High Resolution Image', fontsize=24, y=1.1)
  # And a corresponding grid
  ax2.grid(which='both')

  # Or if you want different settings for the grids:
  ax2.grid(which='minor', alpha=1, linewidth=2)
  ax2.grid(which='major', alpha=1, linewidth=2)
  ax2.set_xticks(np.arange(-0.5, 10.5, 1))
  ax2.set_xticks(np.arange(-0.5, 10.5, 1), minor=True)
  ax2.set_yticks(np.arange(-0.5, 10.5, 1))
  ax2.set_yticks(np.arange(-0.5, 10.5, 1), minor=True)
  ax2.axes.get_xaxis().set_ticks([])
  ax2.axes.get_yaxis().set_ticks([])

  bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="w", ec="k", lw=2)
  t = ax1.text(85, 40, "Shuffle", ha="center", va="center", rotation=0,
              size=15,
              bbox=bbox_props)

  fig.savefig('../img/pixel_shuffle.svg')
  plt.show()
