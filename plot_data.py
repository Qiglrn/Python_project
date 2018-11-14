import matplotlib.pyplot as plt
# matplotlib.pyplot is a collection of command style functions to make matplotlib work like MATLAB. 
# each pyplot function makes changes to the figure, like decorates the plot with labels, 
# plot some lines in the plotting area.
import math
import numpy as np
#np.set_printoptions(threshold=np.nan) # to show the whole array
# numpy is the core library for scientific computing in Python. It provides high-perfornmance multidimonesial 
# array bojects, and tools for working with these arrays. 
# plt.close("all")
import pandas as pd
# pandas stands for python data analysis library, it is a library providing high-performance,
# easy-to-use data structures and data analysis tools for the Python programming language.
# it takes data(like CSV or TSV) and creates a python project with rows and columns called data frame that looks very 
# similar to table in statistical software.
def normalization(n,thefile): 
    """Normalization of the curve"""
    for i in range(1,n):
        y = thefile.values[:,i]
        Nrml_y = y/max(y)
        plt.plot(x,Nrml_y)
        print(Nrml_y)
        #plt.hold(True) 
    return i
    #plt.xlim(380,700)
    #plt.xlabel("Wavelength")
    #plt.ylabel("Intensity")
    #plt.show()
file = pd.read_excel("w_wout_lens_0.57A_980.xlsx")
print(file)
file.as_matrix()
[k,l] = file.shape
print(k)
print(l)
print(file)
x = file.values[:,0]
if __name__ == "__main__": 
    normalization(l,file)
    