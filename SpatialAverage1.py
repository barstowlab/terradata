# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:28:41 2019

@author: buz
"""

from numpy import mean

from matplotlib.pyplot import figure, show, plot

efficiencyData = efficiencyDict['2006-07-01'][2].data
latitudeData = efficiencyDict['2006-07-01'][0]
longitudeData = efficiencyDict['2006-07-01'][1]

length = len(efficiencyData)

latitudeAveragedEfficiencies = []

i = 0
while i < length:
    latitudeAveragedEfficiency = mean(efficiencyData[i])
    latitudeAveragedEfficiencies.append(latitudeAveragedEfficiency)
    
    
    i += 1
    
figure()
plot(latitudeData, latitudeAveragedEfficiencies)

show()