# ------------------------------------------------------------------------------------------------ #

[averagedNppNorthernSummerData, latitudeNppNS, longitudeNppNS] = \
AverageDataset(nppDict, months=['04', '05', '06', '07', '08', '09'])

[averagedNppSouthernSummerData, latitudeNppSS, longitudeNppSS] = \
AverageDataset(nppDict, months=['10', '11', '12', '01', '02', '03'])

[averagedNppData, latitudeNpp, longitudeNpp] = \
AverageDataset(nppDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])




[averagedEffNorthernSummerData, latitudeEffNS, longitudeEffNS] = \
AverageDataset(efficiencyDict, months=['05', '06', '07'])

[averagedEffSouthernSummerData, latitudeEffSS, longitudeEffSS] = \
AverageDataset(efficiencyDict, months=['10', '11', '12', '01', '02', '03'])

[averagedEffData, latitudeEff, longitudeEff] = \
AverageDataset(efficiencyDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])




[averagedLaiNorthernSummerData, latitudeLaiNS, longitudeLaiNS] = \
AverageDataset(laiDict, months=['04', '05', '06', '07', '08', '09'])

[averagedLaiSouthernSummerData, latitudeLaiSS, longitudeLaiSS] = \
AverageDataset(laiDict, months=['10', '11', '12', '01', '02', '03'])

[averagedLaiData, latitudeLai, longitudeLai] = \
AverageDataset(laiDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])




[averagedInsolNorthernSummerData, latitudeInsolNS, longitudeInsolNS] = \
AverageDataset(insolDict, months=['04', '05', '06', '07', '08', '09'])

[averagedInsolSouthernSummerData, latitudeInsolSS, longitudeInsolSS] = \
AverageDataset(insolDict, months=['10', '11', '12', '01', '02', '03'])

[averagedInsolData, latitudeInsol, longitudeInsol] = \
AverageDataset(insolDict, \
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
# ------------------------------------------------------------------------------------------------ #




# ------------------------------------------------------------------------------------------------ #


effVMin = -0.01
effVMax = 0.01

MapPlotCP(averagedEffNorthernSummerData, latitudeEffNS, longitudeEffNS, "Efficiency Averaged April-September. Northern Hemisphere Summer.", \
xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Eff: ", vmin=effVMin, vmax=effVMax, showPlots=False)

MapPlotCP(averagedEffSouthernSummerData, latitudeEffSS, longitudeEffSS, "Efficiency Averaged October-March. Southern Hemisphere Summer.", \
xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Eff: ", vmin=effVMin, vmax=effVMax, showPlots=False)

MapPlotCP(averagedEffData, latitudeEff, longitudeEff, "Annual Average Efficiency", \
xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Eff: ", vmin=effVMin, vmax=effVMax, showPlots=False)



saveBaseDir = \
'Plots/'

nppSaveDir = saveBaseDir + '/' + 'NPP_1month'
laiSaveDir = saveBaseDir + '/' + 'LAI_1month'
insolSaveDir = saveBaseDir + '/' + 'INSOL_1month'
effSaveDir = saveBaseDir + '/' + 'EFFICIENCY_1month'
effLAISaveDir = saveBaseDir + '/' + 'EFFICIENCY_LAI_1month'


ensure_dir(nppSaveDir)
ensure_dir(laiSaveDir)
ensure_dir(insolSaveDir)
ensure_dir(effSaveDir)
ensure_dir(effLAISaveDir)


MakeMapPlotSeriesCP(laiDict, timeStamps, laiSaveDir, xWidth=11, yWidth=8.5, scale=1.4, dpi=80, \
titleText="Leaf Area Index: ", vmin=0, vmax=8, showPlots=False, filePrefix='LAI_')

# ------------------------------------------------------------------------------------------------ #





