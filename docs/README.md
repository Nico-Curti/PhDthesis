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

# Implementation and optimization of algorithms in Biomedical Big Data Analytics

> The Big Data Analytics poses many challenges to the research community who has to handle several computational problems related to the vast amount of data.
> An increasing interest involves Biomedical data aiming to obtain the so-called "personalized medicine", where therapy plans are designed on the specific genotype and phenotype of the individual patient.
> The algorithm optimization plays a key role to this purpose.
> In this work we discuss about several topics related to the Biomedical Big Data Analytics with a special attention to numerical issues and algorithmic solutions related to them.
> We introduce a novel feature selection algorithm tailored on *omics* datasets, proving its efficiency on synthetic and real high-throughput genomic datasets.
> The proposed algorithm is a supervised signature identification method based on a bottom-up combinatorial approach that exploits the discriminant power of all variable pairs.
> We tested our our algorithm against other state-of-art models and it outperforms existing results or compares to them.
> We introduce, also, different kinds of deep learning models, highlighting their efficiencies on biomedical image processing tasks.
> Three custom frameworks for deep learning neural network models development are discussed and used to describe the numerical improvements proposed on the various topics.
> We show promising results about Super Resolution models on NMR images and we discuss possible improvements in the use of these models in combination with Object Detection ones.
> The image segmentation problem of femur head on CT images is discussed and the results obtained by our trained deep neural network are showed.
> The last section of this work introduce a novel biomedical database obtained by the harmonization of multiple data sources.
> The data involved in this project were mined using web-scraping pipelines and a novel natural language processing pipeline was designed to maximize the overlap between the different sources.
> We describe the key steps which bring us to the realization of this network-of-networks database and we discuss about the potential applications of it to the scientific research.

## Table of contents

* [Introduction](./md/Introduction.md)

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
  * [CHIMeRA as Service](./md/Chapter3/CHIMeRA/Service.md)

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

Thanks goes to all contributors of this project.

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
