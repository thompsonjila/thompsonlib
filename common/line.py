# -*- coding: utf-8 -*-

from common.colors import namedColor

# A Line() is an object for plotting defined by a position 'p', a linestyle, and whether it is vertical or not.
class Line:
  def __init__(self, p, ls='--', vert=False, color='#AAAAAA', name=''):
    self.p = p
    self.ls = ls
    self.vert = vert
    self.color = namedColor(color) if namedColor(color) else color
    self.name = str(name)