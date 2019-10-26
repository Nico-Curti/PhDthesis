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

<a href="https://github.com/UniboDIFABiophysics">
<div class="image">
<img src="https://cdn.rawgit.com/physycom/templates/697b327d/logo_unibo.png" width="90" height="90">
</div>
</a>

# PhD Thesis

My PhD thesis in Applied Physics (a.a 2019/2020).

To compile the project you can use the [`Makefile`](https://github.com/Nico-Curti/PhDthesis/blob/master/Makefile) with the simple `make` command.
In this way all the figure into the `img` directory will be converted into a pdf_tex and the full Pdf document will be generated.

## Arguments

Different topics about Big Data Analytics are discussed in this work, starting from Feature Selection problem, passing through model deep learning Neural Network models until a novel approach to Big Data database merging via Natural Language Processing techniques.

The on-line version of the thesis can be found on the [gitbook version](https://app.gitbook.com/@nico-curti2/s/phd-thesis) or via the [github web](https://nico-curti.github.io/PhDthesis).

* [Introduction](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/Introduction.md)

* [DNetPRO algorithm and Feature Selection](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/README.md)
  * [DNetPRO algorithm](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/DNetPRO/README.md)
  * [Synthetic dataset benchmark](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/DNetPRO/ToyModel.md)
  * [Algorithm implementation](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/README.md)
    * [Combinatorial algorithm](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/Couples.md)
    * [Pair sort](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/Sorting.md)
    * [Network signature](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/FeatSel.md)
    * [DNetPRO in Python](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/Python.md)
    * [DNetPRO in Snakemake](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/Pipeline.md)
    * [Time performances](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Implementation/Timing.md)
  * [Benchmark of DNetPRO algorithm](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Synapse/README.md)
    * [Synapse dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Synapse/Dataset.md)
    * [mRNA data](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Synapse/mRNA.md)
    * [miRNA and RPPA data](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Synapse/miRNA_RPPA.md)
    * [Couple ranking](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Synapse/Ranking.md)
    * [Characterization of signature overlap](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Synapse/Overlap.md)
  * [Cytokinoma dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Cytokinoma/README.md)
    * [Dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Cytokinoma/Dataset.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Cytokinoma/Results.md)
  * [Bovine dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Bovine/README.md)
    * [Dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Bovine/Dataset.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter1/Bovine/Results.md)

* [Deep learning Neural Networks](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/README.md)
  * [Neural Network models](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/README.md)
    * [Simple Perceptron](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Perceptron.md)
    * [Fully Connected Neural Network](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/FullyConnected.md)
    * [Matrix Product](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/gemm.md)
    * [Activation Functions](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Activations.md)
    * [Convolution Functions](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Convolutional.md)
    * [Pooling function](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Pooling.md)
    * [BatchNorm function](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/BatchNorm.md)
    * [Dropout function](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Dropout.md)
    * [Shortcut connections](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Shortcut.md)
    * [Pixel Shuffle](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/PixelShuffle.md)
    * [Cost function](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/NeuralNetwork/Cost.md)
  * [Super Resolution](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/SuperResolution/README.md)
    * [Resampling](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/SuperResolution/Resampling.md)
    * [Image Quality](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/SuperResolution/QualityImage.md)
    * [Super Resolution models](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/SuperResolution/WDSR.md)
    * [DIV2K dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/SuperResolution/Dataset.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/SuperResolution/Results.md)
  * [Object Detection](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/ObjectDetection/README.md)
    * [Yolo architecture](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/ObjectDetection/Yolo.md)
    * [COCO dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/ObjectDetection/Dataset.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/ObjectDetection/Results.md)
  * [Image Segmentation](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/Segmentation/README.md)
    * [U-Net model](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/Segmentation/UNet.md)
    * [Femur CT Dataset](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/Segmentation/Dataset.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/Segmentation/Results.md)
  * [Replicated Focusing Belief Propagation](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/rFBP/README.md)
    * [Algorithm Optimization](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/rFBP/Implementation.md)
    * [SNP classification](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/rFBP/Dataset.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter2/rFBP/Results.md)


* [Biological Big Data - CHIMeRA project](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/README.md)
  * [The CHIMeRA project](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/README.md)
  * [How to find the data - Web Scraping](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/WebScraping.md)
  * [SymptomsNet](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/SymptomsNet.md)
  * [Natural Language Processing](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/NLP.md)
  * [CHIMeRA datasets](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/Datasets.md)
  * [CHIMeRA analyes](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/Results.md)
  * [CHIMeRA as Service](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Chapter3/CHIMeRA/Service.md)

* [Conclusions](./Conclusions.md)

* Appendix:
  * [Appendix A - Discriminant Analysis](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/DiscriminantAnalysis/README.md)
    * [Mathematical background](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/DiscriminantAnalysis/MathematicalBackground.md)
    * [Numerical Implementation](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/DiscriminantAnalysis/Numerical.md)
  * [Appendix B - Venice Road Network](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Venice/README.md)
    * [The datasets](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Venice/Dataset.md)
    * [Mobility paths reconstruction on the road network](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Venice/MobilityPaths.md)
  * [Appendix C - BlendNet](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/BlendNet/README.md)
  * [Appendix D - Multi-Class Performances](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Scorer/README.md)
  * [Appendix E - Neural Network as Service](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/FiloBlu/README.md)
    * [FiloBlu Service](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/FiloBlu/Service.md)
    * [Data Transmission](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/FiloBlu/CryptoSocket.md)
  * [Appendix F - Bioinformatics Pipeline Profiling](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Profiling/README.md)
    * [GATK-LODn pipeline](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Profiling/Pipeline.md)
    * [Computational Environments](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Profiling/Environment.md)
    * [Pipeline steps](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Profiling/Step.md)
    * [Results](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Profiling/Results.md)
    * [Conclusions](https://github.com/Nico-Curti/PhDthesis/blob/master/docs/md/Appendix/Profiling/Conclusion.md)


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
  howpublished = {\url{https://github.com/Nico-Curti/PhDthesis}},
}
```


