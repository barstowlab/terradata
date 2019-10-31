# ------------------------------------------------------------------------------------------------ #
# Created by Buz
# ------------------------------------------------------------------------------------------------ #


from numpy import mean, array
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel
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
	


efficiencyDictKeys = list(efficiencyDict.keys())

globallyAveragedEfficiencies = []
months = []
timeKeys = []

startDate = efficiencyDictKeys[0]
startYear, startMonth, startDay = CalculateDateFromKey(startDate)

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
	
	monthsSinceStart = CalculateMonthsFromStart(key, startYear, startMonth, startDay)

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
	months.append(monthsSinceStart)
	globallyAveragedEfficiencies.append(globallyAveragedEfficiency)
	
	k += 1

figure()
plot(months, globallyAveragedEfficiencies)
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged Photosynthetic Efficiency")

show()


