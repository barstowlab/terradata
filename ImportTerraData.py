from terraData import *

from specutils10 import GenerateFileList
import re
from numpy.ma import masked_values
from numpy import array
from os.path import basename, splitext

import cartopy.feature as cpf

	

baseDir = 'Data/'


nppDir = baseDir + '/' + 'NPP_1month'
laiDir = baseDir + '/' + 'LAI_1month'
insolDir = baseDir + '/' + 'INSOL_1month'



nppFileList = sorted(GenerateFileList(directory=nppDir, regex=".*PSN.*\.ss.csv", ignoreCase=True))
laiFileList = sorted(GenerateFileList(directory=laiDir, regex=".*LAI.*\.ss.csv", ignoreCase=True))
insolFileList = sorted(GenerateFileList(directory=insolDir, regex=".*INSOL.*\.ss.csv", ignoreCase=True))


# ------------------------------------------------------------------------------------------------ #
# Create the NPP dataset


nppDict = {}


for file in nppFileList:
	[latitudeData, longitudeData, gridData, gridDataType, timeStamp] = \
	GetLatitudeLongitudeAndGridDataFromFile(nppDir + '/' + file, 99999)
	
	nppDict[timeStamp] = [latitudeData, longitudeData, gridData]
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Create the LAI dataset

laiDict = {}

for file in laiFileList:
	[latitudeData, longitudeData, gridData, gridDataType, timeStamp] = \
	GetLatitudeLongitudeAndGridDataFromFile(laiDir + '/' + file, 99999)
	
	laiDict[timeStamp] = [latitudeData, longitudeData, gridData]
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# Create the INSOL dataset

insolDict = {}

for file in insolFileList:
	[latitudeData, longitudeData, gridData, gridDataType, timeStamp] = \
	GetLatitudeLongitudeAndGridDataFromFile(insolDir + '/' + file, 99999)
	
	insolDict[timeStamp] = [latitudeData, longitudeData, gridData]
# ------------------------------------------------------------------------------------------------ #
