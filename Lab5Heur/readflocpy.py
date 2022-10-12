import numpy as np
import time
import sys

from itertools import product
from math import sqrt

import gurobipy as gp
from gurobipy import GRB


pri=0

# read floc data in python for gurobi

argg=sys.argv
if len(argg)<2: 
    print('Give indata file')
    sys.exit()

fil1=sys.argv[1]
fil=fil1 + '.txt'

# read data
f = open(fil, 'r')
print('Read file '+str(fil))

# m
m = int(f.readline().strip())
print('m:'+str(m))

# n
n = int(f.readline().strip())
print('n:'+str(n))
 
# s
ss=np.zeros((m),dtype=int)
v1 = f.readline().strip()
v2=v1.split()
for i in range(m):
    ss[i]=int(v2[i])
if pri: print(ss)

# d
dd=np.zeros((n),dtype=int)
v1 = f.readline().strip()
v2=v1.split()
for i in range(n):
    dd[i]=int(v2[i])
if pri: print(dd)

# f
ff=np.zeros((m),dtype=int)
v1 = f.readline().strip()
v2=v1.split()
for i in range(m):
    ff[i]=int(v2[i])
if pri: print(ff)

# c
cc=np.zeros((m,n),dtype=int)

for i in range(m):
    v1 = f.readline().strip()
    v2=v1.split()
    for j in range(n):
        cc[i,j]=int(v2[j])

if pri: print(cc)

f.close()

# now solve with gurobi
