# Appendix E
## Neural Network as Service


One of the final goals of Machine Learning is certainly the automation of the processes.
We develop complex models to perform tasks that can be automatically executed by a computer without human supervision.
Neural Networks are classically mathematical tools used for these purposes and was wide discussed in Chapter [2](../../Chapter2/README.md) of this work.
Beyond the Neural Network structures and purposes for which they are made there is a still uncovered topic to discuss: the automation of these kind of algorithms inside a computer device.
In this section we discuss an example of implementation of these algorithms as service in computer server.
In particular we will talk about the implementation of the *FiloBlu* service which is a project developed in collaboration with the University of Sapienza (Roma) and the INFN-CNAF of Bologna.
Since this work is still in progress and its purpose goes beyond the current topic, we will focused only on the implementation of the service without any reference on the Machine Learning algorithm used.
This is a further proof that the developed techniques are totally independent by the final application purpose.

A service is a software that is executed in background in a machine.
In Unix machines it is often call `daemon` while in Windows machine is called *Windows service*.
A service can be started only by admin users and it goes on without any user presence.
An other important requirement is the ability to re-start when some troubles occurs in the machine functionality and/or at the boot of the machine.

A Machine Learning service could be used in applications in which we have to manage an asynchronous stream of data for long time intervals.
An example could be the case which the data provider is identified by an App or a video-camera.
These data should stored inside a central database that can be located in a different device or in the same computer in which the service run.
Since the service process runs in background the only communication channel with the user is given by log files.
A log file is a simple readable file in which are saved the base informations about the current status of the service.
Thus, it is crucial to set appropriate check-points inside the service script and chose the minimum quantity of informations that the service should write to make user-understandable its status.

[**next >>**](./Service.md)