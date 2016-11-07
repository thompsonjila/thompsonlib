# -*- coding: utf-8 -*-
c = 299792458


def Ntot(det, shiftMHz):
  g0 = 0.44; # MHz  
  if type(det) is u:
      if det.unit is 'Hz':
        detMHz = det.val/1000000
  else:
    detMHz = det
  if type(shiftMHz) is u:
    if shiftMHz.unit is 'Hz':
      MHz = shiftMHz.val/1000000
  else:
    MHz = shiftMHz
  return (MHz**2 + MHz*detMHz)/(g0**2)

class u:
  metricAbbrev = {3: "k", 6: "M", 9: "G", 12: "T", 15: "P", -3: "m", -6: "μ", -9: "n", -12: "p", -15: "f", 0: ""}
  def __init__(self, val, dim):
    self.unit = dim
    self.val = val
    self.exponent = 0
    while(val/1000 > 1.0):
      self.exponent += 3 # ???
      val /= 1000
    self.significand = val

  def p(self, sigfigs = 100):
    print(str(self.significand)[0:sigfigs] + " " + self.metricAbbrev[self.exponent] + self.unit)
    
  def __repr__(self):
  #  return(str(self.val) + " " + self.unit)
    global metricAbbrev
    return(str(self.significand) + " " + self.metricAbbrev[self.exponent] + self.unit)



  def __sub__(self, u2):
    if(self.unit == u2.unit):
      return u(self.val-u2.val, self.unit)
    else:
      return u(0, "ERROR")



class Transition:
  def __init__(self, D, F, Fprime, freq):
    global c
    self.line = D
    self.F = F
    self.Fprime = Fprime
    self.freq = u(freq, "Hz") # freq
  #  self.wavelength = c/freq

class Rb87:
  def __init__(self):
    self.name = "Rudium 87!"
    
    # 5S1/2, from Steck
    self.F1 = 0
    self.F2 = 6834682610.90429
    
    # 5P3/2, from Steck
    self.D2Fp0 = 4271676631.81519 + 384230484468500 - 302073800
    self.D2Fp1 = 4271676631.81519 + 384230484468500 - 229851800
    self.D2Fp2 = 4271676631.81519 + 384230484468500 - 72911300
    self.D2Fp3 = 4271676631.81519 + 384230484468500 + 193740800
    
    # 5P1/2, from Steck - TODO
    self.D1Fp1 = 0
    self.D1Fp2 = 0
    
    self.D2F2Fp3 = Transition("D2", 2, 3, self.D2Fp3 - self.F2)


Rb87 = Rb87()