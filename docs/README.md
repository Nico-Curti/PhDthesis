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

[comment]: # (<img src="https://cdn.rawgit.com/physycom/templates/697b327d/logo_unibo.png" width="90" height="90">)

# Implementation and optimization of algorithms in Biomedical Big Data Analytics

> Big Data Analytics poses many challenges to the research community who has to handle several computational problems related to the vast amount of data.
> An increasing interest involves Biomedical data aiming to get the so-called "personalized medicine", where therapy plans are designed on the specific genotype and phenotype of the individual patient and algorithm optimization plays a key role to this purpose.
> In this work we discuss about several topics related to Biomedical Big Data Analytics with a special attention to numerical issues and algorithmic solutions related to them.
> We introduce a novel feature selection algorithm tailored on *omics* datasets, proving its efficiency on synthetic and real high-throughput genomic datasets.
> The proposed algorithm is a supervised signature identification method based on a bottom-up combinatorial approach that exploits the discriminant power of all variable pairs.
> We tested our algorithm against other state-of-art models and it outperforms existing results or compares to them.

> We also implement and optimize different types of deep learning models, testing their efficiency on biomedical image processing tasks.
> Three customized frameworks for deep learning neural network models development are discussed and used to describe the numerical improvements proposed on the various topics.
> In the first implementation we optimize two Super Resolution models and we show their results on NMR images, proving their efficiency in generalization tasks without a retraining.
> The second optimization involves a state-of-art Object Detection neural network architecture, obtaining a significant speedup in computational performance.
> We also highlight how Super Resolution models are able to overcome object detection issues and increase detection performance.
> In the third application we discuss about femur head segmentation problem on CT images: a semi-automated pipeline for the image annotation is proposed and a deep learning neural network model trained on these images.

> The last section of this work is the implementation of a novel biomedical database obtained by the harmonization of multiple data sources that provide network-like relationship between biomedical entities.
> The data involved in this project related to diseases, symptoms and other biological relates were mined using web-scraping methods, and a novel natural language processing pipeline was designed to maximize the overlap between the different data sources.
> We describe the key steps which lead us to this network-of-networks database and we discuss its potential applications to biomedical research.

## Table of contents

* [Introduction](./md/Introduction.md)

* [DNetPRO algorithm and Feature Selection](./md/Chapter1/README.md)
  * [DNetPRO algorithm](./md/Chapter1/DNetPRO/README.md)
  * [Synthetic dataset benchmark](./md/Chapter1/DNetPRO/ToyModel.md)
  * [Algorithm implementation](./md/Chapter1/Implementation/README.md)
    * [Combinatorial algorithm](./md/Chapter1/Implementation/Couples.md)
    * [Pair sorting](./md/Chapter1/Implementation/Sorting.md)
    * [Network signature](./md/Chapter1/Implementation/FeatSel.md)
    * [DNetPRO in Python](./md/Chapter1/Implementation/Python.md)
    * [DNetPRO in Snakemake](./md/Chapter1/Implementation/Pipeline.md)
    * [Time performance](./md/Chapter1/Implementation/Timing.md)
  * [Benchmark of DNetPRO algorithm](./md/Chapter1/Synapse/README.md)
    * [Synapse dataset](./md/Chapter1/Synapse/Dataset.md)
    * [mRNA data](./md/Chapter1/Synapse/mRNA.md)
    * [miRNA and RPPA data](./md/Chapter1/Synapse/miRNA_RPPA.md)
    * [Couple ranking](./md/Chapter1/Synapse/Ranking.md)
    * [Characterization of signature overlap](./md/Chapter1/Synapse/Overlap.md)
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
    * [Resampling](./md/Chapter2/SuperResolution/Resampling.md)
    * [Image Quality](./md/Chapter2/SuperResolution/QualityImage.md)
    * [Super Resolution models](./md/Chapter2/SuperResolution/WDSR.md)
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


* [Biomedical Big Data - CHIMeRA project](./md/Chapter3/README.md)
  * [The CHIMeRA project](./md/Chapter3/CHIMeRA/README.md)
  * [How to find the data - Web Scraping](./md/Chapter3/CHIMeRA/WebScraping.md)
  * [SymptomsNet](./md/Chapter3/CHIMeRA/SymptomsNet.md)
  * [Natural Language Processing](./md/Chapter3/CHIMeRA/NLP.md)
  * [CHIMeRA datasets](./md/Chapter3/CHIMeRA/Dataset.md)
  * [CHIMeRA analyses](./md/Chapter3/CHIMeRA/Results.md)
  * [CHIMeRA as a Service](./md/Chapter3/CHIMeRA/Service.md)

* [Conclusions](./md/Conclusions.md)

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
    * [GATK-LODn pipeline](./md/Appendix/Profiling/Pipeline.md)
    * [Computational Environments](./md/Appendix/Profiling/Environment.md)
    * [Pipeline steps](./md/Appendix/Profiling/Step.md)
    * [Results](./md/Appendix/Profiling/Results.md)
    * [Conclusions](./md/Appendix/Profiling/Conclusion.md)

## License

The `Implementation and optimization of algorithms in Biomedical Big Data Analytics` document is licensed under the MIT "Expat" License. [![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/Nico-Curti/PhDthesis/blob/master/LICENSE.md)


### Acknowledgment

The authors acknowledge EU IMI2 - HARMONY Healthcare Alliance for Resourceful Medicines Offensive against Neoplasms in HematologY n. 116026, EU COMPARE COllaborative Management Platform for detection and Analyses of (Re-) emerging and foodborne outbreaks in Europe n. 643476 and EU VEO - Versatile Emerging infectious disease Observatory n. 874735 for their support on biomedical analyses.
A special thank goes to INFN Gruppo V AIM - Artificial Intelligence in Medicine, Progetto FILO-BLU Bando Lazio POR-FESR 2014-2020 LIFE2020 and EU ETN-ITN ImforFuture - Innovative training in methods for future data n. 721815 for what concern the development of machine learning and deep learning analyses show in this thesis.

### Citation

Please cite `Implementation and optimization of algorithms in Biomedical Big Data Analytics` if you use it in your research.

```tex
@misc{PhDtheis,
  author = {Nico Curti},
  title = {Implementation and optimization of algorithms in Biomedical Big Data Analytics},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://nico-curti2.gitbook.io/phd-thesis/}},
}
```
