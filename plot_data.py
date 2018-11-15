import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

def normalization(k,n,thefile): 
    """Normalization of the curve"""
    mm = np.zeros((k,n))
    x = thefile[:,0]
    mm[:,0] = x
    for i in range(1,n):
        #y = thefile.iloc[:,i]
        y = thefile[:,i]
        Nrml_y = y/max(y)
        [k,l]= thefile.shape
        mm[:,i] = Nrml_y
    return mm
    print(k,l,mm)
    #plt.plot(x,mm[:,1:]) 
    #plt.show()
        #plt.hold(True) 
    
    #plt.xlim(380,700)
    #plt.xlabel("Wavelength")
    #plt.ylabel("Intensity")
    
file = pd.read_excel("w_wout_lens_0.57A_980.xlsx")
file = file.as_matrix()
print(file)
[k,l] = file.shape
print(k,l)
x = file[:,0]
xa = x.shape
print(x,xa)
if __name__ == "__main__": 
    normalization(k,l,file)
