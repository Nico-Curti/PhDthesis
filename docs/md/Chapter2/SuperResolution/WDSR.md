## Super Resolution Models

![Super Resolution models analyzed in this word. **(left)** EDSR model. The model is a modified version of the ResNet architecture designed for SISR applications. The architecture is made by a sequential CNN framework which processes the input image. The EDSR has more than 43 million of parameters in total. **(right)** WDSR model. The model is the updated version of the EDSR one. The model optimizes its numerical efficiency using a different approach in the analysis of low- and high-frequency components in the input image. the WDSR has slight more than 3.5 million of parameters, less than 10% of the EDSR model.](../../../../img/SR_models.png)

There were different kind of models proposed for image Super Resolution purposes but in this work we focused only on two of them.
Both are based on deep learning Neural Network models and they became famous in the research community since they both won the last NTIRE editions, 2017 and 2018 respectively.

|   Layer                |  Channels </br> input/output | Filter </br> dimensions | Number of </br> Parameters |
|:----------------------:|:----------------------------:|:-----------------------:|:--------------------------:|
| Conv. input            | 3/256                        | `3 x 3`                 | 6912                       |
| Conv. (residual block) | 256/256                      | `3 x 3`                 | 589824                     |
| conv. (pre-shuffle)    | 256/256                      | `3 x 3`                 | 589824                     |
| Conv. (upsample block) | 256/1024                     | `3 x 3`                 | 2359296                    |
| Conv. output           | 256/3                        | `3 x 3`                 | 6912                       |

The first model is called EDSR (*Enhanced Deep Super Resolution*) and was firstly proposed at the NTIRE challenge in 2017 [[Agustsson_2017_CVPR_Workshops](www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf)].
The EDSR model structure could be broadly summarized as an updated version of the SRResNet model which is already a modified version of the classical ResNet (standard CNN based on multiple residual blocks).
The major updates concern a series of optimization to improve the training speed and the quality of the output image.
In particular, the batch normalization steps are removed to improve the algorithm speed: it was proved that in low-level vision tasks as the super resolution one, i.e without complex evaluations as object detection, a wide and dynamic range of outputs can be useful [[EDSR](https://ui.adsabs.harvard.edu/\#abs/2017arXiv170702921L)].
A scheme of the EDSR architecture is shown in Fig. [1](../../../../img/SR_models.png)(a) and the full set of parameters are reported in the Table: the EDSR model has more than 43 million of parameters in total.

A first convolutional layer takes the LR image which is processed using 256 filters.
Then a set of 32 residual blocks (convolution with 256 filters + ReLU activation + convolution with 256 filters + linear combination of the output with the input) process the feature map.
The tail of the architecture is made by an up-sample block which re-organize the pixels using a series of convolution and pixel-shuffle functions.
The up-sampling follows the scale factor imposed: the model increases the spatial resolution of the image by a fixed scale factor (x2 and x4 in our applications) and each pixel-shuffle application is equivalent to a x2 in the output sizes [^1].

The first convolutional layer extracts the low frequency components of the input image which will be combined to the output of the residual blocks at the end of the model.
The residual blocks with their relative convolutional layers extract the feature map and the high frequency informations into the LR image: in this way the low- and high-frequency components are "independently" analyzed by the model and then re-combined in the output.
The last set of up-sampling blocks simply reshape and reorganize the extracted informations according to the desired sizes.

The large amount of filters of the up-sampling blocks and the input dimensions drastically affect the computational performances of the model: we numerically evaluated that the most time spent by the processing is related to the tail of the model and thus to the up-sampling blocks.

The second analyzed and implemented model is the WDSR (*Wide Deep Super Resolution*) model which won the NTIRE challenge in 2018 [[WDSR](https://ui.adsabs.harvard.edu/\#abs/2018arXiv180808718Y)].
The WDSR model is a modified version of the EDSR one.
The improvements principally concern two aspects: the network structure and the residual blocks.

As shown in Fig. [1](../../../../img/SR_models.png)(b), the WDSR simplifies the network architecture removing the convolutional layers after the pixel-shuffle ones.
Moreover, if the EDSR applies a x2 up-sampling every pixel-shuffle layer, in the WDSR a single pixel-shuffle function performs a x4 up-sampling.
This update drastically reduce the computational time and the amount of parameters.
Furthermore, the combination between low- and high- frequency components in this case are processed separately (two different branches) and only at the end they are re-combined (ref. Fig. [1](../../../../img/SR_models.png)(b)).

|   Layer                     |  Channels </br> input/output | Filter </br> dimensions | Number of </br> Parameters |
|:---------------------------:|:----------------------------:|:-----------------------:|:--------------------------:|
| Conv. input 1               | 3/32                         | `3 x 3`                 | 864                        |
| Conv. 1 (residual block)    | 32/192                       | `3 x 3`                 | 55296                      |
| conv. 2 (residual block)    | 192/32                       | `3 x 3`                 | 55296                      |
| Conv. (pre-shuffle)         | 32/48                        | `3 x 3`                 | 13824                      |
| Conv. input 2 (pre-shuffle) | 3/48                         | `5 x 5`                 | 3600                       |


The WDSR also changes the residual block structure: the ReLU activations tends to block the information flow from the first layers [[MobileNet](https://ui.adsabs.harvard.edu/\#abs/2018arXiv180104381S)] and in super resolution structures is important to prevent it since they contain the low-frequency components of the image.
To overcome this problem without increasing the number of parameters the WDSR proposes the so-called "passage enlargement", i.e the reduction in the number of channels in input and the corresponding enlargement of the output channels before the ReLU activation.
This optimization allows to increase the number of channels to be activated and thus a better information flux along the network keeping the required non-linearity.
The number of parameters is however constant because there is only a re-arrangement of the input/output parameters.
The list of network parameters are reported in the Table: the WDSR has slight more than 3.5 million of parameters, less than 10% of the EDSR model.
This confirms the computational efficiency of the WDSR against the EDSR one.

In this work we used pre-trained models so we could not change the network structure or change their learning weights.
For this reason we could use only a x2, x4 EDSR model and a x4 WDSR model.
The weights were converted to the `Byron` format and our custom implementation of the network used for the applications.
We would stress that our could be the first `C++` implementation of these models and probably the first optimized version for CPUs environment [^2].

[^1]: It is straightforward that adding multiple up-sampling blocks and thus pixel-shuffle functions we can train the model according to every desired upscale.

[^2]: We have to mention also that the public available implementation of these models are developed only in `Tensorflow` and `PyTorch` but the major part of them does not work in CPU environments without heavy modifications.


[**next >>**](./Dataset.md)
