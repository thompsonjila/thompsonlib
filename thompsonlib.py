# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:50:32 2016
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from common.fitfunc import FitFunc
from thompsonlib.common.fitfunc import *
from thompsonlib.common.wave import Wave
from thompsonlib.common.trace import Trace
from thompsonlib.common.line import Line
from thompsonlib.common.fit import Fit
from thompsonlib.common.dataset import *
from thompsonlib.common.colors import randomColor





''' Plotting library '''
              
plt.rc('font', **{'family':'serif'}) # could change the way eg texttt is rendered
params = {'backend': 'pdf',
      'axes.labelsize': 14,
      'font.size': 14,
      'text.usetex': False,
      'axes.xmargin': 0.03,
      'axes.ymargin': 0.03,
      'legend.numpoints': 1,
      'legend.scatterpoints': 1,
      'legend.framealpha': 0.7,
      'legend.labelspacing': .35,
      'legend.handlelength': 1.2
      }
plt.rcParams.update(params)   




def Plot(listOfTraces, title='', xlabel='', ylabel='', xlog=False, ylog=False, xlim=None, ylim=None, gridlines=True, legend=("best", []), fc='white', fs=(10, 7), dpi=160, show=True):
  if (isinstance(listOfTraces, Trace) or isinstance(listOfTraces, Fit) or isinstance(listOfTraces, Line)):
    listOfTraces = [listOfTraces]
  elif (isinstance(listOfTraces, Wave)):
    listOfTraces = [Trace(listOfTraces)]
  plt.close()
  fig = plt.figure(facecolor=fc, figsize=fs, dpi=dpi)
  if gridlines==True:
    plt.grid(b=True, which='major', color='#cccccc', linestyle='-')
    plt.grid(b=True, which='minor', color='#e5e5e5', linestyle='--')

  ax1 = fig.add_subplot(111)
  ax1.set_axisbelow(True)

  # log plots  
  if (xlog):
    ax1.set_xscale("log", nonposy='clip')  
  if (ylog):
    ax1.set_yscale("log", nonposx='clip')
  
  # manual limits (can we easily set autoscale from 0, etc?)
  if (xlim):  
    ax1.set_xlim(xlim)
  if (ylim):
    ax1.set_ylim(ylim)

  # plot all traces, fits, and error bars
  for trace in listOfTraces:
    if type(trace) is Wave:
      trace = Trace(trace) # convert lone waves to x,y traces
    
    # Fits are always plotted as lines
    if type(trace) is Fit:
      ax1.plot(trace.fitxvals, trace.fitFunc.f(trace.fitxvals, *(trace.popt)), linestyle=trace.linestyle, color=trace.color, label=trace.name)
    elif type(trace) is Trace:
      if (trace.type is 'line'): # lines MUST be plotted with 'plot'
        ax1.plot(trace.xwave.pts, trace.ywave.pts,
                 ls=trace.linestyle,
                 color=trace.color,
                 label=trace.name)
      else: # markers or markers with connecting line
        if trace.cmapstr: # has colormap, we must use scatter()?
          plt.set_cmap(plt.get_cmap(trace.cmapstr))
          ax1.scatter(trace.xwave.pts, trace.ywave.pts,
                      s=(trace.markersize)**2,
                      color='#000000',
                      c=trace.ywave.clist,
                      cmap=plt.cm.plasma,
                      alpha=0.8,
                      linewidth=0.50,
                      label=trace.name)
        else:
          ax1.plot(trace.xwave.pts, trace.ywave.pts,
                   ls=trace.linestyle,
                   marker=trace.marker, 
                   markersize=trace.markersize,
                   markeredgewidth=trace.stroke,
                   color=trace.color,
                   alpha=0.8,
                   label=trace.name)
        
      if ((len(trace.xwave.errbars) > 0 and trace.plotxerr) and (len(trace.ywave.errbars) > 0 and trace.plotyerr)):
        ax1.errorbar(trace.xwave.pts, trace.ywave.pts, xerr=trace.xwave.errbars, yerr=trace.ywave.errbars, fmt='none', ecolor=trace.errbarcol)
      elif (len(trace.xwave.errbars) > 0 and trace.plotxerr):
        ax1.errorbar(trace.xwave.pts, trace.ywave.pts, xerr=trace.xwave.errbars, fmt='none', ecolor=trace.errbarcol)
      elif (len(trace.ywave.errbars) > 0 and trace.plotyerr):
        ax1.errorbar(trace.xwave.pts, trace.ywave.pts, xerr=trace.xwave.errbars, fmt='none', ecolor=trace.errbarcol)
    # else: plot Lines in a moment
  
  # plot all Lines
  xmin, xmax = ax1.get_xlim()
  ymin, ymax = ax1.get_ylim()
  for trace in listOfTraces:
    if type(trace) is Line:
      if trace.vert == True:
        ax1.plot((trace.p, trace.p), (ymin, ymax), linestyle=trace.ls, color=trace.color, label=trace.name)
      else:
        ax1.plot((xmin, xmax), (trace.p, trace.p), linestyle=trace.ls, color=trace.color, label=trace.name)
    # else give error
  
  # set labels, title
  ax1.set_xlabel(xlabel)
  ax1.set_ylabel(ylabel)
  plt.title(title)
  if len(listOfTraces) == 1:
    if not title:
      plt.title(listOfTraces[0].name)
    if not xlabel:
      ax1.set_xlabel(listOfTraces[0].xwave.name)
    if not ylabel:
      ax1.set_ylabel(listOfTraces[0].ywave.name)
  
  # set legend
  if legend: 
    legendposition, excludelist = legend
    handles, labels = ax1.get_legend_handles_labels()
    if handles:
      thelegend = ax1.legend(loc=legendposition)  
      if thelegend:
        frame = thelegend.get_frame()
        frame.set_facecolor('0.95')
        for l in thelegend.get_texts():
          l.set_fontsize('small')
        for l in thelegend.get_lines():
          l.set_linewidth(1.5)  # the legend line width
  
 #  plt.ion()
  plt.tight_layout()
  if show:
    plt.show()  
    plt.close()
    return
  else:
    return plt
