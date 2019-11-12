# Output averaged efficiency, npp, lai and insol data

from utils import ensure_dir
from vectorOutput import *

baseDir = 'output/'

efficiencyFileName = 'efficiency.csv'
nppFileName = 'npp.csv'
laiFileName = 'lai.csv'
insolFileName = 'insol.csv'


ensure_dir(baseDir)


effMatrix = generateOutputMatrix(\
[monthsForEfficiencyData, globallyAveragedEfficienciesWithMaskedPoints], delimeter=',')

laiMatrix = generateOutputMatrix(\
[monthsForLAIData, globallyAveragedLAIsWithMaskedPoints], delimeter=',')

nppMatrix = generateOutputMatrix(\
[monthsForNPPData, globallyAveragedNPPsWithMaskedPoints], delimeter=',')

insolMatrix = generateOutputMatrix(\
[monthsForInsolData, globallyAveragedInsol], delimeter=',')

writeOutputMatrix(baseDir + '/' + efficiencyFileName, effMatrix)
writeOutputMatrix(baseDir + '/' + laiFileName, laiMatrix)
writeOutputMatrix(baseDir + '/' + nppFileName, nppMatrix)
writeOutputMatrix(baseDir + '/' + insolFileName, insolMatrix)
