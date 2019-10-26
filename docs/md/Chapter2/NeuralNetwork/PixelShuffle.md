## Pixel Shuffle

Pixel Shuffle layer is one of the most recent layer type introduced in modern deep learning Neural Network.
Its application is closely related to the single-image super-resolution (SISR) research, i.e the ensemble techniques which aim at restoring a high-resolution image from a single low-resolution one (see section [SR](../SuperResolution/README.md) for further details).

The first SISR Neural Networks start with a preprocessing of low-resolution images in input with a bi-cubic up-sampling.
Then the image, with the same dimensions of the desired output, feeds the model which aim to increase the resolution and fix its details.
In this way the amount of parameters and moreover the computation required by the training section increase (by a factor equal to the square of the desired up-sampling scale), despite the required image processing is smaller.
To overcome this problem a Pixel Shuffle transformation, also known as *sub-pixel convolution*, was introduced [[Wenzhe2016Shuffle](https://ui.adsabs.harvard.edu/\#abs/2016arXiv160905158S)]: in this work the authors proved the equivalence between a regular transpose convolution, i.e the previous standard transformation to enlarge the input dimensions, and the sub-pixel convolution transformation without losing any information.
The Pixel Shuffle transformation reorganize the low-resolution image channels to obtain a bigger image with few channels.
An example of this transformation is shown in Fig. [1](../../../../img/pixel_shuffle.svg).

![Pixel Shuffle transformation. On the left the input image with `scale^2` (:= 9) channels. On the right the result of Pixel Shuffle transformation. Since the number of channels is perfect square the output is a single channel image with the rearrangement of the original ones.](../../../../img/pixel_shuffle.svg)

Pixel Shuffle rearranges the elements of the input tensor expressed as `H x W x C^2` to form a `scale x H x scale x W x C` tensor.
This can be very useful after a convolution process, in which the number of filters chosen drastically increase the number of channels, to "invert" the transformation like a sort of *deconvolution* function.

The main gain in using this transformation is the increment of computational efficiency of the Neural Network model.
The introduction of Pixel Shuffle transformation in the Neural Network tail, i.e after a sequence of small processing steps which increase the number of features, reorganize the set of features into a single bigger image, i.e the desired output in a SISR application.
The feature processing steps, which generally are faced on with convolutional layers, can be performed with smaller images in input and thus can be obtained faster since the up-scaling task will be performed by a single Pixel Shuffle transformation.

Despite this transformation has became a standard in super-resolution applications and thus it can be found into the most common deep learning libraries (e.g `Pytorch` and `Tensorflow` a `C++` implementation is hard to find.
Moreover, each library implements the transformation following its own data organization [^1].
For this reason we proposed in our libraries a dynamic version of the algorithm in `C++` able to perform both versions of the algorithm.

The algorithmic implementation of the pixel-shuffle transformation is essentially a re-indexing of the input values.
While in a `C++` implementation of the algorithm we could obtain the desired result inside a sequence of nested for loops playing with the loop indexes, for an efficient `Python` version we used a sequence of transposition and reshaping to rearrange the input values.
The following snippet shows the `NumPyNet` version of this algorithm.

```python
import numpy as np

class Shuffler_layer(object):

  def __init__(self, scale):

    self.scale = scale
    self.scale_step = scale * scale

    self.batch, self.w, self.h, self.c = (0, 0, 0, 0)

    self.output, self.delta = (None, None)

  def _phase_shift(self, input, scale):
    b, w, h, c = input.shape
    X = input.transpose(1, 2, 3, 0).reshape(w, h, scale, scale, b)
    X = np.concatenate(X, axis=1)
    X = np.concatenate(X, axis=1)
    X = X.transpose(2, 0, 1)
    return np.reshape(X, (b, w * scale, h * scale, 1))

  def _reverse(self, delta, scale):
    # This function apply numpy.split as a reverse function to numpy.concatenate
    # along the same axis also

    delta = delta.transpose(1, 2, 0)

    delta = np.asarray(np.split(delta, self.h, axis=1))
    delta = np.asarray(np.split(delta, self.w, axis=1))
    delta = delta.reshape(self.w, self.h, scale * scale, self.batch)

    # It returns an output of the correct shape (batch, in_w, in_h, scale**2)
    # for the concatenate in the backward function
    return delta.transpose(3, 0, 1, 2)

  def forward(self, input):

    self.batch, self.w, self.h, self.c = input.shape

    channel_output = self.c // self.scale_step # out_c

    # The function phase shift receives only in_c // out_c channels at a time
    # the concatenate stitches together every output of the function.

    self.output = np.concatenate([self._phase_shift(input[:, :, :, range(i, self.c, channel_output)], self.scale)
                                  for i in range(channel_output)], axis=3)

    self.delta = np.zeros(shape=self.out_shape, dtype=float)

  def backward(self, delta):

    channel_out = self.c // self.scale_step # out_c

    # I apply the reverse function only for a single channel
    X = np.concatenate([self._reverse(self.delta[:, :, :, i], self.scale)
                                      for i in range(channel_out)], axis=3)


    # The 'reverse' concatenate actually put the correct channels together but in a
    # weird order, so this part sorts the 'layers' correctly
    idx = sum([list(range(i, self.c, channel_out)) for i in range(channel_out)], [])
    idx = np.argsort(idx)

    delta[:] = X[:, :, :, idx]

```

The two functions `_phase_shift` and `_reverse` [^2] produce the re-arrangement of the indexes according to the pixel-shuffle transformation and its inversion [^3].
In the forward function we apply the `_phase_shift` to the sequence of channels (in the right order) and then we concatenate the results into a single tensor (output).
The backward function instead needs a re-ordering of channel sequence after the concatenation.

As told above, in the `C++` implementation provided into the `Byron` library we can compute the desired re-indexing using a series of nested for loops.
An equivalent solution can be obtained also by the contraction of the loops into a single one using divisions to obtain the right indexes.
This solution was taken in count into the first version of the library but the amount of required divisions weights on the computational performances.
The division operations are the most computationally expensive operations in terms of CPU clock-time.
The old versions of OpenMP multi-threading library forced the users to spend time in the evaluation of the "loop-contraction" to obtain the better performances by a single parallel for loop.
The new features of OpenMP library provide the very powerful `collapse` keyword which performs an automatic loop-contraction.
The keyword can be applied only with a series of independent and perfectly nested [^4] for loops which is exactly our case.
Moreover we have not to take in care any thread concurrency trouble since the iterations, as the output indexes, are totally independent.
We widely used the `collapse` keyword in the `Byron` library to simplify the code and the function evaluation but the Pixel-Shuffle case is one of the most efficient one, since we could collapse six nested loops [^5]  [on-line](https://github.com/Nico-Curti/Byron/blob/master/src/shuffler_layer.cpp).


[^1]: The main difference between `Pytorch` and `Tensorflow` is related to the storage organization of the image. `Tensorflow` has a "standard" input assessment as `H x W x C`. `Pytorch` has a so-called channel-first implementation and so the input tensor is organized as `C x H x W`.

[^2]: These function are "private" function of the object class.

[^3]: During the back-propagation, in fact, we have to apply the reverse transformation to the gradient.

[^4]: Two for loops are perfectly nested if there are not other code lines between them.

[^5]: In the Pixel-Shuffle we have to loop over batch, width, height, channels plus a couple of loops over the scale factor that we want to apply. In total we have to manage six dimensions that can be easily collapsed into a single one given by their product.



[**next >>**](./Cost.md)
