# ------------------------------------------------------------------------------------------------ #
# Created by Buz
# ------------------------------------------------------------------------------------------------ #


from numpy import mean, array
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel, close, title
from scipy.optimize import curve_fit


# ------------------------------------------------------------------------------------------------ #
def CalculateDateFromKey(key):
	date = key.split('-')
	year = int(date[0])
	month = int(date[1])
	day = int(date[2])
	
	return year, month, day
# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
def CalculateMonthsFromStart(dateKey, startYear, startMonth, startDay):
	
	year, month, day = CalculateDateFromKey(dateKey)
	
	monthsFromStart = (year - startYear)*12 + (month - startMonth) + ((day - startDay)/30)

	return monthsFromStart
# ------------------------------------------------------------------------------------------------ #
	
# ------------------------------------------------------------------------------------------------ #
def SpatiallyAverageEfficiencyData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875], \
includeMaskedPointsAsZeroInAverage=False):

	k = 0
	
	globallyAveragedEfficiencies = []
	months = []
	
	while k < len(keysToAverage):

		key = keysToAverage[k]
	
		print(key)
	
		efficiencyData = efficiencyDict[key][2].data
		efficiencyMask = efficiencyDict[key][2].mask

		latitudeData = efficiencyDict[key][0]
		longitudeData = efficiencyDict[key][1]

		latitudeLength = len(latitudeData)
		longitudeLength = len(longitudeData)

		latitudeAveragedEfficiencies = []
		latitudesWithEfficiencyData = []
	
		monthsSinceStart = CalculateMonthsFromStart(key, startYear, startMonth, startDay)

		i = 0
		while i < latitudeLength:
			
			validDataPointsOnLineOfLatitude = []

			j = 0
	
			latitude = latitudeData[i]

			if latitude <= latitudeLimits[0] and latitude >= latitudeLimits[1]:

				while j < longitudeLength:

					longitude = longitudeData[j]

					if longitude >= longitudeLimits[0] and longitude <= longitudeLimits[1]:

						dataPoint = efficiencyData[i][j]
						dataPointMask = efficiencyMask[i][j]

						if dataPointMask == False:
							validDataPointsOnLineOfLatitude.append(dataPoint)
						elif dataPointMask == True: 
							if includeMaskedPointsAsZeroInAverage == True:
								validDataPointsOnLineOfLatitude.append(0)
					
					j += 1

			if len(validDataPointsOnLineOfLatitude) > 0:
				latitudeAveragedEfficiency = mean(validDataPointsOnLineOfLatitude)
				latitudeAveragedEfficiencies.append(latitudeAveragedEfficiency)
				latitudesWithEfficiencyData.append(latitude)

			i += 1


		globallyAveragedEfficiency = mean(latitudeAveragedEfficiencies)
		months.append(monthsSinceStart)
		globallyAveragedEfficiencies.append(globallyAveragedEfficiency)
	
		k += 1
	
	return months, globallyAveragedEfficiencies 
# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
# Run code

keysToAverage = list(efficiencyDict.keys())



startDate = keysToAverage[0]
startYear, startMonth, startDay = CalculateDateFromKey(startDate)



# monthsWithMaskedPoints, globallyAveragedEfficienciesWithMaskedPoints = \
# SpatiallyAverageEfficiencyData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
# includeMaskedPointsAsZeroInAverage=True, \
# latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875])
# 
monthsWithoutMaskedPoints, globallyAveragedEfficienciesWithoutMaskedPoints = \
SpatiallyAverageEfficiencyData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
includeMaskedPointsAsZeroInAverage=False, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875])

# Rachel this is the Amazon stuff for you
# monthsWithMaskedPointsAmazon, amazonAveragedEfficienciesWithMaskedPoints = \
# SpatiallyAverageEfficiencyData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
# includeMaskedPointsAsZeroInAverage=True, \
# latitudeLimits=[5, -14], longitudeLimits=[-79, -45])



figure()
plot(monthsWithoutMaskedPoints, globallyAveragedEfficienciesWithoutMaskedPoints)
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged Photosynthetic Efficiency")
title("Globally Averaged Photosynthetic Efficiencies Without Masked Points")

# figure()
# plot(monthsWithMaskedPoints, globallyAveragedEfficienciesWithMaskedPoints)
# xlabel("Time since July 2006 (months)")
# ylabel("Globally Averaged Photosynthetic Efficiency")
# title("Globally Averaged Photosynthetic Efficiencies With Masked Points")

show()

months = monthsWithoutMaskedPoints
globallyAveragedEfficiencies = globallyAveragedEfficienciesWithoutMaskedPoints
# ------------------------------------------------------------------------------------------------ #


