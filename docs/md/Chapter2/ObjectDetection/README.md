## Object Detection

Object detection is one of the larger deep learning sub-discipline, especially when we talk about Neural Network models.
This kind of problems aim to identify single or multiple objects into a picture or video stream.
The possible applications of these tools are everywhere these days and they involve object tracking, video surveillance, pedestrian detection, anomaly detection, people counting, self-driving cars or face detection, the list goes on.

There are many machine learning and deep learning techniques and algorithms proposed during the years and each one has its pros and cons.
The most prominent and moder techniques involves the use of very deep Neural Network models with a huge amount of parameters to tune.
The most famous one are probably the Faster R-CNN (*Faster Region Convolutional Neural Network*) [[ren2015faster](https://arxiv.org/abs/1506.01497)] and their "evolution" given by the YOLO (*You Only Look Once*) model [[redmon2015look](https://arxiv.org/abs/1506.02640), [redmon2016yolo9000](https://arxiv.org/abs/1612.08242), [redmon2018yolov3](https://arxiv.org/abs/1804.02767)].

The R-CNN models are one of the state-of-art CNN-based deep learning object detection model and their evolution into Fast R-CNN tries to improve the speed on object detection.
The standard approach for object detection is based on moving a *sliding window* to search in every position of the image the looking for objects.
However, the intrinsic problem of these kind of approach is in the dimension of the window and in the large computation required to map with multiple window sizes the full image.
Moreover, different objects or even the same kind of objects could have different aspect ratios and sizes in relation to the position of the camera which captured the image or to their distances.
R-CNN models try to overcome these problems generating about 2k region proposals, i.e bounding boxes, and applying to each one a image classification using standard CNN.
Finally, each detected region can be refined using a regression approach.

A Faster R-CNN model is based on the same idea but, instead of feeding the bounding boxes to the CNN, it feeds the input image to the CNN to generate a convolutional feature map.
Starting from this feature map we can easier identify the region of proposals (Region Proposal Network) and warp them into squares.
The list of these regions are then reshaped using a Polling layer and processed by a fully connected layer.
The advantages of Faster R-CNN are thus visible: we do not need to feed 2k region proposals to the CNN every time but the feature map is generate once per image using the convolution operation.
In this way we can also separate the feature map creation to the selective search algorithm.

A key role is played by the *anchor* concept: an *anchor* is essentially a box and it identify the shape of a portion of the input image at different scale level.
The CNN feature map feeds the Region Proposals Network which uses a sliding window over it generating `k` anchor boxes.
These boxes are certainly fewer than the 2k previous cited windows.

A breakthrough idea on the real-time object detection was the introduction of the YOLO model.
The model was developed by Redmon et al. at Washington University and it is probably the state-of-art on object detection, especially for its very incredible speed (it can reach 45 FPS on modern GPUs!).
Certainly it is the faster method public available but its popularity is due also to its innovative strategy in object detection.
Despite all the other algorithms use regions to localize the object into the image, the YOLO network does not look at the complete image but only on a parts of it which has the higher probability to contain an object.
In YOLO a single CNN predicts the bounding boxes and the class probabilities of them.
YOLO slit a single image into a `S x S` grid and on each grid `m` bounding boxes are taken.
For each of them, the CNN outputs a class probability and offset values.
Finally these bounding boxes are filtered according to their probability and a chosen threshold.

One of the most bigger limitation of this model is that it struggles with small objects.
This is due to the spatial constraints of the algorithm.
Fortunately, in the previous section we have already discussed on how we can overcome this kind of problem using Super Resolution.
In the next section we will discuss about further characteristics of the YOLO model and about its implementation into the Byron library and its efficiency against the original implementation.
Finally we will join the efficiency of the previous Super Resolution models to the performances of our custom implementation of YOLO.


[**next >>**](./Yolo.md)
