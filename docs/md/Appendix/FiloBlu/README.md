# Appendix E
## Neural Network as Service

One of the final goals of Machine Learning is certainly the process automation.
We develop everyday complex models to perform tasks that should be automatically executed by a computer without human supervision.
Neural Networks are classical mathematical tools used for these purposes and we have widely discussed about them in Chapter [2](../../Chapter2/README.md) of this work.
Beyond Neural Network structures and purposes for which they are made there is still an uncovered topic to discuss: the automation of these kind of algorithms into a computer device.
In this section we are going to discuss an implementation of these algorithms as service in a computer server.
In particular we will talk about the implementation of the *FiloBlu* service which is part of a project developed in collaboration with the Sapienza University (Rome) and the INFN Data Center CNAF of Bologna.
This work is still in progress and its purpose goes beyond the current topic, so we will focus only on the implementation of the service without any reference on the Machine Learning algorithm used.
This is a further proof that the developed techniques are totally independent by the final application purpose.

A service is a software that is executed in background in a machine.
In Unix machines it is often call `daemon`s, while in Windows machine is called *Windows service*.
A service starts only with administrator privileges and it goes on without any user presence.
An other important requirement is the ability to restart when some troubles occur in the machine functionality and/or at the boot of the machine.

A Machine Learning service could be used for applications in which we have to manage an asynchronous stream of data for long time intervals.
An example could be the case in which the data provider is identified by an App or a video-camera
These data should be stored inside a central database that can be located in a different device or in the same computer in which the service run.
Since the service runs in background the only communication channel with the user is given by log files.
A log file is a simple readable file in which are saved the base information about the current status of the service.
Thus, it is crucial to set appropriated check-points into the service script and chose the minimum quantity of information that the service should write to make user-understandable its status.

[**next >>**](./Service.md)