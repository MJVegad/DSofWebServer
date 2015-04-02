import numpy as np
import scipy as sp
import scipy.stats
import math

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    print (a)
    n = len(a)
    print (n)
    m, sd = np.mean(a), scipy.stats.sem(a)
    print (m)
    print (sd)
    sd = sd * math.sqrt(n) / math.sqrt(n-1)
    print (sd)
    h = sd * scipy.stats.norm.ppf((1+confidence)/2.)
    print (h)
    return m, m-h, m+h

data = [1,2,3]
a, b, c = mean_confidence_interval(data)
print (a)
print (b)
print (c)