#import matplotlib.pyplot as plt
#import numpy as np
#from scipy.optimize import leastsq
#from scipy import signal
#from scipy.fftpack import fft, ifft
#from scipy.optimize  import curve_fit

#import matplotlib.gridspec as gridspec
#import colorsys # colors
#import glob # for finding files
#import matplotlib.image as mpimg
#import scipy.optimize as opt
#import pandas as pd

# from model_fit import *

####
#### Takes a set of x, y values that could be randomly ordered.  Sorts them together,
#### then bins them based on adjacency in x.  Computes mean and std's within each bin.  
#### 
####


''' Utility functions '''






def smooth_random_scan(x, y, bin_width = 10):
    if not len(x) == len(y):
        print ('Unequal length X, Y')
    else:
        sorted_x, sorted_y = zip(*sorted(zip(x, y)))    
#        mean_ys = [np.mean(sorted_y[bin_width*i:(i+1)*bin_width]) for i in range(int(np.ceil(len(sorted_y)/bin_width)))]
#        mean_xs = [np.mean(sorted_x[bin_width*i:(i+1)*bin_width]) for i in range(int(np.ceil(len(sorted_x)/bin_width)))]
#        stds = [np.std(sorted_y[bin_width*i:(i+1)*bin_width]) for i in range(int(np.ceil(len(sorted_y)/bin_width)))]/np.sqrt(bin_width)
#    return mean_xs, mean_ys, stds
    
####
#### Saves some data to a csv file using pandas dataframe.  Only works if the
#### data is a list of lists (or arrays) of equal length.  
####

def save_data(data, labels, filename):
    if not len(data) == len(labels):
        print ('incorrect number of labels')
    else:
        d = {}
        for dat, lab in zip(data, labels):
            d[lab] = dat
#    df = pd.DataFrame(d)
#    df.to_csv('filename')
        
# test code  
#data = [np.arange(20), range(20)]
#labels = ['item1', 'item2']
#save_data(data, labels, 'test.csv')
#df2 = pd.read_csv('test.csv')
#print df2

####
#### Another way of saving data, without using pandas dataframe
####
####

