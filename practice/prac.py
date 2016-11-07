# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:46:56 2016

@author: Thompson Lab
"""

import numpy as np

import sys
sys.path.insert(0, '\\Radiant\Documents\DataAnalysis\common')

import grahamutils as TL
#from DataAnalysis.common import common.grahamutils as TL
#import ..commom.grahamutils as TL
#\\Radiant\Documents\DataAnalysis\practice\
data=(np.genfromtxt("simpleTwoCol.txt", delimiter='\t', names=True))
columns = data.dtype.names
print(columns)


col0=TL.Wave(data['time'])
col1=TL.Wave(data['amp'])

ptstrial=TL.Trace(col0, col1, 'b-')

x1 = np.linspace(1.345, 2.0, num=250)
y1 = 0.105 * np.exp(-1 * (x1-1.345) / .02) + 0.025

epx = TL.Trace(x1, y1, 'r.')

TL.pleasePlot([ptstrial, epx])