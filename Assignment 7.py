
# coding: utf-8

# In[2]:


#[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
#y1 5 = (3+5+7)/3
#y2 4.66 = (5+7+2)/3
#y3 5.66 = (7+2+8)/3
#y4 6.66 = (2+8+10)/3
#y5 9.66 = (8+10+11)/3
#y6 28.66 = (10+11+65)/3
#y7 49.33 = (11+65+72)/3
#y8 72.66 = (65+72+81)/3
#y9 84    = (72+81+99)/3
#y10 93.33 = (81+99+100)/3
#y11 116.33 = (99+100+150)/3


import numpy as np

x = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]


def movingaverage(value, window):
    weights = np.repeat(1.0,window)/window
    ma = np.convolve(value,weights,'valid')
    return ma


YMA = movingaverage(x,3)
print(YMA)

