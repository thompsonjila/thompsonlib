# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from thompsonlib.common.colors import randomColor

''' Fit function library '''


class FitFunc:
  def __init__(self, name, args, helpStr="", latexFormula=""):
    self.name = name
    self.args = args
    self.helpStr = helpStr
    self.latexFormula = latexFormula


  def help(self):
    print(self.name + " " + str(self.args) + " : " + self.helpStr + "\r\n\t" + self.latexFormula)
    
    
    
FitLine = FitFunc("Linear", ["x", "m", "b"], "", "mx + b")
def fit_linear(x, m, b):
  return m * x + b
FitLine.f = fit_linear

FitGauss = FitFunc("Gaussian", ["x", "A", "x0", "w", "y0"], "", "A \\exp(-\\frac{2 (x-x_0)^2}{w^2}) + y_0")
def fit_gauss(x, A, x0, w, y0):
  return A * np.exp(-2*((x-x0)/w)**2) + y0
FitGauss.f = fit_gauss

FitLor = FitFunc("Lorentzian", ["x", "A", "Gamma", "x0", "y0"], "", "\\frac{A}{\\pi} \\frac{\\Gamma / 2}{(x-x_0)^2 + (\\Gamma/2)^2} + y_0")
def fit_lor(x, A, Gamma, x0, y0):
  return (A/(2*np.pi)) * Gamma / ((x - x0)**2 + (Gamma/2)**2) + y0
FitLor.f = fit_lor
    
FitExp = FitFunc("Exponential", ["x", "A", "tau", "x0", "y0"], "", "A \\exp(-\\frac{x-x_0}{\\tau}) + y_0")
def fit_exp(x, A, tau, x0, y0):
  return A * np.exp(-(x-x0)/tau) + y0
FitExp.f = fit_exp
    
FitDblExp = FitFunc("Double Exp.", ["x", "A1", "tau1", "A2", "tau2", "x0", "y0"], "", "A_1 \\exp(-\\frac{x-x_0}{\\tau_1}) + A_2 \\exp(-\\frac{x-x_0}{\\tau_2}) + y_0")
def fit_dblexp(x, A1, tau1, A2, tau2, x0, y0):
  return A1 * np.exp(-(x-x0)/tau1) + A2 * np.exp(-(x-x0)/tau2) + y0
FitDblExp.f = fit_dblexp
    
FitSin = FitFunc("Sin", ["x", "A", "f", "phi", "y0"], "use radians", "A \\sin(f x + \\phi) + y_0")
def fit_sin(x, A, f, phi, y0):
  return A * np.sin(f*x + phi) + y0
FitSin.f = fit_sin
    
FitCos = FitFunc("Cos", ["x", "A", "f", "phi", "y0"], "use radians", "A \\cos(f x + \\phi) + y_0")
def fit_cos(x, A, f, phi, y0):
  return A * np.cos(f*x + phi) + y0
FitCos.f = fit_cos
    
FitHill = FitFunc("Hill Equation", ["x", "maximum", "xhalf", "rate", "y0"], "", "\\frac{maximum-y_0}{1 + (xhalf/x)^{rate}} + y_0")
def fit_hill(x, maximum, xhalf, rate, y0):
  return y0 + (maximum-y0)/(1 + (xhalf/x)**rate)
FitHill.f = fit_hill

FitSigmoid = FitFunc("Sigmoid", ["x", "maximum", "xhalf", "rate", "y0"], "", "\\frac{maximum}{1 + \\exp(\\frac{xhalf - x}{rate})} + y_0")
def fit_sigmoid(x, maximum, xhalf, rate, y0):
  return y0 + maximum / (1 + np.exp((xhalf-x)/rate))
FitSigmoid.f = fit_sigmoid
    
FitPow = FitFunc("Power", ["x", "A", "pow", "y0"], "", "A x^{pow} + y_0")
def fit_pow(x, A, power, y0):
  return A * x**power + y0
FitPow.f = fit_pow
    
FitLogNormal = FitFunc("Log Normal", ["x", "A", "x0", "w", "y0"], "", "A \\exp(- \\frac{\\ln(x/x_0)^2}{w^2} ) + y_0")
def fit_logNormal(x, A, x0, w, y0):
  return A * np.exp(-(np.log(x / x0) / w)**2) + y0
FitLogNormal.f = fit_logNormal

    
class AllFits:  
  def __init__(self):
    self.Fits = []
    self.Fits.append(FitLine)    
    self.Fits.append(FitGauss)    
    self.Fits.append(FitLor)
    self.Fits.append(FitExp)
    self.Fits.append(FitDblExp)
    self.Fits.append(FitSin)
    self.Fits.append(FitCos)
    self.Fits.append(FitHill)    
    self.Fits.append(FitSigmoid)    
    self.Fits.append(FitPow)    
    self.Fits.append(FitLogNormal)

  def help(self):
    plt.close()
    fig, axarr = plt.subplots(int((1 + len(self.Fits))/2), 2, sharex='all', facecolor='#e5e5e5', figsize=(11, 18), dpi=80)
      
    plt.rc('font', **{'family':'sans-serif'}) # could change the way eg texttt is rendered
    params = {'backend': 'pdf',
          'axes.labelsize': 14,
          'font.size': 14,
          'text.usetex': False,
          }
    plt.rcParams.update(params)   
    ii = 0
    jj = 0
    xs = np.linspace(-10, 10, 250)
    for fit in self.Fits:
      if len(fit.args) == 1:
        ys = fit.f(xs)
      elif len(fit.args) == 2:
        ys = fit.f(xs, 1)
      elif len(fit.args) == 3:
        ys = fit.f(xs, 1, 4)
      elif len(fit.args) == 4:
        ys = fit.f(xs, 1, 3, 3)
      elif len(fit.args) == 5:
        ys = fit.f(xs, 1, 3, 2, 4)
      elif len(fit.args) == 6:
        ys = fit.f(xs, 1, 4, 3, 3, 5)
      elif len(fit.args) == 7:
        ys = fit.f(xs, 1, 4, 3, 3, 2, 2)

      axarr[ii, jj].plot(xs, ys, color=randomColor(), linestyle='-')
      axarr[ii, jj].set_title(fit.name + ": $" + str(fit.latexFormula) + "$")
      axarr[ii, jj].xaxis.set_major_formatter(plt.NullFormatter())
      axarr[ii, jj].yaxis.set_major_formatter(plt.NullFormatter())
      axarr[ii, jj].grid(b=True, which='major', color='#cccccc', linestyle='-')
      axarr[ii, jj].grid(b=True, which='minor', color='#e5e5e5', linestyle='--')
      [minrng, maxrng] = axarr[ii, jj].get_ylim()
      totalrng = (maxrng-minrng)
      midptrng = (maxrng+minrng)/2      
      minrng = midptrng - .55*totalrng
      maxrng = midptrng + .55*totalrng
      axarr[ii, jj].set_ylim([minrng, maxrng])
      if jj is 1:
        ii += 1
        jj = 0
      else:
        jj += 1
        axarr[ii, jj].xaxis.set_major_formatter(plt.NullFormatter())
        axarr[ii, jj].yaxis.set_major_formatter(plt.NullFormatter())
    
    plt.tight_layout()
    plt.show()  
    plt.close()
    return 1


AllFits = AllFits()  