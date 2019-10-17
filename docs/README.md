| **Author**   | **Project** | **Documentation**                                                                   | **Build Status**              |
|:------------:|:-----------:|:-----------------------------------------------------------------------------------:|:-----------------------------:|
|   [**N. Curti**](https://github.com/Nico-Curti)   |  **PhDthesis**  | [![docs](https://img.shields.io/badge/documentation-latest-blue.svg?style=plastic)](https://nico-curti.github.io/PhDthesis/) | **Linux** : [![travisCI](https://travis-ci.com/Nico-Curti/PhDthesis.svg?token=7QqsqaQiuDHSyGDT3xek&branch=master)](https://travis-ci.com/Nico-Curti/PhDthesis) <br/> **Windows** : *miss* |

| **Supervisor** | **Co-Supervisor** |
|:--------------:|:-----------------:|
| [**Prof. D. Remondini**](https://www.unibo.it/sitoweb/daniel.remondini) | [**Prof. G. Castellani**](https://www.unibo.it/sitoweb/gastone.castellani) <br/> [**Prof. A. Bazzani**](https://www.unibo.it/sitoweb/armando.bazzani) |

[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Nico-Curti/PhDthesis.svg?style=plastic)](https://github.com/Nico-Curti/PhDthesis/pulls)
[![GitHub issues](https://img.shields.io/github/issues/Nico-Curti/PhDthesis.svg?style=plastic)](https://github.com/Nico-Curti/PhDthesis/issues)

[![GitHub stars](https://img.shields.io/github/stars/Nico-Curti/PhDthesis.svg?label=Stars&style=social)](https://github.com/Nico-Curti/PhDthesis/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/Nico-Curti/PhDthesis.svg?label=Watch&style=social)](https://github.com/Nico-Curti/PhDthesis/watchers)

<img src="https://cdn.rawgit.com/physycom/templates/697b327d/logo_unibo.png" width="90" height="90">

# PhD Thesis

My PhD thesis in Applied Physics (a.a 2019/2020).

To compile the project you can use the [`Makefile`](https://github.com/Nico-Curti/PhDthesis/blob/master/Makefile) with the simple `make` command.
In this way all the figure into the `img` directory will be converted into a pdf_tex and the full Pdf document will be generated.

## Arguments

Different topics about Big Data Analytics are discussed in this work, starting from Feature Selection problem, passing through model deep learning Neural Network models until a novel approach to Big Data database merging via Natural Language Processing techniques.

* [Introduction on Big Data](./Introduction.md)

* [DNetPRO algorithm and Feature Selection](./md/Chapter1/README.md)
  * [DNetPRO algorithm](./md/Chapter1/DNetPRO/README.md)
  * [Synthetic dataset benchmark](./md/Chapter1/DNetPRO/ToyModel.md)
  * [Algorithm implementation](./md/Chapter1/Implementation/README.md)
    * [Combinatorial algorithm](./md/Chapter1/Implementation/Couples.md)
    * [Pair sort](./md/Chapter1/Implementation/Sorting.md)
    * [Network signature](./md/Chapter1/Implementation/FeatSel.md)
    * [DNetPRO in Python](./md/Chapter1/Implementation/Python.md)
    * [DNetPRO in Snakemake](./md/Chapter1/Implementation/Pipeline.md)
    * [Time performances](./md/Chapter1/Implementation/Timing.md)
  * [Benchmark of DNetPRO algorithm](./md/Chapter1/Synapse/README.md)
    * [Synapse dataset](./md/Chapter1/Synapse/Dataset.md)
  * [Cytokinoma dataset](./md/Chapter1/Cytokinoma/README.md)
    * [Dataset](./md/Chapter1/Cytokinoma/Dataset.md)
    * [Results](./md/Chapter1/Cytokinoma/Results.md)
  * [Bovine dataset](./md/Chapter1/Bovine/README.md)
    * [Dataset](./md/Chapter1/Bovine/Dataset.md)
    * [Results](./md/Chapter1/Bovine/Results.md)

* [Deep learning Neural Networks](./md/Chapter2/README.md)
  * [Neural Network models](./md/Chapter2/NeuralNetwork/README.md)
    * [Simple Perceptron](./md/Chapter2/NeuralNetwork/Perceptron.md)
    * [Fully Connected Neural Network](./md/Chapter2/NeuralNetwork/FullyConnected.md)
    * [Matrix Product](./md/Chapter2/NeuralNetwork/gemm.md)
    * [Activation Functions](./md/Chapter2/NeuralNetwork/Activations.md)
    * [Convolution Functions](./md/Chapter2/NeuralNetwork/Convolutional.md)
    * [Pooling function](./md/Chapter2/NeuralNetwork/Pooling.md)
    * [BatchNorm function](./md/Chapter2/NeuralNetwork/BatchNorm.md)
    * [Dropout function](./md/Chapter2/NeuralNetwork/Dropout.md)
    * [Shortcut connections](./md/Chapter2/NeuralNetwork/Shortcut.md)
    * [Pixel Shuffle](./md/Chapter2/NeuralNetwork/PixelShuffle.md)
    * [Cost function](./md/Chapter2/NeuralNetwork/Cost.md)
  * [Super Resolution](./md/Chapter2/SuperResolution/README.md)
    * [Super Resolution](./md/Chapter2/SuperResolution/README.md)
    * [Resampling](./md/Chapter2/SuperResolution/Resampling.md)
    * [Image Quality](./md/Chapter2/SuperResolution/QualityImage.md)
    * [DIV2K dataset](./md/Chapter2/SuperResolution/Dataset.md)
    * [Results](./md/Chapter2/SuperResolution/Results.md)
  * [Object Detection](./md/Chapter2/ObjectDetection/README.md)
    * [Yolo architecture](./md/Chapter2/ObjectDetection/Yolo.md)
    * [COCO dataset](./md/Chapter2/ObjectDetection/Dataset.md)
    * [Results](./md/Chapter2/ObjectDetection/Results.md)
  * [Image Segmentation](./md/Chapter2/Segmentation/README.md)
    * [U-Net model](./md/Chapter2/Segmentation/UNet.md)
    * [Femur CT Dataset](./md/Chapter2/Segmentation/Dataset.md)
    * [Results](./md/Chapter2/Segmentation/Results.md)
  * [Replicated Focusing Belief Propagation](./md/Chapter2/rFBP/README.md)
    * [Algorithm Optimization](./md/Chapter2/rFBP/Implementation.md)
    * [SNP classification](./md/Chapter2/rFBP/Dataset.md)
    * [Results](./md/Chapter2/rFBP/Results.md)


* [Biological Big Data - CHIMeRA project](./md/Chapter3/README.md)
  * [The CHIMeRA project](./md/Chapter3/CHIMeRA/README.md)

* [Conclusions](./Conclusions.md)

* Appendix:
  * [Appendix A - Discriminant Analysis](./md/Appendix/DiscriminantAnalysis/README.md)
    * [Mathematical background](./md/Appendix/DiscriminantAnalysis/MathematicalBackground.md)
    * [Numerical Implementation](./md/Appendix/DiscriminantAnalysis/Numerical.md)
  * [Appendix B - Venice Road Network](./md/Appendix/Venice/README.md)
    * [The datasets](./md/Appendix/Venice/Dataset.md)
    * [Mobility paths reconstruction on the road network](./md/Appendix/Venice/MobilityPaths.md)
  * [Appendix C - BlendNet](./md/Appendix/BlendNet/README.md)
  * [Appendix D - Multi-Class Performances](./md/Appendix/Scorer/README.md)
  * [Appendix E - Neural Network as Service](./md/Appendix/FiloBlu/README.md)
    * [FiloBlu Service](./md/Appendix/FiloBlu/Service.md)
    * [Data Transmission](./md/Appendix/FiloBlu/CryptoSocket.md)
  * [Appendix F - Bioinformatics Pipeline Profiling](./md/Appendix/Profiling/README.md)


