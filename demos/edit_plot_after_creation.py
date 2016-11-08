# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:39:04 2016

@author: Thompson Lab
"""

import importlib
from thompsonlib import thompsonlib as TL
importlib.reload(TL)

a1 = TL.Trace([1.3, 2, 3, 3.4, 1.5, 2, 2.3, 3.3, 3.75, 4.15, 2.6], [.36, .6, .2, .55, .26, .22, .21, .214, .26, .36, 0.2])

TL.Plot(a1, title="Plot is not editable", fc="silver", fs=(6, 4))

mypl = TL.Plot(a1, fc="gold", fs=(6, 4), show=False)
mypl.title("Title edited after creation")
mypl.show()
mypl.close()
