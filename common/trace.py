# -*- coding: utf-8 -*-

from common.colors import randomColor, namedColor
from common.wave import Wave
from common.fit import Fit
from copy import copy

# A Trace() is a set of an xwave and a ywave which form (x, y) scatter points
#   OR a ywave which will get automatic x points 1...N
class Trace:
  def __init__(self, w1, w2=[], plotxerr=True, plotyerr=True, ls='none', color=randomColor(), marker='o', markersize=8, cmapstr='', stroke=0.5, errbarcol=None, name=None):
    # if ys was not provided, let's make a wave of integer points.
    if len(w2) == 0:
      w2 = w1
      w1 = w2.getScalingWave()
    if (isinstance(w1, Wave)):
      self.xwave = w1
    else:
      self.xwave = Wave(w1)    
    if (isinstance(w2, Wave)):
      self.ywave = w2
    else:
      self.ywave = Wave(w2)

    self.name = str(name) if name else ''
      
    if ((ls in ['solid', 'dashed', 'dashdot', 'dotted', '-', '--', '-.', ':']) and marker is None):
      self.type = 'line'
      self.linestyle = ls
      self.marker = None
    else:
      self.type = 'scatter'
      self.linestyle = ls
      self.marker = 'o'
    self.stroke = stroke if stroke else 0
    self.markersize = markersize # marker size    
    
    self.color = namedColor(color) if namedColor(color) else color
    self.cmapstr = cmapstr
    
    self.plotxerr = True
    self.plotyerr = True
    if errbarcol is not None:
      self.errbarcol = namedColor(errbarcol) if namedColor(errbarcol) else errbarcol
    else:
      self.errbarcol = self.color


  # quickly add a fit based on corresponding x and y waves
  def addFit(self, fitFunc, params, pruneX=False, pruneY=False, usexerr=True, useyerr=True, ls='-', color=randomColor(), verbose=True):
    return Fit(self.xwave, self.ywave, fitFunc, params, pruneX=pruneX, pruneY=pruneY, usexerr=usexerr, useyerr=useyerr, ls=ls, color=color, verbose=verbose)

    
  # enable/disable plotting error bars if they have been set within the waves
  def plotErrorbars(self, plotxerr=True, plotyerr=True, color=None):
    self.plotxerr = plotxerr
    self.plotyerr = plotyerr
    if color is not None:
      self.errbarcol = namedColor(color) if namedColor(color) else color

  # sort x and y wave by x wave values
  # is it useful to be able to sort based on a different wave?? 
  def sort(self):
    sortedxwave, sortedywave = (list(x) for x in zip(*sorted(zip(self.xwave.pts, self.ywave.pts))))
    self.xwave = copy(self.xwave)
    self.xwave.pts = sortedxwave
    self.ywave = copy(self.ywave)
    self.ywave.pts = sortedywave
  
  
  def __len__(self):
    return len(self.xwave)
    
  def __repr__(self):
    return "To do: implement something for printing Traces?"

  def __getitem__(self, index):
    return (self.xwave[index], self.ywave[index])
