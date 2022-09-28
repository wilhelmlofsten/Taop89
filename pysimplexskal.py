import numpy as np
import time
import sys

filc=" ".join(sys.argv[1:]).split('.')[0]+'.npz'
npzfile = np.load(filc)
c=npzfile['c']
b=npzfile['b']
A=npzfile['A']
bix=npzfile['bix']
zcheat=npzfile['zcheat']
xcheat=npzfile['xcheat']

A = np.matrix('1 1 1 0 0; 1 0 0 1 0; 8 20 0 0 1')       #test från martin 14-17
b = np.array([1, 0.75,10])
c = np.array([2, 1, 0, 0, 0])
bix = np.array([3,4,5])

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

BinVerse = np.linalg.inv(B)
print(BinVerse)
b = np.dot(BinVerse,b) 
print(b)

# Start iterations
iter = 0

while iter >= 0:
    iter+=1
 
    BinVerse = np.linalg.inv(B) 
    

    # calc right-hand-sides and reduced costs
    # --------

    b = np.dot(BinVerse,b)          #Steg 2 i sida 169/340
    bix = b
    nix = 0 
                                    
    zcheat = np.dot(cB.transpose(),bix)     #steg 3

    y = (np.dot(cB.transpose(),BinVerse)).transpose()         #används för reducerad kostnad

    cN = (cN - np.dot(N.transpose(), y))                #steg 5

    # calc most negative reduced cost, rc_min,
    # and index for entering variable, inkvar
    # --------

    rc_min = np.amax(cN)                    #steg 5-6           hittat största 
    inkvar = (np.argmax(cN) + 1)            #kanske ta bort +1      #steg7

    
    if rc_min >= -1.0E-12:
        print ('Ready')
        iter=-1
 
        # construct solution, x, and check it
        # --------



        diffx = np.linalg.norm(x-xcheat)
        diffz = z-zcheat
        print ('xdiff: '+repr(diffx))
        print ('zdiff: '+repr(diffz))
    else:
        # calc entering column, a
        # --------

        a = N[:, inkvar]

        if max(a) <= 0 :
            # unbounded solution
            print('Unbounded solution!')
            iter=-1
        else:
            # calc leaving var, utgvar
            # --------



            print(' Iter: '+repr(iter)+' z: '+repr(z)+' rc: '+repr(rc_min)+' ink: '+repr(inkvar+1)+' utg: '+repr(utgvar+1))

            # make new partition
            # --------


elapsed = time.time() - t1
print('Elapsed time: '+repr(elapsed))