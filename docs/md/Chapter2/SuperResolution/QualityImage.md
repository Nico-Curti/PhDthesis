## Image Quality

The most common image quality evaluator is given by our eyes.
This is true also for SR problems: the final purpose still remain to obtain images that are better visible for human eyes, the so called *visual loss*.
We can however provide some mathematical formulas which allows to quantitative evaluate the image quality.
In both cases we need to establish a relation between the original image and the produced one.
Thus we can formulate a quality score only with a reference image.
In SR problems, or more in general in up-sampling problems, we can compare the original HR image with the image obtained by the output of our model.
In this way our quality score will be a measure of similarity between the two images.

The simple similarity score can be obtained evaluating the peak-signal-to-noise-ratio (PSNR).
This quantity is commonly used to establish the compression lossless of an image and it can be computed as

$$
PSNR = 20 \cdot \log_{10}\left( \frac{\max(I)}{\sqrt(MSE)} \right)
$$

where `max(I)` is the maximum value which can be taken by a pixel in the image (in general it will be 1 or 255 depending on the image format chosen) and MSE is the Mean Square Error (ref. [Cost](../NeuralNetwork/Cost.md)) between the original image and the reconstructed one.
The MSE for an image can be computed as:

$$
MSE = \frac{1}{WH} \sum_{i=1}^{W}\sum_{j=1}^{H} \left( I(i, j) - K(i, j) \right)^2
$$

where `W`, `H` are width and height of the two images and `I`, `K` are the original and reconstructed images, respectively.

In other words the PSNR is the maximum power of the signal over the background noise.
It is expressed in decibel (dB) because the image values ranging in a wide interval and the logarithmic function rearrange the domain.
Thus we can conclude that high PSNR values are associated to a good reconstruction of the original image.

The PSNR is probably the most common quality score [[PSNR_SSIM](https://ieeexplore.ieee.org/document/5596999)] but it does not always related to a qualitative visual quality.
Despite it is commonly used as loss function for SR models.

|       | Nearest  | Bicubic | Lanczos |
|:-----:|:--------:|:-------:|:-------:|
| PSNR  | 25.118   | 27.254  | 26.566  |
| SSIM  |  0.847   |  0.894  |  0.871  |

Considering the series of images shown in Fig. [-1](../../../../img/up_down_sampling.svg) we can evaluate the PSNR score starting from a down-sampled image.
Taking the down-sampled image obtained with the Lanczos algorithm we can compare the original image with their up-sampled version given by the three methods (ref. Table).
As expected, the lowest PSNR value is achieved by the nearest interpolation method while the best performances are obtained by the bicubic algorithm.
This confirm the wider use of bicubic method in image processing applications.
Moreover we have to take in account that an increment of 0.25 in PSNR value correspond to a visible improvement for human eyes.

A more advanced quality score, commonly used in super resolution image evaluation, is given by the *Structural SIMilarity index* (SSIM).
The SSIM aims to mathematically evaluate the structural similarity between two images taking into account also the visible improvement seen by human eyes.
The SSIM function can be expressed as

$$
SSIM(I, K) = \frac{1}{N}\sum_{i=1}^{N} SSIM(x_{i}, y_{i})
$$

where `N` is the number of arbitrary patches which divide the image [^1].
For each patch the SSIM is computed as

$$
SSIM(x, y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{ ({\mu_x}^2 + {\mu_y}^2 + c_1)({\sigma_x}^2 + {\sigma_y}^2 + c_2) }
$$

where $$\mu$$ and $$\sigma$$ are the means and variances of the images, respectively, and $$\sigma_{xy}$$ represents the covariance.
The $$c_1$$ and $$c_2$$ parameters are fixed to avoid mathematical divergence.
Also in this case higher value of SSIM corresponds to high similarity between the original image and the reconstructed one.

Based on the previous equation we can highlight a link with the pooling functions discussed in [Pooling](../NeuralNetwork/Pooling.md).
Also in this case, in fact, we works with a window/kernel moved along the image which applies a mathematical function on the underlying pixels.
This equivalence suggests an easy implementation of this method with slight modifications of the previous code.

The evaluation of SSIM quality score on the previous up-sampled images (ref. Fig. [-1](../../../../img/up_down_sampling.svg) and Table) confirms the results obtained by the PSNR.
Also in this case the worst reconstruction is obtained by the nearest algorithm while the highest SSIM is obtained by the bicubic algorithm.
The gap between SSIM values is smaller than PSNR ones but this is due to the different domains of the two functions.

[^1]: Patch dimensions commonly used are `11 x 11` or `8 x 8`.

[**next >>**](./WDSR.md)
