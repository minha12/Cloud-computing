# Evaluating matrix computation in LINALG [1] library of Spark on Google Cloud
----
## Abstract
> This is a report for the assignment of the Cloud Module within the Software Engineering and Cloud Computing course - WASP project. We will go through the process from setting up the Goolge Cloud to the final goal of evaluating matrix computation required by the Project 1 of the assignment. 
----
## Setup Google Cloud

In order to set up virtual machines on Google Cloud to run the experiment, there are three initial steps:

1. Enable DataProc API on Google Cloud DashBoard. Like the other tasks, the step could be configured in the Google Cloud web interface or through command lines. The web UI could be preferable for a beginner while the command line is less delay but also less intuitive.
2. The second step is creating a Bucket in Google Storage. A Bucket is a place where code and data files are uploaded. Each file or folder in the Bucket will have a URL like address which could be used for reference to other code files or loading and saving data. 
3. Creating clusters. Finally, clusters with different hardware configurations can be created. For example, in our experiment - two clusters, one has a low-profile configuration of only one master node and another one has a high-profile configuration with three nodes with more CPU power and more memory. The purpose is to see the differences between the low-profile cluster and high-profile cluster, which also implies how Cloud Computing could speed up the computation.

----
## Setting up Python environment in clusters
After creating the clusters, the master node in each cluster can be accessed by SSH. In there, we can install packages which are needed for running the python files. For example, some packages such as scipy and tensorflow were installed in the master node of each cluster in our experiments. In the SSH console, we can sync files between the node and the Bucket. The benefit of this feature is that we can modify the code files or data files directly in the console without re-uploading the files from local computer to Bucket. 

----
## Choosing data and matrix operations
The given dataset [2] has many different kinds of data from multiple applications. They are widely different in structure and size. We chose the matrix market data type since it is more suitable for loading in Python. Some of the basic matrix operations in the LINALG library of Spark has limitations of the number of rows and columns up to 65535 so that we chose a data set which has dimensions as close as this limit as possible. Our choice is a "Subsequent Computational Fluid Dynamics Problem" dataset named venkat50 which has a size of 62424 x 62424. The package is firstly pre-processed to fit with input format of Spark and to reduce the data handling time since we are focusing on evaluating the matrix computation only.

We chose two basic matrix operations to evaluate the LINALG library, they are addition and multiplication. Of course, we could pick other matrix operations with slightly changes in our test cases as well, however, the chosen ones are the most fundamental operation and they are fitted for the goal of this project which is evaluating matrix computation. The two methods are evaluated separately on the low-profile and high-profile cluster.  

----
## Submitting a job to a cluster
We have made four test cases with the two matrix operations and two cluster configurations. Each test case is submitted one-by-one as a single "job" to the cluster. For the least computational delay, it is required that the Bucket and Cluster should be in the same geographical region. While the job is running, we can monitor the process by visual tools in the web UI of the cluster. We can see here the information such as memory usage, CPU usages, YARN pending memory, network bytes, disk byte, etc. More details information could be seen via StackDrive - an intuitive monitoring interface of Google Cloud. 

>CPU usage of 3-node cluster displaying in StackDrive:

![alt text](https://github.com/minha12/Cloud-computing/blob/master/images/CPU-3-node-add.png)

----
## Result comparison
First, we compare the execution time to see how the Spark could speed up the matrix computation. We noticed that there is no significant difference between the addition and multiplication. However, when we use the high-profile cluster the execution time is significantly lower which showed that the matrix computation could be much more efficient with cloud computing.

![alt text](https://github.com/minha12/Cloud-computing/blob/master/images/Exection_time.png)

Regarding CPU usages we saw the 3-node cluster used much lesser CPU resource, however, it used more Memory. The reason is probably due to the fact that it could afford using more RAM.

![alt text](https://github.com/minha12/Cloud-computing/blob/master/images/CPU-Mem1.png)

----
## Conclusion
We have learned a lot about Cloud Computing during this assignment. We can set up the Google Cloud for our use of high-demand computation from now on. The important lesson here is to see that the Cloud Computing system is really helpful when it comes to big data and machine learning. The task which may require days to run on a local computer now can be hours or lesser with the new technology. 

With the experiment on the LINALG library of Spark, we have tried for ourself to see that the Cloud Computing works. The learning process by trial-and-error was quite fun, but in some cases, we really hoped for an official tutorial to start with. It may be too easy with someones who have already had the experience with this system, however, it could be a daunting task for beginners. 

----
## Reference
[1] https://spark.apache.org/docs/1.5.1/api/java/org/apache/spark/mllib/linalg/package-frame.html 

[2] https://sparse.tamu.edu/ 
