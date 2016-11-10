# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import numbers
from thompsonlib.common.colors import randomColor



def removeByIndex(pts, listOfIndices):
  return np.delete(pts, listOfIndices)

class Wave:
  def __init__(self, pts, errbars=[], name='', x0=0, deltax=1, clist=[]):
    if isinstance(pts, Wave):
      return pts
    self.pts = np.array(pts)
    self.name = name
    if (len(errbars) == len(pts)) or (len(errbars) == 0):
      self.errbars = np.array(errbars)
    else:
      print("Number of error bars (%d) did not match number of points (%d). Wave Created with no error bars." % (len(errbars), len(self.pts)))
      self.errbars = np.array([])
    self.waveStats()
    self.x0 = x0
    self.deltax = 1
    if isinstance(clist, Wave):
      self.clist = clist.pts
    else:
      self.clist = clist

    
  def waveStats(self):
    if len(self.pts) == 0:
      self.mean = 0
      self.std = 0
      self.var = 0
      self.max = 0
      self.min = 0
      return
    self.mean = np.mean(self.pts)
    self.std = np.std(self.pts)
    self.var = np.var(self.pts)
    self.max = np.max(self.pts)
    self.min = np.min(self.pts)


  # set errorbars
  def setErrs(self, errbars=[]):
    if (len(errbars) == len(self.pts)) or (len(errbars) == 0):
      self.errbars = np.array(errbars)
    else:
      print("Number of error bars (%d) did not match number of points (%d). Wave Created with no error bars." % (len(errbars), len(self.pts)))
      self.errbars = np.array([])
   
   
  # set x-axis scaling from floats or from a wave
  def setScaling(self, wave=None, x0=0, deltax=1):
    if (wave):
      self.x0 = wave.x0
      self.deltax = wave.deltax
    else:
      self.x0 = x0
      self.deltax = deltax
      
      
  # return wave from x-axis scaling information
  def getScalingWave(self):
    newName = 'x-axis scaling of ' + str(self.name)
    return Wave(pts=[self.x0 + self.deltax*ii for ii in range(0, len(self))], name=newName)
      
      
      
  def pruneWave(self, conditions, judgeWave=None):
    if (len(conditions) is not 2) or (conditions[0] > conditions[1]):
      print("'conditions' should be of the form [low, high]")      
      return self
    (low, high) = conditions
    if judgeWave is None:
      judgeWave = self
    if len(judgeWave) is not len(self):
      print ("Cannot prune wave based on judgeWave of different length")
      return self
    badindices = []    
    for ii in range(0, len(judgeWave.pts)):
      if ((judgeWave.pts[ii] < low) or (judgeWave.pts[ii] > high)):
        badindices.append(ii)
    newpts = removeByIndex(self.pts, badindices)
    newerrbars = removeByIndex(self.errbars, badindices)
    return Wave(newpts, name=self.name, errbars=newerrbars)
     
  # intentionally do not pollute this with extra options
  # potentially add in errorbars.
  def plot(self, ls='none', ms='o'):
    plt.close()
    fig = plt.figure(facecolor="#e5e5e5", figsize=(5, 3), dpi=80)
    ax1 = fig.add_subplot(111)
    ax1.set_axisbelow(True)    
    plt.rc('font', **{'family':'serif'})
    params = {'backend': 'pdf', 'axes.labelsize': 14, 'font.size': 12, 'text.usetex': False}
    plt.rcParams.update(params)   
    ax1.plot(self.getScalingWave(), self.pts,
             linestyle=ls,
             marker=ms, 
             color=randomColor(),
             markeredgewidth=True,
             alpha=0.8)         
    ax1.set_title(self.name, y=1.03)
    ax1.grid(b=True, which='major', color='#cccccc', linestyle='-')
    ax1.grid(b=True, which='minor', color='#e5e5e5', linestyle='--')
    plt.tight_layout()
    plt.show()
    return None
     
     
     
     
     
     
  ''' Overriding and overloading functions '''     
  def __sub__(self, a):
    if isinstance(a, numbers.Number):
      return Wave(self.pts - a, errbars=self.errbars, name=self.name, x0=self.x0, deltax=self.deltax)
    elif isinstance(a, Wave):
      if (len(self.pts) == len(a.pts)):
        if (len(self.errbars) == len(a.errbars)):
          return Wave(np.subtract(self.pts, a.pts), np.add(self.errbars, a.errbars), x0=self.x0, deltax=self.deltax)
        else:
          return Wave(np.subtract(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax)
      else:
        print("Can't subtract waves with different number of points")
    return Wave([])
        
  def __add__(self, a):
    if isinstance(a, numbers.Number):
      return Wave(self.pts + a, errbars=self.errbars, name=self.name, x0=self.x0, deltax=self.deltax)
    elif isinstance(a, Wave):
      if (len(self.pts) == len(a.pts)):
        if (len(self.errbars) == len(a.errbars)):
          return Wave(np.add(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax) # TODO error propagation
        else:
          return Wave(np.add(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax)
      else:
        print("Can't add waves with different number of points")
    return Wave([])
        
  def __mul__(self, a):
    if isinstance(a, numbers.Number):
      return Wave(self.pts * a, errbars=self.errbars * a, name=self.name, x0=self.x0, deltax=self.deltax)
    elif isinstance(a, Wave):
      if (len(self.pts) == len(a.pts)):
        if (len(self.errbars) == len(a.errbars)):
          return Wave(np.multiply(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax) # TODO: error propagation
        else:
          return Wave(np.multiply(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax)
      else:
        print("Can't multiply waves with different number of points")
    return Wave([])
        
  def __pow__(self, a):
    if isinstance(a, numbers.Number):
      return Wave(np.pow(self.pts, a), errbars=[], name=self.name, x0=self.x0, deltax=self.deltax)
    elif isinstance(a, Wave):
      print("Pow() is not implemented for Waves")
    return Wave([])
        
  def __truediv__(self, a):
    if isinstance(a, numbers.Number):
      return Wave(self.pts / a, errbars=self.errbars / a, name=self.name, x0=self.x0, deltax=self.deltax)
    elif isinstance(a, Wave):
      if (len(self.pts) == len(a.pts)):
        if (len(self.errbars) == len(a.errbars)):
          return Wave(np.divide(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax) # TODO: error propagation
        else:
          return Wave(np.divide(self.pts, a.pts), [], x0=self.x0, deltax=self.deltax)
      else:
        print("Can't divide waves with different number of points")
    return Wave([])
  
  def __radd__(self, a):
    return self + a
  def __rsub__(self, a):
    return (-1 * self) + a
  def __rmul__(self, a):
    return self * a
  def __rtruediv__(self, a):
    if isinstance(a, numbers.Number):
      return Wave(a / self.pts, errbars=a / self.errbars)
    print("Error with Wave division...")
    return Wave([])

  def __len__(self):
    return len(self.pts)
  def __repr__(self):
    return str(self.pts)
  def __getitem__(self, index):
    return self.pts[index]
