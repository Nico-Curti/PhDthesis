## Data Transmission

In the above configuration we have focused on the pipeline which process the stream of data ignoring the problems about the communication between the external device and the machine which host the service.
The *FiloBlu* project uses an external App to send data to the main server.
So we have two systems which have to communicate between them automatically via Internet connection.
In general we could also manage sensitive data and the Internet communication could became a vulnerability in our application.
To face on this problem we developed a simple TCP/IP client-server package which also supports a RSA cryptography, the `CryptoSocket` package [[CryptoSocket](https://github.com/Nico-Curti/CryptoSocket)].

The communication security could be an important point in many research applications and a valid cryptography is essential.
The RSA cryptography is considered one of the most secure cryptography for data transmission and it is quite easy to implement.
In this package we implemented a simple wrap around the *socket* Python library to perform a serialization of our data which will be (optionally) processed by a custom [RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).
In this way different kind of data could be sent by the client at the same time.
The client script could be adapted with slight modification for any user need and also complex Python structure could be transmitted between two machines.
The cryptography module was written in pure C++ for computational efficiency and a `Cython` wrap was provided for a pure-Python application.
`CryptoSocket` has only demonstrative purpose and so it works only for a 1-by-1 data transmission (1 server and 1 client).

Since this second implementation could be used also for other applications it was treated as a separated project and it has its own open-source code.
The `CryptoSocket` package can be installed via [`CMake`](https://github.com/Nico-Curti/CryptoSocket/blob/master/CMakeLists.txt) in any platform and a full list of installation instructions is provided in the project repository.
The continuous integration of the project is guaranteed by testing the package installation across multiple C++ compilers and Unix and Windows platforms.

[**next >>**](../Profiling/README.md)
