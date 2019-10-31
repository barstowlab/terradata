from numpy import mean, array
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel, close
from scipy.optimize import curve_fit


def MapPlotCP2(data, latitudeData, longitudeData, time, xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Insolation: ", vmin=0, vmax=600, showPlots=False):
	
	from cartopy import config
	import cartopy.crs as ccrs
	
	import numpy as np
	import matplotlib.pyplot as plt
	
	
	xWidthScaled = xWidth*scale
	yWidthScaled = yWidth*scale
	
	lons, lats = np.meshgrid(longitudeData, latitudeData)

	fig = plt.figure(figsize=(xWidthScaled, yWidthScaled), dpi=dpi)

	ax = plt.axes(projection=ccrs.PlateCarree())
	

	im = plt.contourf(lons, lats, data, 60, transform=ccrs.PlateCarree())

	plt.colorbar(im, ax=ax)

	
	ax.set_title(titleText + time)
	
	plt.show()

# ------------------------------------------------------------------------------------------------ #



# efficiencyDictKeys = list(efficiencyDict.keys())
efficiencyDictKeys = ['2006-07-01']

# Rachel this is for you
#efficiencyDictKeys = ['2006-07-01', '2007-07-01', '2008-07-01', '2009-07-01', '2010-07-01', \
#'2011-07-01', '2012-07-01', '2013-07-01', '2014-07-01']

for key in efficiencyDictKeys:

	effData = efficiencyDict[key][2]
	latitudeData = efficiencyDict[key][0]
	longitudeData = efficiencyDict[key][1]


	MapPlotCP2(effData, latitudeData, longitudeData, '2006-07-01', xWidth=11, yWidth=8.5, \
	scale=1.4, dpi=80, \
	titleText="Efficiency: ", vmin=0, vmax=600, showPlots=False)

