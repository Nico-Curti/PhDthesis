# Conclusions

We have concluded our trip about the applications of Big Data Analytics to Biomedical datasets.
In this work we have touched multiple and different topics related to this theme.

In the first chapter we have focused on the difficulty about information extraction analyzing high-throughput datasets.
The so-called -omics datasets are becoming a very interesting research field in biology and medicine since, using modern data acquisition techniques, they are capable to give us a wide range of useful data for the analysis of multiple diseases.
A crucial role on this topic is still given by tumors and using omic data we can design novel methods to identify those responsible for these diseases.
The amount of these data, or more in general of Biomedical Big Data, poses new challenges to the scientific research since we have to convert them into useful information or, in other words, we have to be able to identify their informative core.
To this purpose we have designed the new `DNetPRO` algorithm as novel feature selection method.

We have tried to show all the pros and cons about the proposed algorithm since before a application on real data we have always to take care (and eventually tune) about the limits of our model.
Only knowing its limits we could be able to provide a reasonable interpretation about its results.
The proposed `DNetPRO` pipeline was tailored for gene expression applications and we have shown its application comparing its efficiency against other state-of-art models in which it is able to outperform them in the major part of analyzed cases.
We have proved how it can be used also in other kind of biomedical applications and with other data sources.
All these results are also already published or they are under press.
We would remark that the `DNetPRO` could be used also as standalone feature selection algorithm, but, for sake of brevity, we have discussed its application on non-biological data only in the Appendix of this work.

In the second chapter we have moved to more numerical applications talking about the modern deep learning research field.
We have payed particular attention to the description and optimization of some state-of-art deep learning models.
In this chapter we have also introduced three new custom libraries about this topic and which have been developed with different purposes: the `NumPyNet` is essentially an educational framework for the development of neural network model while the `Byron` library is focused on the numerical performances; the `rFBP` library was designed for very particular applications and in this work we have briefly shown one.
Starting from the bases of neural network models we have discussed about different kind of functions (more or less straightforward) which are commonly involved in the construction of a deep learning neural network architecture.
For each function we have only summarily described its mathematical background focusing instead on the critical points related to its algorithmic version.

We have used the two developed libraries to highlight possible ways to overcome these numerical issues.
For sake of brevity it has not been possible to go in deeper details about the numerical improvements performed but all the developed codes have been shared and they are public available on Github.
The modern scientific research, in fact, is not made only by papers and publications but it is acquiring even more importance the code development and, thus, its public availability.
Our works about deep learning applications are not yet concluded and no papers are written about them, but sharing our codes along the Internet we want encourage the research community to take in consideration also our promising results about this topic.
We have faced on different state-of-art models and implementations of them along our discussion and in all the analyzed cases our results overcome them with not negligible results.

The results obtained using Super Resolution and Segmentation models are very promising for the analysis of biomedical images.
Moreover, we have showed as deep learning models are capable of a very efficient generalization due to the vast amount of parameters which compose the model and the well-programmed training section.
In particular, our Super Resolution models were trained on general-purpose images but they are however able to reconstruct biomedical NMR images better than standard methods.
This, already discussed, result is due to the ability of the model to identify analogous textures and patterns between the training and validation images without it needs a tailored re-train.
We have also seen how we can improve the object detection efficiency using a pre - Super Resolution - processing: we could not show biomedical results on this topic due to lack of data, but we have shown how a people-count problem (Complex System task) could be improve by it.
We are still working about the discussed image Segmentation model but we can conclude that the preliminary results obtained on this problem encourage us in using a deep learning approach to solve also this kind of task.

We would remark that our work was focused on the optimization of that codes only for CPU usages and thus we can not compare them to the wide world of GPU deep learning models.
We would, however, stress that we have intentionally chosen to focus only on these computational environments aiming to increase the usage of this kind of models also to research fields which do not need GPUs in their everyday works.
There are, in fact, a lot of scientific applications which are tailored on CPUs architecture and which are pushed out to the deep learning researches or which do not even try to use deep learning models afraid by their intensive computational demand.
We developed the `Byron` library to overcome these issues and to highlight how a well-thought-out algorithmic implementation can overcome also the more computational expensive applications.

In all our discussions a crucial role was played by the algorithm testing either in numerical stability and correctness terms either from a profiling point-of-view.
All the developed algorithms were intensively profiled against other state-of-art implementations and their pros and cons were examined in order to find the best solution for a given problem.
The code testing was performed also according to different operative systems since how well an algorithm is made, it is useless if it works only a well-defined machine.
A continuous integration of our codes has been at the basis of all the proposed libraries as much as a reliable and user-friendly code documentation.

We have concluded our discussion introducing the `CHIMeRA` project which, even though the analysis of its results is still in work in progress, gives us multiple talking points about Biomedical Big Data.
There is an increasing interest about the harmonization of databases in these years and its need is given by the growing amount of public data.
The research community is still trying to keep up with the new demand for data analysis and an increasingly important role is played by the development of new computational strategies and techniques.
Many European projects financed by the Horizon 2020 Research and Innovation program are focused on this topic and a particular attention is payed on the health-care research.

The `CHIMeRA` project could not be compared to such big research program but it is driven by the same kind of ideas.
Its final purpose, in fact, is to use the wide range of available information and results obtained by independent research studies and to combine them into a unique framework of analysis.
Observational databases differ in both purpose and design: they have been collected for different purposes and the logical organizations as much the medical terminologies can vary from source to source.
A *Common Data model* (CDM) is designed to overcome these issues and to offer a unique solution for the information storage in the same way as our `CHIMeRA` project merges together information provided by multiple on-line databases.
Unfortunately, the research community is developing a wide range of CDMs and until a single solution is taken as a standard the problem can not be solved.
Also in this case we have not developed `CHIMeRA` as putative alternative to this purpose but it is simply a temporary solution which allows us to perform a panoramic overview of biomedical compounds.

We have highlighted the multiple possible usage of the developed `CHIMeRA` network-of-networks structure and we hope it can useful as integrative tool also for biggest project like the HARMONy one.
In this work we have focused on the key steps which bring us to the idea behind the `CHIMeRA` project and moreover we have described the difficulties and their relative proposed solutions about the creation of a such network-of-networks database.
Despite the work has been intense up to now the more interesting part from a scientific point-of-view is just started.
The `CHIMeRA` database is the only "code" discussed in this work which is not yet public available due to its embryonic stage, but hopefully we can provide its first release as soon as possible.

[**next >>**](./SUMMARY.md)
