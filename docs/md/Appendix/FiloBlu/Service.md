## FiloBlu Service

In the *FiloBlu* project we have a stream of data provided by an external App that are stored in a central database server.
The Machine Learning service has to read the information in the database, to process them and finally write the results in the same database.
All these operations have to be performed with high frequency since the result of the algorithm are shown in a real-time application.
This frequency will be the clock-time of the process function, i.e at each time interval (as small as we like) the process task will be called and we have the desired results in output.
At the same time we have to be care of the time required by our Machine Learning algorithm: not all the algorithms can process data in real time and the process function frequency has to be less than the time required by the algorithm or we can lose some frequency clock.

The best efficiency by a service can be obtained splitting as much as possible the required functionality in small-and-easy tasks.
Small task can evaluated as independent functions with an associated frequency that in this case can be reduced as much as possible.
The *FiloBlu* required functionality can be reviewed as a sequence of 3 fundamental steps and other 2 optional ones: read the data from the database, process the data with the Machine Learning algorithm and write the obtained results on the database are certainly the fundamental ones; update the Machine Learning model and clear old log files are optional steps.
To further improve the efficiency of the service we can give each independent step to a different thread.
The whole set of tasks will be piloted by a master thread given by the service itself.
In this way the service will be computational efficient and moreover it does not weight on the computer performances.
We have always take in mind that the computer which host the service have to be effected by the daemon process as less as possible either in memory either on computational point-of-view.
Now we only have to synchronize our steps with appropriate clock frequencies.

Let's start from the reading data function.
Since our data are assumed to be stored in a database this function have to perform a simple query and extract the latest data inserted.
Obviously the efficiency of the step is based on the efficiency of the chosen query.
The data extracted will be saved in a common container shared between the list of thread and thus belonging to the master.
The choice of an appropriate shared container is a second point to carefully take in mind.
This container should be light an thread-safe to avoid thread concurrency.
While the second request is implementation dependent the first one can be faced on using a `FIFO` container [^1].
In this way we can ensure that the application will saved a fixed maximum of data and it will not occupy large portion of memory (RAM).

The second task is identified by the Machine Learning function which process the data.
The algorithm will take from the FIFO container of the previous step (if there is) and it will save the result in a second FIFO container for the next step.
The time frequency of the step is given by the time required by the Machine Learning algorithm.

The third step will keep the data from the FIFO container of results (if there is) and it performs a second query (a writing one in this case) to the database.
Also in this case the frequency is given by the efficiency of the chosen query.

The last two steps can be executed without press time requirements and are useful only on a large time scale.

Each step perform its independent logging on a single shared file.
If an error occurs the service logs the message and save the current log-file in a different location to prevent possible log-cleaning (optional step).
Then the service will be re-started.

We implemented this type of service in pure Python [[FiloBluService](https://github.com/Nico-Curti/FiloBluService)].
The developed service was customize according to the server requirements of the project [^2].
We chose the Python language either for its simplicity in the code writing either for its thread native module which ensures a total thread-safety of each variable.
Using simple decorator we are able to run each function in a separate-detached thread as required by the previous instructions.
The project includes a documentation about its use (also in general applications) and it can be easily installed via `setup`.
In the *FiloBlu* project we use a Neural Network algorithm written in `Tensorflow`.
`Tensorflow` does not allow to run background process directly so the problem was overcame using a direct call to a Python script which perform full list of steps into an infinite loop.
In this way the service can be re-started also if the process-service is killed.
The service can be driven using a simple [`Powershell`](https://github.com/Nico-Curti/FiloBluService/blob/master/filobluservice.ps1) script provided in the project.


[^1]: FIFO container, i.e *First-In-First-Out*, is a special data structure in which the first element added will be processed as first and then automatically removed from it.

[^2]: The FiloBlu service is a Windows service and it can not run on Unix machines. Moreover the database used in the project is a MySQL one so the queries and the libraries used are compatible only with this kind of databases.

[**next >>**](./CryptoSocket.md)