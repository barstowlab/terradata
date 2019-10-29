# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:28:41 2019

@author: buz
"""

from numpy import mean

from matplotlib.pyplot import figure, show, plot


efficiencyDictKeys = list(efficiencyDict.keys())

globallyAveragedEfficiencies = []
months = []
timeKeys = []

k = 0

while k < len(efficiencyDictKeys):

	key = efficiencyDictKeys[k]
	print(key)
	
	efficiencyData = efficiencyDict[key][2].data
	efficiencyMask = efficiencyDict[key][2].mask

	latitudeData = efficiencyDict[key][0]
	longitudeData = efficiencyDict[key][1]

	latitudeLength = len(latitudeData)
	longitudeLength = len(longitudeData)

	latitudeAveragedEfficiencies = []
	latitudesWithEfficiencyData = []

	i = 0
	while i < latitudeLength:

		validDataPointsOnLineOfLatitude = []

		j = 0
	
		latitude = latitudeData[i]

		while j < longitudeLength:

			longitude = longitudeData[j]

			dataPoint = efficiencyData[i][j]
			dataPointMask = efficiencyMask[i][j]

			if dataPointMask == False:
				validDataPointsOnLineOfLatitude.append(dataPoint)
			

			j += 1

		if len(validDataPointsOnLineOfLatitude) > 0:
			latitudeAveragedEfficiency = mean(validDataPointsOnLineOfLatitude)
			latitudeAveragedEfficiencies.append(latitudeAveragedEfficiency)
			latitudesWithEfficiencyData.append(latitude)

		i += 1



	# figure()
# 	plot(latitudesWithEfficiencyData, latitudeAveragedEfficiencies)
# 	xlabel('Latitude')
# 	ylabel('Photosynthetic Efficiency')
# 
# 	show()

	globallyAveragedEfficiency = mean(latitudeAveragedEfficiencies)
	months.append(k)
	globallyAveragedEfficiencies.append(globallyAveragedEfficiency)
	
	k += 1

figure()
plot(months, globallyAveragedEfficiencies)
xlabel('Month from Start')
ylabel('Globally Averaged Photosynthetic Efficiency')

show()

