from scipy.io import mmread
from scipy.sparse import coo_matrix
import numpy as np

def read_data(path):
	#Read data from *.mtx file
	A = mmread(path)
	#Convert to array
	B = coo_matrix(A, dtype=np.float64).toarray()
	#Convert to single dimention array
	Data = B.ravel()
	return Data

path = 'venkat50.mtx'
Data = read_data(path)
n=1000 # rows number
m=1000 # columns number

np.savetxt('matrix.csv', Data[:4*m*n], delimiter = ',')

print(Data)