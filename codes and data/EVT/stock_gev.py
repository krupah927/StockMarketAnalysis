import numpy as np
import math
import pylab
import scipy.stats
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from pylab import *
from math import exp, expm1
from matplotlib import pyplot
sum = 0
Expected_sum = 0
chi_square_sum = 0
chi_square_sum_new = 0
y = np.loadtxt('AMZN30.txt', dtype = float, delimiter =',')
print(y)
y_1 = sorted(y, key=(float))
b = 10
k =  -0.507368316225204 # GS20
sigma = 2.719584475623592
mu = 1.173119328100787e+03
#k= -0.554304428926347   # min  for 520 data initial.txt
#sigma = 2.861643859457927
#mu = 1.041507049467601e+03
#k = 0.204955529329468  # block size = 5
#sigma = 0.189998696076679
#mu = 33.817381945183328
#k = 0.207394622839910 #  block size = 10#
#sigma = 0.18990014441652
#mu = 33.817313929456716
#k = 0.212268692064482 #  block size = 20
#sigma = 0.189758702011169
#mu = 33.817178133370192
#k = 0.214709035799699 #  block size = 25
#sigma = 0.189709675150231
#mu = 33.817119080633518
result = [max(y_1[i:i+b]) for i in range(0, len(y_1), b)]
y_2 = np.multiply(result,1)
print (y_2)
print (len(y_2))
N = len(y)
print (N)
Nb = (N/b)
print(N/b)
nb1 = ceil(Nb)
nb = int(nb1)
print (nb)
N_bins = ceil(Nb/10.0)
n_b = int(N_bins)
mean = np.mean(y_2)
std = np.std(y_2)
r_min = min(y_2)
x_list = []
for i in range(1,nb+1):
    x =  mu - (sigma/k)*(1-(-math.log((i)/(Nb+1)))**(-k)) 
    x_list.append(x)
r_max = max(y_2)
print (len(x_list))
(m,b) = polyfit(x_list,y_2 , 1)
#print (mean)
count = 0
#print (b)Nb
yp = polyval([m,b],(x_list))
#print (yp)
plt.plot(x_list,yp, 'r')
plt.scatter(x_list,y_2, color = 'green')
#pylab.ylim([33, 39])
plt.xlabel(' Quantiles')
plt.ylabel('Empirical Quantiles')
plt.title('QQ-Plot of Block Maximum Values for stock values')
plt.show()
Expected_samples_list = []
Observed_samples_list = []
range_min_list = []
range_max_list = []
#print (r_min)
#print (r_max)
for c in range(1, n_b+1):
    count = 0
    for z in y_2: 
        range_min = r_min + ((r_max-r_min)/N_bins)*(c-1)
        range_max = r_min + ((r_max-r_min)/N_bins)*(c)
        if range_min <= z <= range_max :
            count = count +1     
    Observed_samples = count
    Observed_samples_list.append(Observed_samples)   
    prob_min = exp(-(1+k*((range_min-mu)/sigma))**(-1/k)) #Calculation of prob_min(lower bin edge)
    prob_max = exp(-(1+k*((range_max-mu)/sigma))**(-1/k)) # Calculation of prob_max(upper bin edge)
    Expected_samples = Nb * (prob_max- prob_min)
    Expected_samples_list.append(Expected_samples)
    chi_square = np.sum((Observed_samples-ceil(Expected_samples))**2/ceil(Expected_samples))
    chi_square_sum += chi_square
    range_min_list.append(range_min)
    range_max_list.append(range_max)
print (Observed_samples_list)
#print (chi_square_sum)
print (ceil(Expected_samples_list))
chi_square_func = scipy.stats.chisquare(f_obs = Observed_samples_list, f_exp=ceil(Expected_samples_list))
print (chi_square_func) 
#print (range_min_list)
#print (range_max_list)
index = 0
x = []
range_max_new_list = []
range_min = r_min
prob_next_min_list = []
range_min_new_list = []
h = plt.hist(y_2, bins=n_b, alpha = 1, label = 'Observed samples')
plt.plot(range_min_list,Expected_samples_list, label='Expected_samples')
plt.xlabel('Stock Price ($)')
plt.ylabel('Number of Observations')
pylab.legend(loc='upper right')
plt.title('Fit of stock data for chi-square test')
plt.show()
for y1 in Observed_samples_list :
    sum += y1
    index += 1        
    if sum >= 5:                          
        x.append(sum)              
        sum = 0
        range_max_new = r_min + ((r_max-r_min)/N_bins)*(index)
        range_max_new_list.append(range_max_new)
        range_min_new = r_min + ((r_max-r_min)/N_bins)*(index)
        range_min_new_list.append(range_min_new)              
del range_min_new_list[-1]       
range_max_new = r_min + ((r_max-r_min)/N_bins)*(index)
z = sum + x[len(x)-1]
new = range_min_new_list.insert(0, range_min)# inserting the range_min value to the range_min_new_list
range_maximum = np.array(range_max_new_list)
range_maximum[len(x)-1]= range_max_new
#print range_max_new_list
S = np.array(x)
#print (range_min_new_list)
#print (range_maximum.tolist())
S[len(x)-1] = z
print (S.tolist())
#print (range_maximum)
min_new = np.array(range_min_new_list)
#print (min_new)
prob_next_min_new = np.exp(-(1+k*((min_new-mu)/sigma))**(-1/k))
prob_next_max_new = np.exp(-(1+k*((range_maximum-mu)/sigma))**(-1/k))
#print (ceil(Expected_new.tolist()))
#print (prob_next_min_new.tolist())
#print (prob_next_max_new.tolist()) 
Expected_new = Nb * (prob_next_max_new- prob_next_min_new)
print (ceil(Expected_new))
chi_new = np.sum((S-ceil(Expected_new))**2/ceil(Expected_new))
chi_square_sum_new += c
#print chi_new
#print (chi_square_sum_new)
chi_square_function = scipy.stats.chisquare(f_obs = S, f_exp=ceil(Expected_new))
print (chi_square_function)
mx = (max(range_maximum.tolist()))
c = (range_min_new_list.insert(2,mx))
range_hist_bin= sorted(range_min_new_list,key=(float))
#print (range_hist_bin)
h = plt.hist(y_2, bins= min_new, alpha = 1, label = 'Observed samples')
plt.plot(min_new,Expected_new, label='Expected_samples')
plt.xlabel('Stock Price ($)')
plt.ylabel('Number of Observations')
pylab.legend(loc='upper right')
plt.title('Fit of stock data for chi-square test after combining bins')
plt.show()

