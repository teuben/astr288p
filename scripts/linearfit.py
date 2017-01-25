#! /usr/bin/env python
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy  import stats

# make some data (the # makes a comment in the script)
x = (np.arange(10)+1)*0.2
y = x*3-4
# add a little noise
y = y + np.random.normal(0.0,0.2,len(x))

# do the fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

# print out the fit parameters
print(slope,intercept)

# compute the line
yfit = intercept + slope * x

# make a plot of the data
plt.scatter(x, y)
# plot the fit in a red dashed line
plt.plot(x, yfit, color='red', linestyle='dashed')
# labels
plt.xlabel("x label")
plt.ylabel("y label")
# save
plt.savefig("Pplots.pdf")
# on screen
plt.show()
