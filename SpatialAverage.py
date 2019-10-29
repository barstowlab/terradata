# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:28:41 2019

@author: buz
"""

from numpy import mean

from matplotlib.pyplot import figure, show, plot

efficiencyData = efficiencyDict['2006-07-01'][2].data
efficiencyMask = efficiencyDict['2006-07-01'][2].mask

latitudeData = efficiencyDict['2006-07-01'][0]
longitudeData = efficiencyDict['2006-07-01'][1]

latitudeLength = len(latitudeData)
longitudeLength = len(longitudeData)

latitudeAveragedEfficiencies = []

i = 0
while i < latitudeLength:

	validDataPointsOnLineOfLatitude = []

	j = 0

	while j < longitudeLength:

		dataPoint = efficiencyData[i][j]
		dataPointMask = efficiencyMask[i][j]

		if dataPointMask == False:
			validDataPointsOnLineOfLatitude.append(dataPoint)

		j += 1

	latitudeAveragedEfficiency = mean(validDataPointsOnLineOfLatitude)
	latitudeAveragedEfficiencies.append(latitudeAveragedEfficiency)

	i += 1
    
figure()
plot(latitudeData, latitudeAveragedEfficiencies)
xlabel('Latitude')
ylabel('Photosynthetic Efficiency')

show()