import numpy as np


rows = int(raw_input('Enter # of A matrix rows: '));
columns = int(raw_input('Enter # of A matrix columns: '));

A = np.zeros((rows,columns))
B = np.zeros((columns,rows))

print 'Please fill out matrix A to generate a secure key'
for i in range(rows):
    for j in range(columns):
        A[i][j] = raw_input('Enter A('+str(i+1)+')('+str(j+1)+'): ')

print 'Please fill out matrix B'
for i in range(columns):
    for j in range(rows):
        B[i][j] = raw_input('Enter B('+str(i+1)+')('+str(j+1)+'): ')

print "\nMatrix A"
print A

print "\nMatrix B"
print B

matrixResult = np.matrix(A)*np.matrix(B)
print "\nMultiplication result"
print matrixResult
print "\n"
print 'The first vector of the result matrix'
v1 = matrixResult[:, 0]
print v1

v1_sum = sum(v1)

print 'Sum of the first vector: '+str(v1_sum)