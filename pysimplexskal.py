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

#A = np.matrix('1 1 1 0 0; 1 0 0 1 0; 8 20 0 0 1')       #test från martin 14-17 ##
#b = np.array([1, 0.75,10])
#c = np.array([2, 1, 0, 0, 0])
#bix = np.array([3,4,5])

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

#BinVerse = np.linalg.inv(B)
#print(BinVerse)
#b = np.dot(BinVerse,b) 
#print(b)

#zcheat = np.dot(cB.transpose(),bix)  


# Start iterations
iter = 0

while iter >= 0:
    iter+=1
 
    BinVerse = np.linalg.inv(B) 

    

    # calc right-hand-sides and reduced costs
    # --------

    bHatt = np.dot(BinVerse,b)          #Steg 2 i sida 169/340
    #bix = b
    #
    # nix = 0 
                                    
    z = np.dot(cB.transpose(),bix)     #steg 3
    #print(zcheat)

    y = (np.dot(cB.transpose(),BinVerse)).transpose()         #används för reducerad kostnad
    #print(y)

    cNHatt = (cN - np.dot(N.transpose(), y))                #steg 5
    #print(cN)

    # calc most negative reduced cost, rc_min,
    # and index for entering variable, inkvar
    # --------

    rc_min = np.amin(cNHatt)                    #steg 5-6           hittat största 
    #print(rc_min)
    inkvar = np.argmin(cNHatt)            #    #steg7              kanske fel sehit med inkvar
    #inix = np.argmin(cNHatt)
    #inkvar = nix[inix]
    #print(inkvar)

    
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

        a = N[:, inkvar]                    #ksk matris? ist för vektor då print saknar punkter
        #print(a)

        if max(a) <= 0 :
            # unbounded solution
            print('Unbounded solution!')
            iter=-1
        else:
            # calc leaving var, utgvar
            # --------

        
    

            counter = 0                                                     #semaphore om multitrådar behövs
            i = 0
            print(a)
            print(bHatt)
            print("-------------------")
            while i < len(a):
                if counter > 0 and 0 <= a[i] and tempMin > bHatt[i]/a[i]:
                    tempMin = (bHatt[i]/a[i])
                    utgvar = bix[i] 
                if (counter == 0 and 0 <= a[i]):                                #b[x]/a[x]) < tempMin
                    counter = 1
                    tempMin = (bHatt[i]/a[i]) 
                    utgvar = bix[i] 
                i +=1

            print(utgvar)                                           # 3an representerar x4 ... (ty bix -1)       
            
            print(' Iter: '+repr(iter)+' z: '+repr(z)+' rc: '+repr(rc_min)+' ink: '+repr(inkvar+1)+' utg: '+repr(utgvar+1))

            # make new partition
            # --------

            print(inkvar)
            print(utgvar)
            print(nix[np.where(inkvar)])
            print(bix[np.where(utgvar)])
            nix[np.where(inkvar)] = utgvar              #bix[utix]=nix[inix]
            #bix[np.where(utgvar)] = inkvar          #steg 11 uppdaterat bix och nix


            print("teeest")
            print(nix)
            #print(bix)

            B  = A[:, bix]
            print("B kommer nedan")
            print(B)
            N  = A[:, nix]
            print(N)
            cB = c[bix]
            print(cB)
            cN = c[nix]
            print(cN)
elapsed = time.time() - t1
print('Elapsed time: '+repr(elapsed))