## DNetPRO in Python

Up to now we have focused on the algorithm performances, leaving out the usability of the `DNetPRO` algorithm for the (research) community.
Despite the `C++` is one of the most efficient and older programming language[^1], the number of `Python`-users is growing in the last few years.
`Python` is becoming leader in scientific research publications and the large part of Machine Learning analyses are performed using `Python` libraries (in particular `scikit-learn` library).
So, we have to reach a compromise between performances and usability of the new codes and a reasonable solution is given by the `Cython` [[behnel2010cython](https://cython.org/)] framework.

`Cython` "language"[^2] allows an easy interface between `C++` codes and `Python` language.
With a relatively simple wrapping of the `C++` functions, they can be used inside a pure `Python` code, preserving as much as possible the computational performances of a pure `C++` version.
In this way, we have written a simple `Python` object which performs the full set of `DNetPRO` steps and, moreover, which is compatible with functions provided by other machine learning libraries.

With this purposes we have chosen to operate a "double wrap" of the `C++` functions to separate as much as possible the `C++` components from `Python`[^3].
The [`Python` object](https://github.com/Nico-Curti/DNetPRO/blob/master/DNetPRO/DNetPRO.py) was written considering a full compatibility with the `scikit-learn` library to allow the use of the `DNetPRO` feature selection as an alternative component of other Machine Learning methods.


[^1]: Still in common use in scientific research groups.

[^2]: It is not a real programming language since it is based on `Python`. However it has its own syntax and keywords which are different either from `Python` either from `C++`. In the end it needs a compiler to run and it is certainly different from Python.

[^3]: `Cython` wraps are very powerful tools for `C++` integration into `Python` code but, by experience, they are difficult to manage by pure-`Python`-users. A simple workaround is to perform a first wrap of the `C++` functions inside a `Cython` object, adding a second wrap of it into a pure-`Python` class. This two-steps wrap certainly gets worse the computational performances, but it allows a complete separation between the compiled part of the code (`Cython`) and the interpreted (`Python`) one. Moreover, we can leave back all the checks on input parameters of the `C++` function since they can be performed at run time by the `Python` wrap.

[**next >>**](./Pipeline.md)
