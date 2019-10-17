## DNetPRO in Python

Up to now we are focusing on the algorithm performances leaving out the usability of the DNetPRO algorithm for the (research) community.
Despite the C++ is one of the most efficient and old programming language[^1], the Python language users are increasing in the last few years.
Python is becoming leader in scientific research publications and the large part of Machine Learning analysis are performed using Python libraries (in particular `scikit-learn` library).
So we have to reach a compromise between the performances and usability of new developed codes and it can be reached using the `Cython` [[behnel2010cython](https://cython.org/)] framework.

Cython "language"[^2] allows an easy interface between C++ codes and Python language.
With a relatively simple wrapping of the C++ functions they can be used inside a pure Python code preserving as much as possible the computational performances of the pure C++ version.
In this way we can create a simple Python object which performs the full set of DNetPRO steps and moreover which is compatible with the functions provided by the other machine learning libraries.

With this purposes we chose to operate a double wrap of the C++ functions to separate as much as possible the C++ component from the Python one[^3].
The [Python object](https://github.com/Nico-Curti/DNetPRO/blob/master/DNetPRO/DNetPRO.py) was written considering a full compatibility with the `scikit-learn` library to allow the use of the DNetPRO feature selection as an alternative component of other Machine Learning pipelines.


[^1]: Still in common use in scientific research groups.

[^2]: It is not a real programming language since it is based on Python.
  However it has its own syntax and keywords which are different either from Python either from C++.
  In the end it needs a compiler to run and it is certainly different from Python.

[^3]: Cython wrap are very powerful tools for C++ integration into Python code but, by experience, they are difficult to manage by pure-Python users.
  A simple workaround is to perform a first wrap of the C++ function inside a Cython object and a second wrap of it into a pure-Python one.
  This two-steps wrap certainly gets worse the computational performances but it allows a complete separation between the compiled part of the code (Cython) and the interpreted (Python) one.
  Moreover we can leave back all the checks on input parameters
  in the C++ version since they will be performed at run time in the Python wrap.

[**next >>**](./Pipeline.md)
