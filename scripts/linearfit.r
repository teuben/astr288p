# This is a script in the R language, taken from http://www.astro.umd.edu/~harris/ASTR610_F16/linearfit.r
#
# make some data (the # makes a comment in the script)
x = (1:10)*0.2
y = x*3-4
# add a little noise
y = y + rnorm(length(y), 0, 0.2)

# do the fit
lmfit = lm(y~x)
# print out the fit parameters
print(lmfit)

# make a plot of the data
plot(x, y, xlab='x label', ylab='y label')
# plot the fit in a red dashed line
abline(lmfit, col='red', lty=2)
