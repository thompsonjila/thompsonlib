# -*- coding: utf-8 -*-

from thompsonlib import thompsonlib as TL
from thompsonlib.common.colors import plot_color_gradients

# Get help for one fit function
print(TL.FitExp)

# Get help for all fit functions
print(TL.AllFits)

# Print all color maps
plot_color_gradients()

# Quickly preview a wave.
wave1 = TL.Wave([1, 2, .3, .66, 2.4, 1.5], name="Test Wave")
wave1.plot()