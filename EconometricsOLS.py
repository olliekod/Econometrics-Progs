from math import ceil

####################################################
#                    FUNCTIONS                     #
def findXbar(Xarr):
	summ = 0
	for i in range(len(Xarr)):
		summ += Xarr[i]
	return summ* (1/len(Xarr))

def findYbar(Yarr):
	summ = 0
	for i in range(len(Yarr)):
		summ += Yarr[i]
	return summ* (1/len(Yarr))

#Find B1hat
def B1hat(Xarr, Yarr, XBar, YBar):
	numerator = 0
	for i in range(len(Xarr)):
		a = (Xarr[i]-XBar)*(Yarr[i]-YBar)
		numerator += a

	denominator = 0
	for i in range(len(Xarr)):
		d = (Xarr[i]-XBar)**2
		denominator += d

	B1hat = numerator/denominator
	return B1hat
#Find B0hat
def B0hat(B1hat, Xbar, Ybar):
	return (Ybar-(B1hat*Xbar))


def fittedY(B0hat, B1hat, Xarr):
	fittedYarr = []
	for i in range(len(Xarr)):
		fittedYarr.append(ceil((B0hat + (B1hat * Xarr[i])) * 10000) / 10000)
	#Returns fitted Y array
	return fittedYarr


def residualArr(Yarr, fittedArray):
	resArr = []

	for i in range(len(Yarr)):
		resArr.append(ceil((Yarr[i] - fittedArray[i]) * 10000) / 10000)
	
	return resArr


def findSST(Yarr, YBar):
	fin = 0

	for i in range(len(Yarr)):
		fin += ((Yarr[i] - YBar)**2)
	return ceil((fin) * 10000) / 10000

def findSSR(residualArr):
	fin = 0

	for i in range(len(residualArr)):
		fin += residualArr[i]**2

	return ceil((fin) * 10000) / 10000

def findSSE(SST, SSR):
	return (ceil((SST-SSR) * 10000) / 10000)

def findYhat(B0hat, B1hat, Xbar):
	return (B0hat + (B1hat*Xbar))

def findR2(SSE, SST):
	return (SSE/SST)
#                                                        #
##########################################################
# ! ! ! ! ! ! ! DONT ALTER WHATS DOWN HERE ! ! ! ! ! ! ! #

print("Enter each X value, separated by a comma like this: \n1, 2.4, 3.12, 4, etc: ")
Xvalues = input()
Xval_str = Xvalues.split(',')
Xarray = list(map(float, Xval_str))

print("Now enter each Y value, separated by a comma like previously: ")
Yvalues = input()
Yval_str = Yvalues.split(',')
Yarray = list(map(float, Yval_str))

print("The two sets of values are:")
print(f"X Values: {Xarray}")
print(f"Y Values: {Yarray}")


Xbar_done = findXbar(Xarray)
Ybar_done = findYbar(Yarray)
B1hat_done = B1hat(Xarray, Yarray, findXbar(Xarray), findYbar(Yarray))
B0hat_done = B0hat(B1hat(Xarray, Yarray, findXbar(Xarray), findYbar(Yarray)), findXbar(Xarray), findYbar(Yarray))
FittedYarray = fittedY(B0hat_done, B1hat_done, Xarray)
ResidualArray = residualArr(Yarray, FittedYarray)
Yhat_done = findYhat(B0hat_done, B1hat_done, Xbar_done)
SST = findSST(Yarray, Ybar_done)
SSR = findSSR(ResidualArray)
SSE = findSSE(SST, SSR)
Rsquared = findR2(SSE, SST)

print(f"""
X Bar = {Xbar_done}
Y Bar = {Ybar_done}
B1hat = {B1hat_done}
B0hat = {B0hat_done}
Fitted Y Values: {FittedYarray}
Residuals (Ui): {ResidualArray}
SST (Sum of Squares of Total) = {SST}
SSR (Sum of Squares due to Regression) = {SSR}
SSE (Sum of Squares of Errors) =  {SSE}
R^2 = {Rsquared}
	  """)
