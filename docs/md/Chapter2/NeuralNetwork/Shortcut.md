## Shortcut connections

The harder becomes the problem to solve and the deeper [^1] will be the Neural Network model created to solve it.
The payback of these deep network structures is a reduction in accuracy after reaching a maximum, the so-called *degradation problem*.
This accuracy reduction does not arise from over-fitting problems but it is due to numerical instabilities (*vanishing gradient* - as the gradient is back-propagated to earlier layers, repeated multiplications may make the gradient very small) and troubles related to the data dimensionality (called *curse of dimensionality*).
Despite Neural Network could be defined as universal function approximators, adding numerous layers and thus parameters, the result in accuracy does not grow proportionally.
With simple empirical examples we can easily see how the accuracy starts to saturate (and eventually degrade) with an increasing number of layers.
Those problems poses a limit to the number of layers usable on a Neural Network model and seem that the shallower networks learn better than their deeper counterparts.
Keeping this results in mind we can think about a strategy to skip these "extra" layers.

![Scheme of shortcut connections into a deep learning model. Each colored line connects the previous layer block to the following one. The output combination can be customized but the most used one is a simple linear combination of them. A particular attention must be payed with the dimensions management.](../../../../img/shortcut_layer.png)


We can obtain a simple solution to this problem making extra connections between layers called shortcuts or residuals.
A shortcut is a link between two distant layers without involving the set of layers between them, a so-called "identity shortcut connection".
A graphical example is show in Fig. [1](../../../../img/shortcut_layer.png).
The authors of [[he2015deep](https://arxiv.org/abs/1512.03385)] argue that stacking layers should not degrade the network performance, because we could simply stack identity mappings (layer that does not do anything) upon the current network, and the resulting architecture would perform the same.
In the original paper, the shortcut connections perform an operation like:

$$
H(x) = F(x_1) + x_2
$$

where `F(x)` is the output of the previous block and `x` is the output of the current block.
The function `F` generalizes the combination of these two values [^2].

The introduction of these extra connections bring us to the ResNet (Residual Neural Network) models era in which a key role was played by the object detection models.
A wide range of modern deep learning architectures use this kind of connections and in this way they involve a large number of layers: famous examples of this kind are the VGG models and the ResNets.
We have done a large use of this connections also in the models described in the next sections, either for object detection purposes (ref. [object_detection](../ObjectDetection/README.md)), Super Resolution (ref. [SuperResolution](../SuperResolution/README.md)) and mostly for our segmentation (ref. [Segmentation](../Segmentation/README.md)) applications.
This kind of functions are becoming so popular into the modern deep learning models that more and more often we describe a model according to its *residual blocks*, i.e the layer ensemble between two shortcut connection.

From a computational point of view the implementation of this kind of "layers" is straightforward in `Python` (and thus in our `NumPyNet`): we can easily implement a network structure as a list of object and thus a shortcut connection simply combine the output of two elements of it.
We met more problems when we translated this idea into `C++`.
The `C++` language is more rigid with the data type involved in each operation and we have to carefully manage the "signature" (list of input arguments) of each function.
In this way we can not simply implement a list of different object types as a network structure.

A possible solution can reached using the object inheritance: we can create a single `Base_layer` object and specialize it according to our needs.
This is certainly the most `C++`-like solution but it requires many checks (if statements) at execution time.
An other (more modern) solution is provided by the new (standard) data types provided by the `C++17`: in particular we refer to the `variant` objects.
A `variant` is a `template union` data-type which allow to combine and reinterpret different data types into a single object.
The most important consequence of the use of this kind of data-type is that we can easily jump to one type to an other using `constexpr` statement which (by definition) are solved at compile time.
Besides the particulars involved into this kind of implementation is important to notice that the difference between the two solution is the same between run-time and compile-time: if we perform computation at compile-time we will not re-execute when the code runs and thus we can reach better time performances.
The `Byron` library widely use `template`s and with the support of the `C++17` standard a large part of costly operations are execute one-for-all at compile time [^3].

Using `variant` object and `templates` we can easily implement a shortcut connection also in `C++` as can be seen on the on-line version of the code (ref. [on-line](https://github.com/Nico-Curti/Byron/blob/master/src/shortcut_layer.cpp)).


[^1]: The deep of a Neural Network model is related to the number of layers which made it.

[^2]: In our implementations we choose to generalize this formula as $$H(x) = \alpha x_1 + \beta x_2$$.

[^3]: We provide also an efficient retro-compatibility for "old-standard users" with a custom implementation of `variant` objects.

[**next >>**](./PixelShuffle.md)
