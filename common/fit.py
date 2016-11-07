# -*- coding: utf-8 -*-

import numpy as np
from common.colors import randomColor, namedColor
from common.wave import Wave
#from common.fitfunc import fitFunc
from scipy.optimize import curve_fit



class Fit:
  def __init__(self, xs, ys, fitFunc, p_guess, name='', pruneX=False, pruneY=False, usexerr=True, useyerr=True, ls='-', color=randomColor(), verbose=True):
    if len(xs) is not len(ys):
      print ("Length of X and Y waves did not match during Fit")      
      return -1
    self.fitFunc = fitFunc
    if (isinstance(xs, Wave)):
      self.xwave = xs
    else:
      self.xwave = Wave(xs)
    if (isinstance(ys, Wave)):
      self.ywave = ys
    else:
      self.ywave = Wave(ys)
    
    # only fit to points which are in some [low, high] range
    if pruneX:
      self.ywave = self.ywave.pruneWave(pruneX, self.xwave)
      self.xwave = self.xwave.pruneWave(pruneX, self.xwave)
    if pruneY:
      self.xwave = self.xwave.pruneWave(pruneY, self.ywave)
      self.ywave = self.ywave.pruneWave(pruneY, self.ywave)
    
    self.p_guess = p_guess
    self.linestyle = ls
    self.color = namedColor(color) if namedColor(color) else color
    self.fitxvals = np.linspace(self.xwave.min, self.xwave.max, num=250)
    self.popt, self.pcov = curve_fit(self.fitFunc.f, self.xwave.pts, self.ywave.pts, p0=p_guess)
    # if self.pcvo1 == BAD: print warning
    self.stdevs = [np.sqrt(self.pcov[ii, ii]) for ii in range(0, len(self.pcov))] # sqrt of diag elements is stdev
    self.fittedParams = dict(zip(self.fitFunc.args[1:], zip(self.popt, self.stdevs)))
    self.residuals = np.subtract(self.ywave, self.fitFunc.f(self.xwave.pts, *(self.popt)))
    # self.usedErrBars = (usexerr, useyerr)
    # TODO fit trace, fit with error bars unless requested not to
    self.name = ''
    if name:
      self.name = str(name)
    else:
      if self.xwave.name:
        self.name = 'Fit of ' + str(self.xwave.name)
        
    if verbose:
      print(self)


    
  def __repr__(self):
    retStr = self.fitFunc.name + " fit for \"" + str(self.ywave.name) + "\" as a function of \"" + str(self.ywave.name) + "\":\n"
    for p in self.fitFunc.args[1:]:
      retStr += "\t" + str(p) + "\t: " + str(self.fittedParams[p]) + "\r\n"
    return retStr
