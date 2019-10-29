## Algorithm implementation

The `DNetPRO` algorithm is made by a sequence of different steps which have to be performed sequentially for a signature extraction.
For this purpose each step can be optimized independently using the full set of available computational resources[^1].
In this section will be analyzed each part of the pipeline focusing on the optimization strategies used for the algorithm implementation.

The full code is open source and available at [[DNetPRO](https://github.com/Nico-Curti/DNetPRO)].
The code installation is automatically tested using [`travis`](https://github.com/Nico-Curti/DNetPRO/blob/master/.travis.yml
) (for Linux and MacOS environments) and [`appveyor`](https://github.com/Nico-Curti/DNetPRO/blob/master/appveyor.yml) (for Windows environments) at every commit.
The installation can be performed using [`CMake`](https://github.com/Nico-Curti/DNetPRO/blob/master/CMakeLists.txt) and a full set of installation instructions can be found in the on-line project documentation.

The `Python` version of the algorithm (see next sections) can be installed via [`setup.py`](https://github.com/Nico-Curti/DNetPRO/blob/master/setup.py) and the compilable parts of it checked via `CMake`.
The `Python` installer provides also the full list of dependencies of the project which will be automatically installed by the main.

In the Github repository can be found also a full list of example scripts and utilities to obtain the results shown in the next sections.
The complete benchmark pipeline can be found which can be run on cluster environment using the `SnakeMake` version of it (see next section).

[^1]: Further optimization can be performed in a cross validation environment and they will be discussed later in this section.


[**next >>**](./Couples.md)
