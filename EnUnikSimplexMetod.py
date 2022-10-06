from lib2to3.pgen2.token import EQUAL
from operator import index
import numpy as np
import time
import sys

#
#  How to run: python EnUnikSimplexMetod.py lab1-cloetta.npz
# 
#                             
filc=" ".join(sys.argv[1:]).split('.')[0]+'.npz'        
npzfile = np.load(filc)
c=npzfile['c']
b=npzfile['b']
A=npzfile['A']
bix=npzfile['bix']
zcheat=npzfile['zcheat']
xcheat=npzfile['xcheat']


bix=bix-1                                                                                 
t1=time.time()
[m,n] = np.shape(A)
print ('Rows: ' +repr(m)+' cols: '+repr(n))



# Create nix
nix=np.setdiff1d(range(n), bix) 

B  = A[:, bix]
N  = A[:, nix]
cB = c[bix]
cN = c[nix]

# Start iterations
iter = 0

while iter >= 0:
    iter+=1

    BinVerse = np.linalg.inv(B) 
    

    # calc right-hand-sides and reduced costs
    # --------

    bHatt = np.dot(BinVerse,b)          #Steg 2 

    z = np.dot(cB.transpose(),bHatt)     #steg 3
    y = (np.dot(cB.transpose(),BinVerse)).transpose()         #steg 4 y skuggpriser
    cNHatt = (cN - np.dot(N.transpose(), y))                #steg 5

    # calc most negative reduced cost, rc_min,
    # and index for entering variable, inkvar
    # --------

    rc_min = np.amin(cNHatt)                    #steg 5 forts    minsta reducerande kostnaden
   
    inix = np.argmin(cNHatt)                 #steg7  
    inkvar = nix[inix]


    if rc_min >= -1.0E-12:                      #steg 6
        print ('Ready')
        iter=-1
 
        # construct solution, x, and check it
        # --------
        
        x = np.zeros((len(nix)+len(bix)))                     # create vector of right size and filled with zeros
        i = 0                                                 # counter for iterations
        indexOfPlacement = 0                                  


        while i < len(x):                                     #constructs the x vector with the corresponding value of each x[i] in x
            if i in bix:
                indexOfPlacement = np.where(bix == i)
                x[i] = bHatt[indexOfPlacement[0]]           

            i +=1


        print("z Value:  ", z)
        diffx = np.linalg.norm(x-xcheat)
        diffz = z-zcheat
        print ('xdiff: '+repr(diffx))
        print ('zdiff: '+repr(diffz))
    else:
        # calc entering column, a
        # --------
        a = np.dot(BinVerse, N[:, inix])            # Beräknar inkommande kolumn för aktuel bas, uppdaterar a

        if max(a) <= 0 :                                # ej tillåten om alla värden negativa
            # unbounded solution
            print('Unbounded solution!')
            iter=-1
        else:
            # calc leaving var, utgvar
            # --------

            counter = 0                                                     # semaphore bör behövas om multitrådar sker 
            i = 0

            while i < len(a):                                               # väljer utgående variabel där tillåtenhet behålls
                if counter > 0 and 0 < a[i] and tempMin > bHatt[i]/a[i]:
                    tempMin = (bHatt[i]/a[i])
                    utgvar = bix[i] 
                    utix = i
                if (counter == 0 and 0 < a[i]):                                
                    counter = 1
                    tempMin = (bHatt[i]/a[i]) 
                    utgvar = bix[i] 
                    utix = i
                i +=1

            print(' Iter: '+repr(iter)+' z: '+repr(z)+' rc: '+repr(rc_min)+' ink: '+repr(inkvar+1)+' utg: '+repr(utgvar+1))

            # make new partition
            # --------

            bix[utix]=nix[inix]                         #steg 11 uppdaterat bas och ickebas variabler
            nix[inix]=utgvar

            B  = A[:, bix]                      #Uppdaterar bas
            N  = A[:, nix]
            cB = c[bix]
            cN = c[nix]

elapsed = time.time() - t1
print('Elapsed time: '+repr(elapsed))