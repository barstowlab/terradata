# Rachel this is the Amazon stuff for you
# monthsWithMaskedPointsAmazon, amazonAveragedEfficienciesWithMaskedPoints = \
# SpatiallyAverageEfficiencyData(efficiencyDict, keysToAverage, startYear, startMonth, startDay, \
# includeMaskedPointsAsZeroInAverage=True, \
# latitudeLimits=[5, -14], longitudeLimits=[-79, -45])


monthsForNPPDataAmazon, globallyAveragedNPPsWithMaskedPointsAmazon = \
SpatiallyAverageMaskedData(nppDict, keysToAverage, startYear, startMonth, startDay, \
includeMaskedPointsAsZeroInAverage=True, \
latitudeLimits=[5, -14], longitudeLimits=[-79, -45])
