## Pipeline steps

The pipeline steps that have been examined are a subset of all the possible steps: we only focus on those whose computational requirements are higher and thus require the most computational power.
These steps are:

* **mapping:** takes all the reads of the subjects and maps them on the reference genome;

* **sort:** sorts the sequences based on the alignment, to improve the reconstruction steps;

* **markduplicates:** checks for read duplicates (that could be imperfections in the experimental procedures and would skew the results);

* **buildbamindex:** indexes the dataset for faster sorting;

* **indexrealigner:** realigns the created data index to the reference genome;

* **BQSR:** base quality score recalibration of the reads, to improve SNPs detection;

* **haplotypecaller:** determines the SNPs of the subject;

* **hardfilter:** removes the least significant SNPs.


The following statistics were evaluated:

* **memory per function:** estimate percentage of the total memory available to the node used for each individual step of the pipeline;

* **energy consumption:** estimated as the time taken by the step, multiplied by the number of cores used in the step and the power consumption per core (TDP divided by the available cores). As mentioned before this normalization unavoidably penalize the multi-core machines but give us a term of comparison between the different environment;

* **elapsed time:** wall time of each step.


The pipeline was tested on the patient data from the 1000 genome project with access code NA12878, sample SRR1611178.
It is referred as a Gold Standard reference dataset [Zook2014](https://www.nature.com/articles/nbt.2835).
It is generated with an Illumina HiSeq2000 platform, SeqCap EZ Human Exome Lib v3.0 library and have a 80x coverage.
As Gold Standard reference it is commonly used as benchmark of new algorithm and for our purpose can be used as valid prototype of genome.

[**next >>**](./Results.md)
