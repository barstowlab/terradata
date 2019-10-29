# Condense net primary productivity, leaf area index and Insolation data into an estimate
# of efficiency

# ------------------------------------------------------------------------------------------------ #
def AnalyzeFileNameToFindDataType(filename):
	import pdb
	import re
	
	fileNameRe = re.compile('INSOL|PSN|LAI')
	
	searchRe = fileNameRe.search(filename)
	
	# pdb.set_trace()
	
	if searchRe != None:
		fileNameDataType = searchRe.group()
		if fileNameDataType == 'INSOL':
			dataType = 'insolation'
		elif fileNameDataType == 'PSN':
			dataType = 'npp'
		elif fileNameDataType == 'LAI':
			dataType = 'lai'
	else:
		dataType = 'unknown'
	

	return dataType
# ------------------------------------------------------------------------------------------------ #




# ------------------------------------------------------------------------------------------------ #
def GetLatitudeLongitudeAndGridDataFromFile(filePath, maskValue):
	
	from numpy import array, float
	from numpy.ma import masked_values
	from os.path import basename
	
	import pdb
	
	print(filePath)
	data = open(filePath, 'r').readlines()
	
	longitudes = data[0].strip().split(',')[1:]
	for lon in longitudes:
		lon = float(lon)
	longitudeData = array(longitudes, float)

	latitudes = []
	i = 1
	while i < len(data):
		latitudes.append(float(data[i].strip().split(',')[0]))
		#pdb.set_trace()
		i += 1

	latitudeData = array(latitudes, float)
	
	gridDataType = AnalyzeFileNameToFindDataType(basename(filePath))
	
	i = 1
	gridData = []
	while i < len(data):
		gridRow = data[i].strip().split(',')[1:]
		gridRowF = []
		for entry in gridRow:
			gridRowF.append(float(entry))
		gridData.append(gridRowF)	
		i += 1

	gridData = array(gridData)
	gridDataMasked = masked_values(gridData, maskValue)
	
	timeStamp = GetTimesFromFileList([basename(filePath)])[0]

	return [latitudeData, longitudeData, gridDataMasked, gridDataType, timeStamp]
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def GetTimesFromFileList(fileList):
	import re
	
	dateStampRe = re.compile('\d+\-\d+\-\d+')
	
	dateStampArray = []
	
	for fileName in fileList:
		dateStampSearch = dateStampRe.search(fileName)
		dateStamp = dateStampSearch.group()
		dateStampArray.append(dateStamp)
	
	return dateStampArray
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


# ------------------------------------------------------------------------------------------------ #
def MakeMapPlotSeriesCP(dataDict, timeStamps, saveDir, xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Efficiency: ", vmin=-0.02, vmax=0.02, showPlots=False, filePrefix='Efficiency_'):
	
	from cartopy import config
	import cartopy.crs as ccrs
	
	import numpy as np
	import matplotlib.pyplot as plt
	
	xWidthScaled = xWidth*scale
	yWidthScaled = yWidth*scale


	for time in timeStamps:
		latitudeData  = dataDict[time][0]
		longitudeData = dataDict[time][1]
		lons, lats = np.meshgrid(longitudeData, latitudeData)


		data = dataDict[time][2]

		fig = plt.figure(figsize=(xWidthScaled, yWidthScaled), dpi=dpi)
		ax = plt.axes(projection=ccrs.PlateCarree())
		
		plt.contourf(lons, lats, data, 60, transform=ccrs.PlateCarree())
			
		ax.set_title(titleText + time)
	
# 		fig.savefig(saveDir+'/'+filePrefix + time +'.png',format='png')
		
		if showPlots==True:
			plt.show()
		else:
			plt.close()

# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
def MapPlotCP(data, latitudeData, longitudeData, time, xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
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
	
	plt.colorbar(ax)

	plt.contourf(lons, lats, data, 60, transform=ccrs.PlateCarree())
	
	ax.set_title(titleText + time)
	
	plt.show()

# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
def ensure_dir(f):
    import os
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
# ------------------------------------------------------------------------------------------------ #



