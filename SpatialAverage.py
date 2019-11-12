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
def SpatiallyAverageMaskedData(dataDict, keysToAverage, startYear, startMonth, startDay, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875], \
includeMaskedPointsAsZeroInAverage=False):

	k = 0
	
	globallyAveragedDataArray = []
	months = []
	
	while k < len(keysToAverage):

		key = keysToAverage[k]
	
		print(key)
	
		data = dataDict[key][2].data
		mask = dataDict[key][2].mask

		latitudeData = dataDict[key][0]
		longitudeData = dataDict[key][1]

		latitudeLength = len(latitudeData)
		longitudeLength = len(longitudeData)

		latitudeAveragedDataArray = []
		latitudesWithDataArray = []
	
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

						dataPoint = data[i][j]
						dataPointMask = mask[i][j]

						if dataPointMask == False:
							validDataPointsOnLineOfLatitude.append(dataPoint)
						elif dataPointMask == True: 
							if includeMaskedPointsAsZeroInAverage == True:
								validDataPointsOnLineOfLatitude.append(0)
					
					j += 1

			if len(validDataPointsOnLineOfLatitude) > 0:
				latitudeAveragedData = mean(validDataPointsOnLineOfLatitude)
				latitudeAveragedDataArray.append(latitudeAveragedData)
				latitudesWithDataArray.append(latitude)

			i += 1


		globallyAveragedData = mean(latitudeAveragedDataArray)
		months.append(monthsSinceStart)
		globallyAveragedDataArray.append(globallyAveragedData)
	
		k += 1
	
	return months, globallyAveragedDataArray 
# ------------------------------------------------------------------------------------------------ #



# ------------------------------------------------------------------------------------------------ #
def SpatiallyAverageUnmaskedData(dataDict, keysToAverage, startYear, startMonth, startDay, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875]):

	k = 0
	
	globallyAveragedDataArray = []
	months = []
	
	while k < len(keysToAverage):

		key = keysToAverage[k]
	
		print(key)
	
		data = dataDict[key][2].data

		latitudeData = dataDict[key][0]
		longitudeData = dataDict[key][1]

		latitudeLength = len(latitudeData)
		longitudeLength = len(longitudeData)

		latitudeAveragedDataArray = []
		latitudesWithDataArray = []
	
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

						dataPoint = data[i][j]
						validDataPointsOnLineOfLatitude.append(dataPoint)
						
						
					j += 1

			if len(validDataPointsOnLineOfLatitude) > 0:
				latitudeAveragedData = mean(validDataPointsOnLineOfLatitude)
				latitudeAveragedDataArray.append(latitudeAveragedData)
				latitudesWithDataArray.append(latitude)

			i += 1


		globallyAveragedData = mean(latitudeAveragedDataArray)
		months.append(monthsSinceStart)
		globallyAveragedDataArray.append(globallyAveragedData)
	
		k += 1
	
	return months, globallyAveragedDataArray 
# ------------------------------------------------------------------------------------------------ #




# ------------------------------------------------------------------------------------------------ #
# Run code

keysToAverage = list(efficiencyDict.keys())



startDate = keysToAverage[0]
startYear, startMonth, startDay = CalculateDateFromKey(startDate)


monthsForEfficiencyData, globallyAveragedEfficienciesWithMaskedPoints = \
SpatiallyAverageMaskedData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
includeMaskedPointsAsZeroInAverage=True, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875])




monthsForNPPData, globallyAveragedNPPsWithMaskedPoints = \
SpatiallyAverageMaskedData(nppDict, keysToAverage, startYear, startMonth, startDay, \
includeMaskedPointsAsZeroInAverage=True, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875])


monthsForLAIData, globallyAveragedLAIsWithMaskedPoints = \
SpatiallyAverageMaskedData(laiDict, keysToAverage, startYear, startMonth, startDay, \
includeMaskedPointsAsZeroInAverage=True, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875])


monthsForInsolData, globallyAveragedInsol = \
SpatiallyAverageUnmaskedData(insolDict, keysToAverage, startYear, startMonth, startDay, \
latitudeLimits=[89.875, -89.875], longitudeLimits=[-179.875, 179.875])




# Rachel this is the Amazon stuff for you
# monthsWithMaskedPointsAmazon, amazonAveragedEfficienciesWithMaskedPoints = \
# SpatiallyAverageEfficiencyData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
# includeMaskedPointsAsZeroInAverage=True, \
# latitudeLimits=[5, -14], longitudeLimits=[-79, -45])



figure()
plot(monthsForEfficiencyData, globallyAveragedEfficienciesWithMaskedPoints)
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged Photosynthetic Efficiency")
title("Globally Averaged Photosynthetic Efficiencies With Masked Points")


figure()
plot(monthsForNPPData, globallyAveragedNPPsWithMaskedPoints)
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged NPP")
title("Globally Averaged NPP With Masked Points")

figure()
plot(monthsForLAIData, globallyAveragedLAIsWithMaskedPoints)
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged LAI")
title("Globally Averaged LAI With Masked Points")

figure()
plot(monthsForInsolData, globallyAveragedInsol)
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged Insolation")
title("Globally Averaged Insolation")



show()

# ------------------------------------------------------------------------------------------------ #


