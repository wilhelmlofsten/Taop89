from copyreg import pickle
import pickle
import numpy as np
import time
import sys
import copy

e=1
allow_pickle = True                         #Pickle


prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'


allow_pickle = True                         #Pickle


print("prob :   ", prob)


npzfile = np.load(fil)
npzfile.files
m=npzfile['m']
n=npzfile['n']
s=npzfile['s']
d=npzfile['d']
f=npzfile['f']
c=npzfile['c']
print ('m:',m,' n:',n)
print ('s:',s)
print ('d:',d)
print ('f:',f)
print ('c:',c)

t1=time.time()
x=np.zeros((m,n),dtype=np.int)
y=np.zeros((m),dtype=np.int)

ss=copy.deepcopy(s)
dd=copy.deepcopy(d)

#while sum(dd)>0:
    # find facility, find customer, send, at min cost
    # set x and y
    # deduct from ss and dd, 
    # --------

    #simpel verision:
    #   Om ingen fabrik är öppen while loop, öppna en 

    #legit:
    # minCost = 0
        #  while 1 till i, gå igenom alla fabriker
            #if ss[i] > 0:
             #   while 1 till j, gå igenom alla personer
             #      if  dd[j] =0:
             #         if y[i] = 0:
            #              if minCost > (f[i] + dd[j]*c[i][j]) 
                #               minCost = f[i] + dd[j]*c[i][j]
                #               factory = i
                #               customer= j
                #      else:
               #        if minCost >  dd[j]*c[i][j]) 
                #               minCost = dd[j]*c[i][j]
                #               factory = i
                #               customer= j
    #
    # x[factory, customer] = min(ss[factory],dd[customer])
    # if y[factory] = 0
    #   y[factory] = 1
    # ss[factory] = ss[factory] - min(ss[factory],dd[customer])
    # dd[customer] = dd[customer] - min(ss[factory],dd[customer])
               


elapsed = time.time() - t1
print ('Tid: '+str('%.4f' % elapsed))

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print ('Problem:',prob,' Totalkostnad: '+str(cost))
print ('y:',y)
print ('Antal byggda fabriker:',sum(y),'(av',m,')')