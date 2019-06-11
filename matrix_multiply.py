from pyspark.mllib.linalg import Matrices
from pyspark.mllib.linalg.distributed import BlockMatrix
from scipy.io import mmread
from scipy.sparse import coo_matrix
import numpy as np
from pyspark import SparkContext
from pyspark.sql import SparkSession
from scipy.sparse import coo_matrix
from tensorflow.python.lib.io import file_io
import sys
import time

sc =SparkContext()
rdd = sc.parallelize([("a", 1)])
spark = SparkSession(sc)
hasattr(rdd, "toDF")

def read_data(path):
	#Read data from *.mtx file
	with file_io.FileIO(path, mode ='r') as f:
	 	Data = f.readlines()
	return Data

path = sys.argv[1]
#path = 'gs://dataproc-3848bc98-5d0f-4c2b-adb1-e09149aa21eb-europe-north1/matrix.txt'
Data = read_data(path)

n = int(sys.argv[2])
#n=500 # rows number
m = int(sys.argv[3])
#m=1000 # columns number
loop = int(sys.argv[4])

start = time.time()
for i in range(loop):
	dm1 = Matrices.dense(n, m, Data[:n*m])
	dm2 = Matrices.dense(n, m, Data[n*m:2*n*m])
	dm3 = Matrices.dense(m, n, Data[2*n*m:3*n*m])
	dm4 = Matrices.dense(m, n, Data[3*n*m:4*n*m])

	blocks1 = sc.parallelize([((0, 0), dm1), ((0, 1), dm2)])
	blocks2 = sc.parallelize([((0, 0), dm3), ((1, 0), dm4)])

	mat1 = BlockMatrix(blocks1, n, m)
	mat2 = BlockMatrix(blocks2, m, n)

	print(mat1.multiply(mat2).toLocalMatrix())
end = time.time()
print("Runing time:", end - start)	