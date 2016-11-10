from thompsonlib import thompsonlib as TL
import random as random



# data_array1 = np.loadtxt("../practice/doubleDataset.tsv", skiprows=1)
# data_array = np.array(data_array1[1:,])
# data_dimensions = data_array.shape


print("\n\n\n\n\n")
print("Plot single wave with implicit scaling:")
xpts1 = TL.Wave([.12, .25, .43, .30, .24, .03, .84, .42, .19, .01], x0=500, deltax=100, name='X Wave 1')
TL.Plot(xpts1, xlabel='x-axis scaling test: $x_0 = 100, \\Delta x = 100$', ylabel='Manual Y Label', title='Manual Title')



print("\n\n\n\n\n")
print("Plot two waves (Traces)")
print("Trace 4 has been sorted by x-values.")
xpts1 = TL.Wave([.12, .25, .43, .30, .24, .03, .54, .42, .19, .01], name='X Wave 1')
ypts1 = TL.Wave([.48, .28, .19, .73, .79, .28, .40, .14, .42, .25], name='Y Wave 1')
ypts2 = ypts1 + 1.0
ypts3 = ypts1 + 2.0
ypts4 = ypts1 + 3.0
trace1 = TL.Trace(xpts1, ypts1, name="Trace 1", color='m1')
trace2 = TL.Trace(xpts1, ypts2, name="Trace 2", color='m2', stroke=False)
trace3 = TL.Trace(xpts1, ypts3, name="Trace 3", color='m3', ls='-')
trace4 = TL.Trace(xpts1, ypts4, name="Trace 4", color='m4', ls=':', marker=None)
trace4.sort()
TL.Plot([trace1, trace2, trace3, trace4], xlabel='Manual X Label', ylabel='Manual Y Label', title='Markers and Lines')



print("\n\n\n\n\n")
print("Import data from file, fit, and plot it")
dataset1 = TL.importTSV("fake_data.tsv", name='4 Column Dataset 1', headers=True)
xpts5 = TL.Wave(dataset1["Lorentzian_xvals"], name="x2")
xpts5.setErrs([0.5*random.random() for x in range(0, 42)])
ypts5 = TL.Wave(dataset1["Lorentzian_yvals"], name="y2 (lor)")
ypts5.setErrs([10*random.random() for x in range(0, 42)])
trace5 = TL.Trace(xpts5, ypts5, 'o', name='trace pts2', color='yellow')
fit5 = TL.Fit(xpts5, ypts5, TL.FitLor, [200, 3, 1, 78], ls='-', color='orange', verbose=False)
line1 = TL.Line(-3, vert=True)
line2 = TL.Line(160)

TL.Plot([fit5, trace5], xlabel='xlabel', ylabel='ylabel', title='Fit Test')
print(fit5)

print("\n\n\n\n\n")
print("Residuals test")
residuals5 = TL.Wave(fit5.residuals, name='Residuals of Fit2')
TL.Plot(residuals5, title="Residuals of Lor Fit")


  # weighted fits, etc
  # TODO confidence bands, residuals, etc. 



print("\n\n\n\n\n")
print("Color-wave test")
pts6 = TL.Wave([0, 1, 2, 6, 4, 3, 7, 5, 12, 2, 3, 5], name='MyWave', clist=[0, .2, .1, .3, .2, .6, .8, .9, 1, 1.2, 1.3, 1.1])
trace6 = TL.Trace(pts6, cmapstr='plasma')
TL.Plot(trace6, title="Color wave test")