from numpy import mean, array
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel, legend
from scipy.optimize import curve_fit


# ------------------------------------------------------------------------------------------------ #
def LinearFunction(x, a, b):
	return a + x*b
# ------------------------------------------------------------------------------------------------ #


linearFitToEfficiency = curve_fit(LinearFunction, months, globallyAveragedEfficiencies)

figure()
plot(array(months), globallyAveragedEfficiencies, label='Averaged Data')
xlabel("Time since July 2006 (months)")
ylabel("Globally Averaged Photosynthetic Efficiency")

plot(array(months), LinearFunction(array(months), linearFitToEfficiency[0][0], \
linearFitToEfficiency[0][1]), label='Linear Fit')

legend()

show()