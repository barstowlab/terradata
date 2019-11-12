# ------------------------------------------------------------------------------------------------ #
def ImportCSV(fileName):

	dataHandle = open(fileName, 'r')
	data = dataHandle.readlines()
	
	dataArray = []
	
	for line in data:
		dataArray.append(line.strip().split(','))
	
	return dataArray
# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
def ConvertImportedArrayToFloats(importedArray):
	from numpy import float

	i = 0
	x = []
	y = [] 
	while i < len(importedArray):
		x.append(float(importedArray[i][0]))
		y.append(float(importedArray[i][1]))
		i += 1
	
	return x, y

# ------------------------------------------------------------------------------------------------ #

from matplotlib.pyplot import *

baseDir = 'output'

efficiencyFileName = 'efficiency.csv'
nppFileName = 'npp.csv'
laiFileName = 'lai.csv'
insolFileName = 'insol.csv'


averageEfficiencyData = ImportCSV(baseDir + '/' + efficiencyFileName)
averageNPPData = ImportCSV(baseDir + '/' + nppFileName)
averageLAIData = ImportCSV(baseDir + '/' + laiFileName)
averageInsolData = ImportCSV(baseDir + '/' + insolFileName)

averageEfficiencyMonths, averageEfficiency = ConvertImportedArrayToFloats(averageEfficiencyData)

