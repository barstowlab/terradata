# ------------------------------------------------------------------------------------------------ #
def MapPlot(data, latitudeData, longitudeData, time, xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Insolation: ", vmin=0, vmax=600, showPlots=False):
	
	xWidthScaled = xWidth*scale
	yWidthScaled = yWidth*scale
	
	lons, lats = np.meshgrid(longitudeData, latitudeData)

	fig = plt.figure(figsize=(xWidthScaled, yWidthScaled), dpi=dpi)

	ax = fig.add_axes([0.05,0.05,0.9,0.9])

	m = Basemap(projection='cea',llcrnrlat=-90,urcrnrlat=90,\
				llcrnrlon=-180,urcrnrlon=180,resolution='c', lon_0=0)
	
	m.drawcoastlines()

	im = m.pcolormesh(lons, lats, data, shading='flat', \
	cmap=plt.cm.jet, latlon=True, vmin=vmin, vmax=vmax)

	m.drawparallels(np.arange(-90.,99., 30.), labels=[True, False, False, True])
	m.drawmeridians(np.arange(-180.,189., 60.), labels=[True, False, False, True])
	
	cb = m.colorbar(im, "bottom", size="5%", pad="10%")
	
	ax.set_title(titleText + time)
	
	plt.show()

# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
def AverageDataset(dataDict, months=['04', '05', '06', '07', '08', '09'], timeStamps=None):
	
	import pdb
	import numpy.ma
	
	dataKeys = dataDict.keys()

	
	if months != None and timeStamps == None:
		dataKeysToUse = []	
		for key in dataKeys:
			splitKey = key.split('-')
			if splitKey[1] in months:
				dataKeysToUse.append(key)
	elif months == None and timeStamps != None:
		dataKeysToUse = timeStamps
	else:
		dataKeysToUse = dataKeys
	
	dataKeysToUse = sorted(dataKeysToUse)
	
# 	pdb.set_trace()
		
	averageData = numpy.ma.zeros(dataDict[dataKeysToUse[0]][2].shape)
	
	i = 0
	while i < len(dataKeysToUse):
		averageData += dataDict[dataKeysToUse[i]][2]
		i += 1
	
	averageData = averageData/len(dataKeysToUse)
	
	[latitude, longitude] = [dataDict[dataKeysToUse[0]][0], dataDict[dataKeysToUse[0]][1]]
	
	return [averageData, latitude, longitude]
# ------------------------------------------------------------------------------------------------ #








[averagedNppNorthernSummerData, latitudeNppNS, longitudeNppNS] = \
AverageDataset(nppDict, months=['04', '05', '06', '07', '08', '09'])

[averagedNppSouthernSummerData, latitudeNppSS, longitudeNppSS] = \
AverageDataset(nppDict, months=['10', '11', '12', '01', '02', '03'])

[averagedNppData, latitudeNpp, longitudeNpp] = \
AverageDataset(nppDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])




[averagedEffNorthernSummerData, latitudeEffNS, longitudeEffNS] = \
AverageDataset(efficiencyDict, months=['05', '06', '07'])

[averagedEffSouthernSummerData, latitudeEffSS, longitudeEffSS] = \
AverageDataset(efficiencyDict, months=['10', '11', '12', '01', '02', '03'])

[averagedEffData, latitudeEff, longitudeEff] = \
AverageDataset(efficiencyDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])




[averagedLaiNorthernSummerData, latitudeLaiNS, longitudeLaiNS] = \
AverageDataset(laiDict, months=['04', '05', '06', '07', '08', '09'])

[averagedLaiSouthernSummerData, latitudeLaiSS, longitudeLaiSS] = \
AverageDataset(laiDict, months=['10', '11', '12', '01', '02', '03'])

[averagedLaiData, latitudeLai, longitudeLai] = \
AverageDataset(laiDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])




[averagedInsolNorthernSummerData, latitudeInsolNS, longitudeInsolNS] = \
AverageDataset(insolDict, months=['04', '05', '06', '07', '08', '09'])

[averagedInsolSouthernSummerData, latitudeInsolSS, longitudeInsolSS] = \
AverageDataset(insolDict, months=['10', '11', '12', '01', '02', '03'])

[averagedInsolData, latitudeInsol, longitudeInsol] = \
AverageDataset(insolDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])





# MapPlot(averagedNppNorthernSummerData, latitudeNppNS, longitudeNppNS, "Averaged April-September. Northern Hemisphere Summer.", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Npp: ", vmin=-10, vmax=10, showPlots=False)
# 
# MapPlot(averagedNppSouthernSummerData, latitudeNppSS, longitudeNppSS, "Averaged October-March. Southern Hemisphere Summer.", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Npp: ", vmin=-10, vmax=10, showPlots=False)
# 
# MapPlot(averagedNppData, latitudeNpp, longitudeNpp, "Annual Average NPP", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Npp: ", vmin=-10, vmax=10, showPlots=False)




effVMin = -0.01
effVMax = 0.01

MapPlot(averagedEffNorthernSummerData, latitudeEffNS, longitudeEffNS, "Efficiency Averaged April-September. Northern Hemisphere Summer.", \
xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Eff: ", vmin=effVMin, vmax=effVMax, showPlots=False)

MapPlot(averagedEffSouthernSummerData, latitudeEffSS, longitudeEffSS, "Efficiency Averaged October-March. Southern Hemisphere Summer.", \
xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Eff: ", vmin=effVMin, vmax=effVMax, showPlots=False)

MapPlot(averagedEffData, latitudeEff, longitudeEff, "Annual Average Efficiency", \
xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Eff: ", vmin=effVMin, vmax=effVMax, showPlots=False)



# laiVMin = 0
# laiVMax = 10
# 
# MapPlot(averagedLaiNorthernSummerData, latitudeLaiNS, longitudeLaiNS, "LAI Averaged April-September. Northern Hemisphere Summer.", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Lai: ", vmin=laiVMin, vmax=laiVMax, showPlots=False)
# 
# MapPlot(averagedLaiSouthernSummerData, latitudeLaiSS, longitudeLaiSS, "LAI Averaged October-March. Southern Hemisphere Summer.", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Lai: ", vmin=laiVMin, vmax=laiVMax, showPlots=False)
# 
# MapPlot(averagedLaiData, latitudeLai, longitudeLai, "Annual Average LAI", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Lai: ", vmin=laiVMin, vmax=laiVMax, showPlots=False)
# 
# 
# 
# 
# 
# insolationVMin = 0
# insolationVMax = 600
# 
# MapPlot(averagedInsolNorthernSummerData, latitudeInsolNS, longitudeInsolNS, "Insolation Averaged April-September. Northern Hemisphere Summer.", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Insol: ", vmin=insolationVMin, vmax=insolationVMax, showPlots=False)
# 
# MapPlot(averagedInsolSouthernSummerData, latitudeInsolSS, longitudeInsolSS, "Insolation Averaged October-March. Southern Hemisphere Summer.", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Insol: ", vmin=insolationVMin, vmax=insolationVMax, showPlots=False)
# 
# MapPlot(averagedInsolData, latitudeInsol, longitudeInsol, "Annual Average Insolation", \
# xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
# titleText="Insol: ", vmin=insolationVMin, vmax=insolationVMax, showPlots=False)
# 
# 
# 
# 
# 
