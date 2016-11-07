"""
Reference for colormaps included with Matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random
import six

# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html

cmaps = ['viridis', 'inferno', 'plasma', 'magma', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys',
         'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu',
         'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'gist_heat', 'gray', 'hot',
         'pink', 'spring', 'summer', 'winter', 'BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
         'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral', 'seismic', 'Accent', 'Dark2', 'Paired',
         'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'gist_earth', 'terrain', 'ocean', 'gist_stern',
         'brg', 'CMRmap', 'cubehelix', 'gnuplot', 'gnuplot2', 'gist_ncar', 'nipy_spectral', 'jet',
         'rainbow', 'gist_rainbow', 'hsv', 'flag', 'prism']


ncols = 2
nrows = len(cmaps) // ncols
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients():
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(8, 8))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.8)
    axes[0, 0].set_title('All colormaps', fontsize=14)
    axes[0, 1].set_title('All colormaps', fontsize=14)

    for row in range(0, nrows):
      for col in range(0, ncols):
        axes[row, col].imshow(gradient, aspect='auto', cmap=plt.get_cmap(cmaps[row*ncols + col]))
        pos = list(axes[row, col].get_position().bounds)
        y_text = pos[1] + pos[3]/2.
        if col:
          x_text = pos[0] + pos[2] + 0.01
          fig.text(x_text, y_text, cmaps[row*ncols + col], va='center', ha='left', fontsize=10)
        else:
          x_text = pos[0] - 0.01
          fig.text(x_text, y_text, cmaps[row*ncols + col], va='center', ha='right', fontsize=10)
        axes[row, col].set_axis_off()


if __name__ == "__main__":
  plot_color_gradients()
  plt.savefig("colormaps.pdf")
  plt.show()


def randomColor():
  return "#%02x%02x%02x" % (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)) 


def namedColor(colorStr):
  colors_ = list(six.iteritems(colors.cnames))
  for name, rgb in six.iteritems(colors.ColorConverter.colors):
      hex_ = colors.rgb2hex(rgb)
      colors_.append((name, hex_))
  colors_.append(("m1", colors.rgb2hex((0.2472, 0.24, 0.6))))
  colors_.append(("m2", colors.rgb2hex((0.6, 0.24, 0.4428))))
  colors_.append(("m3", colors.rgb2hex((0.6, 0.5470, 0.24))))
  colors_.append(("m4", colors.rgb2hex((0.24, 0.6, 0.3369))))
  colors_.append(("m5", colors.rgb2hex((0.24, 0.3532, 0.6))))
  colors_.append(("m6", colors.rgb2hex((0.6, 0.24, 0.5633))))
  colors_.append(("m7", colors.rgb2hex((0.6, 0.4266, 0.24))))
  colors_.append(("m8", colors.rgb2hex((0.2635, 0.6, 0.24))))
  colors_.append(("m9", colors.rgb2hex((0.24, 0.4735, 0.6))))
  colors_ = dict(colors_)
  if colorStr in colors_:
    return colors_[colorStr]
  else:
    return None
