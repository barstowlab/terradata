# Sin fit

from numpy import mean, array
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel
from scipy.optimize import curve_fit


# ------------------------------------------------------------------------------------------------ #
def HarmonicFunction(t, a0, b0, c0, alpha0, phi0, c1, alpha1, phi1, c2, alpha2, phi2):
	
	from numpy import sin
	
	harmonic = a0 + b0*t + c0*sin(alpha0*t + phi0) + c1*sin(alpha1*t + phi1) \
	+ c2*sin(alpha2*t + phi2)
	
	return harmonic	
# ------------------------------------------------------------------------------------------------ #


figure()
plot(months, globallyAveragedEfficiencies)
xlabel('Month from Start')
ylabel('Globally Averaged Photosynthetic Efficiency')

show()


# Harmonic fit to efficiency (hFtE)
hFtE = curve_fit(HarmonicFunction, months, globallyAveragedEfficiencies)


figure()
plot(array(months), globallyAveragedEfficiencies, label='Averaged Data')
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged Photosynthetic Efficiency")

plot(array(months), \
HarmonicFunction(array(months), hFtE[0][0], hFtE[0][1], hFtE[0][2], hFtE[0][3], hFtE[0][4], \
hFtE[0][5], hFtE[0][6], hFtE[0][7], hFtE[0][8], hFtE[0][9], hFtE[0][10]), \
label='Harmonic Fit')



legend()

show()

