#TAOP89, willo509, oskda863
from copyreg import pickle
from multiprocessing import allow_connection_pickling
import pickle
import numpy as np
import time
import sys
import copy

e = 1
prob = " ".join(sys.argv[1:]).split('.')[0]
fil = prob+'.npz'

npzfile = np.load(fil, allow_pickle=True)
npzfile.files
m = npzfile['m']
n = npzfile['n']
s = npzfile['s']
d = npzfile['d']
f = npzfile['f']
c = (npzfile['c'])


print('m:', m, ' n:', n)
print('s:', s)
print('d:', d)
print('f:', f)
print('c:', c)

t1 = time.time()
x = np.zeros((m, n), dtype=np.int64)
y = np.zeros((m), dtype=np.int64)

ss = copy.deepcopy(s)
dd = copy.deepcopy(d)


while sum(dd) > 0:
    # find facility, find customer, send, at min cost
    # set x and y
    # deduct from ss and dd,
    # --------

    minCost = -1
    i = 0

    while i < m:                # gå igenom alla fabriker
        if ss[i] > 0:
            j = 0
            while j < n:          # gå igenom alla kunder
                if dd[j] != 0:
                    if minCost == -1:                                       # -1 för första kunden så vi kan "set minCost"
                        minCost = (e * f[i]) + (dd[j]*int(c[i][j])) + 1

                    if y[i] == 0:
                        if minCost > ((e*f[i]) + (dd[j]*int(c[i][j]))): # om fabriken måste öppnas, tas fasta kostnaden med
                            minCost = (e*f[i]) + (dd[j]*int(c[i][j]))
                            factory = i
                            customer = j
                    else:                                      
                        if minCost > (dd[j]*int(c[i][j])):  # om fabriken måste öppnas, tas fasta kostnaden inte med
                            minCost = (dd[j]*int(c[i][j]))
                            factory = i
                            customer = j
                j += 1
        i += 1

    x[factory, customer] = min(ss[factory], dd[customer])       # uppdaterar skickade enheter
    y[factory] = 1

    ss[factory] = (ss[factory] - x[factory, customer])          # uppdaterar kapacitet
    dd[customer] = (dd[customer] - x[factory, customer])        # uppdaterar efterfrågan

elapsed = time.time() - t1
print('Tid: '+str('%.4f' % elapsed))

cost = sum(sum(np.multiply(c, x))) + e*np.dot(f, y)
print('Problem:', prob, ' Totalkostnad: '+str(cost))
print('y:', y)
print('Antal byggda fabriker:', sum(y), '(av', m, ')')
