import matplotlib.pyplot as plt
import numpy as np
import glob # for finding files
from scipy.optimize  import curve_fit
import os


"""
This program watches a data folder that labview is adding data to.  If a file is
added, it runs some code, and makes some plots.  
"""




data_folder = "DataAnalysis.practice"
f_names = glob.glob(data_folder + '*.tsv')
dt = .02 #ms

FIT = True

""" Set up the graph.  Uses some info from the first data set """

def init_graphs(f_name, dt):
    plt.close()
    fig = plt.figure()
    dataarray = np.array(np.transpose(np.loadtxt(f_name,skiprows=0)))
    AI0 = dataarray[15]    
    dat=[0, 1]
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax1.set_xlim([0,dt*len(AI0)])
    ax1.set_ylim([1.1*np.min(AI0),2*np.max(AI0)])
    
    ax2.set_xlim([0,100])
    ax2.set_ylim([0,.001])
    
    ln1, = ax1.plot(dat)
    ln_fit, = ax1.plot(dat)
    
    ln_persist, = ax2.plot(dat, 'ko')
    plt.ion()
    plt.show()  
    return ln1, ln_fit, ln_persist
    


# p = [A, x0, w]
def sample_fit(x, a, b):
    return a*x + b

def do_fit(trace, dt):
    y_vals = trace
    x_vals = dt*np.arange(len(trace))
    p_guess = [.01, .01]
    popt, pcov = curve_fit(sample_fit, x_vals, y_vals, p0 = p_guess)

    return popt
    
    

""" Load in the data, and plot it """

def process_trace(f_name, ln1, ln_fit, dt):
    dataarray = np.array(np.transpose(np.loadtxt(last_file)))
    AI0 = dataarray[15]
    times = dt*np.arange(len(AI0))
    popt = do_fit(AI0, dt)
    
    ln1.set_xdata(times)    
    ln1.set_ydata(AI0)
    print popt
    ln_fit.set_xdata(times)
    ln_fit.set_ydata(sample_fit(times, *popt))
    return popt[0], popt[1]

""" saves the persistant data as a csv file """
def save_data(a_s, b_s):
    data_array = np.transpose(np.asarray([a_s, b_s]))
    np.savetxt(data_folder+'things.csv', data_array, delimiter = ',', )


""" Watch for new files in the data folder """
a_s = []  # track some persistant parameter
b_s = []
plt.close()
print 'running'
while True:
    plt.pause(.1)
    current_files = glob.glob(data_folder + '*.txt')
    if current_files != f_names:
        last_file = current_files[-1]

        file_ok = False
        if os.path.exists(last_file):
            try:
                os.rename(last_file, last_file)
                file_ok = True
            except OSError as e:
                print 'Access-error on file "' + last_file + '"! \n' + str(e)
        if file_ok:
            # if this is the first run, set up the graph
            if not 'ln1' in vars():
                ln1, ln_fit, ln_persist = init_graphs(last_file, dt)
            a, b = process_trace(last_file, ln1, ln_fit, dt)
            a_s.append(a)
            b_s.append(b)
            
            ln_persist.set_ydata(a_s)
            ln_persist.set_xdata(range(len(a_s)))
            f_names = current_files


        