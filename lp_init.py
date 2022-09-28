from numpy import *
import time
import sys
import scipy.io

fila=" ".join(sys.argv[1:])
fil=scipy.io.matlab.mio.find_mat_file(fila)
if fil==None:
    print('File '+repr(fila)+' does not exist')
    exit()

print('Datafile: '+repr(fil))
mat=scipy.io.loadmat(fil,squeeze_me=True)

c=mat['c']
A=mat['A']
b=mat['b']
bix=asarray(mat['bix'],dtype=int)
zcheat=mat['zcheat']
if 'xcheat' in mat:
    xcheat=mat['xcheat']
else:
    xcheat=0

bix=bix-1
[m,n] = shape(A)
print('Rows: '+repr(m)+' cols: '+repr(n))

print('c:',c)
print('b:',b)
print('A:',A)
print('bix:',bix)
print('xcheat:',xcheat)
print('zcheat:',zcheat)
