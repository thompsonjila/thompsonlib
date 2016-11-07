# -*- coding: utf-8 -*-

import numpy as np
import os.path

import warnings
warnings.simplefilter('error')



class Dataset:
  def __init__(self, filename, name='', delimiter='\t', headers=True, skip_header=0, skip_footer=0, usecols=[], unpack=True, max_rows=0, isDatalog=False):
    if (os.path.isfile(filename)):
      self.folder, self.filename = os.path.split(filename)
      self.data = np.asarray(np.genfromtxt(filename, delimiter=delimiter, names=headers, skip_header=skip_header, usecols=usecols, skip_footer=skip_footer, unpack=True))
      self.headers = self.data.dtype.names
      self.name = name
      self.rows = len(self.data)
      self.cols = len(self.data[0])
      self.isDatalog = isDatalog
    else:
      warnings.warn("File not found for import: " + str(filename))      
      return
      
  def __repr__(self):
    retStr = str(self.name) + " ("+str(self.filename)+") is a Dataset:\r\n"
    retStr += "\t" + str(self.rows) + " rows\r\n"
    retStr += "\t" + str(self.cols) + " columns\r\n" 
    return retStr
    
  def __getitem__(self, index):
    if self.isDatalog:    
      if isinstance(index, str):
        return self.data[index]
      else:
        warnings.warn("Datalog Datasets can only be indexed by column name. Use 'print(obj.headers)' to see names.")
    return self.data[index] 






''' Rubidium-side importing wrappers '''
# Rb style Datalog importing
def importDatalog(filename, name='', headers=True, skip_header=0, skip_footer=0, usecols=[], unpack=True, max_rows=0):
  filename = "//Radiant/Documents/Data/" + filename + "_XYGraphDataLog0.txt"
  return Dataset(filename, name, headers=headers, skip_header=skip_header, skip_footer=skip_footer, usecols=usecols, unpack=unpack, max_rows=max_rows, isDatalog=True)

# Rb style time traces
def importTimeTrace(filename, name='', skip_header=3, skip_footer=3, usecols=[], unpack=True, max_rows=0):
  numberOfAIs = 7
  colnames = ["AI%d" % (x) for x in range(0, numberOfAIs)]
  return Dataset(filename, name, delimiter='\t', headers=colnames, skip_header=skip_header, skip_footer=skip_footer, usecols=usecols, unpack=unpack, max_rows=max_rows)



''' Strontium-side importing wrappers '''
# Sr style AI point importing
def importAIPoints(filename, name='', headers=False, skip_header=0, skip_footer=0, unpack=True, max_rows=0):
  numberOfAIs = 8  
  if not headers:
    colnums = [0]
    colnums.extend(np.arange(1, 2*numberOfAIs, 2))
    colnames = ["time"]
    colnames.extend(["AI%d" % (x-1) for x in range(numberOfAIs, 0, -1)])
  return Dataset(filename, name, headers=colnames, skip_header=skip_header, skip_footer=skip_footer, usecols=colnums, unpack=unpack, max_rows=max_rows)
  
  
''' General importing wrappers '''
# import regular comma separated file
def importCSV(filename, name='', headers=False, skip_header=0, skip_footer=0, usecols=[], unpack=True, max_rows=0):
  return Dataset(filename, name, delimiter=',', headers=headers, skip_header=skip_header, skip_footer=skip_footer, usecols=usecols, unpack=unpack, max_rows=max_rows)

# import regular comma separated file
def importTSV(filename, name='', headers=False, skip_header=0, skip_footer=0, usecols=[], unpack=True, max_rows=0):
  return Dataset(filename, name, delimiter='\t', headers=headers, skip_header=skip_header, skip_footer=skip_footer, usecols=usecols, unpack=unpack, max_rows=max_rows)
