import numpy as np

rows, columns = 3, 2;

A = np.zeros((rows,columns))
B = np.zeros((columns,rows))

print 'Please fill out matrix A to generate a secure key'
for i in range(rows):
    for j in range(columns):
        A[i][j] = j+1 #raw_input('Enter A('+str(i+1)+')('+str(j+1)+'): ')

print "\nMatrix A"
print A

print 'Please fill out matrix B'
for i in range(columns):
    for j in range(rows):
        B[i][j] = raw_input('Enter B('+str(i+1)+')('+str(j+1)+'): ')
        
print "\nMatrix B"
print B

print "\n"
print np.matrix(A)*np.matrix(B)

print "\n"
print B[:, 0]