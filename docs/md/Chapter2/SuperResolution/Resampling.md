## Resampling

Up to now we have talked about neural network models as classification algorithms.
In the SR problem we have no classes but the desired output is a image.
This behavior is often hard to digest but it does not change anything about the previous consideration.
The only change will be related to the size of the neural network and its amount of parameters that could drastically increase due to the larger output required.
Lets start from the beginning: to feed a super-resolution model we have to use a series of prior-known LR-HR image association.
In the real life we always have a series of images, typically LR images, and we want to enlarge the resolution of them, i.e enlarge the spatial dimensions of the input image, to better see some particulars or just to create an output without artifacts or evident pixel grains.
If we consider these series of images as the HR one we can easily down-sample them without particular troubles [^1].
This re-sampling will introduce a aliasing factor that our model should learn to nullify.
The number of model parameters is typically around the `10^7` so if we introduce any filtering process (degradation) in the input image the model will be able to overcome also these problems.

Starting from these considerations we can down-sample our images by a desired scale factor: common scale factor are between 2 and 8 and in this work we will refer to a scaling equal to 4.
A crucial role is played by the re-sampling (or down-sampling) algorithm chosen for the artificial image degradation.
Any down-sampling algorithm, in fact, loose part of the original information by definition.
Thus we can facilitate the learning choosing a lossless one but in this way we will loose in generalization (the model will not learn how to overcome some cases), or we can apply a drastic down-sample technique and achieve better performances later.

The simpler down-sampling algorithm is given by a *nearest interpolation*.
This algorithm pass a kernel mask over the image and it substitutes each pixel mask to their average [^2].
This procedure can be achieved using a *Pooling* algorithm (in particular an AveragePooling) (ref. [Pooling](../NeuralNetwork/Pooling.md) for further information) for the down-sample or we can use an UpSample layer.
The UpSample function is commonly related to GAN (Generative Adversarial Networks) models in which we have to provide a series of artificial images to a given Neural Network but it is a function which can be introduce inside a Neural Network model to rescale the number of features.
We mention it in this section since it is not intrinsically related to a Neural Network model but it could be use as image processing technique.

We provide an implementation of this algorithm either in `NumPyNet` either in `Byron` library using different techniques.
The UpSample function inside a Neural Network model has to provide both up- and down- sampling technique since one is used in the forward function and its inverse during the back-propagation.
To achieve this function in `NumPyNet` we can use a series of reshapes and striding on the input matrix as shown in the following snippet.

```python
import numpy as np
from numpy.lib.stride_tricks import as_strided

class Upsample_layer(object):

  def __init__(self, stride=(2, 2), scale=1., **kwargs):

    self.scale = float(scale)
    self.stride = stride

    if not hasattr(self.stride, '__iter__'):
      self.stride = (int(stride), int(stride))

    assert len(self.stride) == 2

    if self.stride[0] < 0 and self.stride[1] < 0: # downsample
      self.stride = (-self.stride[0], -self.stride[1])
      self.reverse = True

    elif self.stride[0] > 0 and self.stride[1] > 0: # upsample
      self.reverse = False

    else:
      raise NotImplementedError('Mixture upsample/downsample are not yet implemented')

    self.output, self.delta = (None, None)

  def _downsample (self, input):
    batch, w, h, c = input.shape
    scale_w = w // self.stride[0]
    scale_h = h // self.stride[1]

    return input.reshape(batch, scale_w, self.stride[0], scale_h, self.stride[1], c).mean(axis=(2, 4))

  def _upsample (self, input):
    batch, w,  h,  c  = input.shape     # number of rows/columns
    b,     ws, hs, cs = input.strides   # row/column strides

    x = as_strided(input, (batch, w, self.stride[0], h, self.stride[1], c), (b, ws, 0, hs, 0, cs)) # view a as larger 4D array
    return x.reshape(batch, w * self.stride[0], h * self.stride[1], c)                                     # create new 2D array

  def forward(self, input):
    self.batch, self.w, self.h, self.c = input.shape

    if self.reverse: # Downsample
      self.output = self._downsample(input) * self.scale

    else:            # Upsample
      self.output = self._upsample(input) * self.scale

    self.delta = np.zeros(shape=input.shape, dtype=float)

  def backward(self, delta):
    if self.reverse: # Upsample
      delta[:] = self._upsample(self.delta) * (1. / self.scale)

    else:            # Downsample
      delta[:] = self._downsample(self.delta) * (1. / self.scale)


```

Thus the down-sampling algorithm is obtained reshaping the input array according the two scale factors (`strides` in the code) along the two dimensions and computing the mean along these axes.
Instead the up-sample function use the stride functionality of the `Numpy` array to rearrange and replicate the value of each pixel in a mask of size `strides x strides`.

The same functionality can be obtained in the `C++` version of the code provided by the `Byron` library in which we compute the right indexes along a nested sequence of for loops (ref. [on-line](https://github.com/Nico-Curti/Byron/blob/master/src/upsample_layer.cpp)).
We have to take in care the summation reduction provided by the down-sampling according to the thread concurrency: in this case we can not generalize the loop collapsing to the full set of lops but we have to separately manage the summation in a sequential section.

A more sophisticated interpolation algorithm, which reduce the loosing information, is provided by the *bicubic interpolation*.
The re-sampling algorithm interpolate the information provided by the nearest pixels using a cubic function.
Given a pixel, the interpolation function evaluates the 4 pixels around it applying a filter given by the equation:

$$
k(x) = \frac{1}{6} \left\{ \begin{array}{rc}
  (12 - 9B - 6C) |x|^3 + (-18 + 12B + 6C) |x|^2 + (6 - 2B)           & \mbox{if}        |x| < 1 \\
  (−B − 6C) |x|^3 + (6B + 30C) |x|^2 + (−12B − 48C) |x| + (8B + 24C) & \mbox{if} 1 \leq |x| < 2 \\
  0                                                                  & \mbox{otherwise}         \\
  \end{array}
  \right.
$$

where `x` identifies each pixel below the filter.
Commonly values used for the filter parameters are `B=0` and `C=0.75` (used by `OpenCV` library) or `B=0` and `C=0.5` used by `Matlab`[^3].
Despite this function was also implemented in the most common library in `Python` we provide an efficient multi-threading implementation in the `Byron` library.

Equivalent performances could be achieved using a generalized version of the bicubic filter which use the 8 positions mask around each pixel, the so called Lanczos filter.
Also this function was provided into the `Byron` library.

To better understand the told above functions we can consider their application on the simple image given in Fig. [1](../../../../img/up_down_sampling.svg).

![Re-sampling image example. **(left)** The original image. **(up right)** The down-sampled blue-ROIs using different interpolation algorithm (Nearest, Bicubic and Lanczos, respectively). We use a scale factor equal to 2 (half size in down-sampling and double size in up-sampling). The Lanczos interpolation is the lossless algorithm but from a qualitative point-of-view the result is the quite the same of the bicubic one. **(down right)** The up-sampled red-ROIs using the same interpolation algorithm of the upper row. Also in the Up-sampling the Lanczos and bicubic algorithms produces equal qualitative results. The Nearest algorithm produces the worse results in both up- down- cases.](../../../../img/up_down_sampling.svg)

In the figure the three algorithms were applied over the same image to highlight the differences against the down-sampling and up-sampling.
The nearest interpolation algorithm produces always the worse results both in up-sampling and down-sampling.
In the bicubic and Lanczos down-sampling we can better appreciate the "preservation" of the line shapes that are lost using the Nearest algorithm.
The result obtained by bicubic and Lanczos are quite similar in both cases but the computational cost of the Lanczos algorithm is greater than the bicubic one.
This is the reason why the bicubic interpolation is the most used technique for image resizing with a balance between computational cost and qualitative results.
In our implementation of SR algorithms we chose to use the bicubic interpolation for those reasons.

The aim of SR algorithm is to overcome these results and obtain a better quality image either from an optical point-of-view either from a mathematical one.
Until now we are considering the quality of the digital image only from a qualitative point-of-view.
In the next section we will introduce some useful mathematical scoring to numerically evaluate the image quality.


[^1]: Ignoring particular cases the hardest step is always to enlarge the image resolution and not the inverse step.

[^2]: The inverse (up-sampling) interpolation simply replicates each pixel in each dimension by a number equal to the scale factor.

[^3]: In this case the filter is also called Catmull-Rom filter.

[**next >>**](./QualityImage.md)

