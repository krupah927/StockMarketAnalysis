import numpy as np
import matplotlib.pyplot as plt
import pylab
count = 0
summation_max1 = []
summation_max2 = []
summation_max3 = []
summation_max4 = []
summation_max5 = []
summation_min = []
sum_gpd = []
prob_exceedance_max1 = []
prob_exceedance_max2 = []
prob_exceedance_max3 = []
prob_exceedance_max4 = []
prob_exceedance_max5 = []
prob_exceedance_min = []
sum_cv = []
wcet_max = []
wcet_min = []
p = [10 **-0.000000001,10 **-0.5,10 ** -1,10 **-1.3, 10**-1.5,10**-1.7, 10 **-2, 10 ** -2.3, 10 **-2.7, 10 ** -3, 10 ** -3.3, 10**-5, 10**-7, 10**-9, 10**-10]
p1 = [10 **0, 10 **-3, 10**-6, 10 ** -9, 10 ** -12,10 ** -15, 10 **-18]
WCET1 = [240, 241, 242, 243, 244, 245, 247, 248, 249, 250, 251, 252]
WCET = [1170,1172,1175,1178,1180]
data1 = np.loadtxt('GS17.txt', dtype = float, delimiter =',')
y_1 = sorted(data1, key=(float),reverse = True)
gev_data1 = np.multiply(y_1,1)
data2 = np.loadtxt('GS21.txt', dtype = float, delimiter =',')
y_2 = sorted(data2, key=(float),reverse = True)
gev_data2 = np.multiply(y_2,1)
data3 = np.loadtxt('GS22.txt', dtype = float, delimiter =',')
y_3 = sorted(data3, key=(float),reverse = True)
gev_data3 = np.multiply(y_3,1)


p_tick1 = []
p_tick2 = []

b = 30
#k_min1 = -0.568351413795622# GS20
#sigma_min1 = 3.108384284356629
#mu_min1 = 1.171907108947735e+03
# GEV Method               

#k_max1 =  -0.517368316225204 # GS20
#sigma_max1 = 2.719584475623592
#mu_max1 = 1.173119328100787e+03


k_min= -0.436503903491632
  # GS20
sigma_min = 0.374234725559329
mu_min = 2.380764724383187e+02
# GEV Method              

#b = 10
k_max = -0.3618435004245055
# GS20
sigma_max = 0.329235759136942
mu_max = 2.382293741091156e+02

#for max values
for i in p:
    #print i
    w = mu_max - (sigma_max/k_max)*(1-(-np.log(1-i))**(-k_max)) #gev
    #print (-(sigma_max/k_max)*(1-(-np.log(1-i))**(-k_max)))
    wcet_max.append(w)
    p_1 = (1-(1-i)**(1/b))
#print (wcet_max)    
    p_tick1.append(p_1)
print (wcet_max)

#for min values
for o in p:
    #print i
    w = mu_min - (sigma_min/k_min)*(1-(-np.log(1-o))**(-k_min)) #gev
    wcet_min.append(w)
    p_2 = (1-(1-o)**(1/b))   
    p_tick2.append(p_2)
print (wcet_min)
for j1 in wcet_min:
    count1 = 0
    for z1 in gev_data1:
        if z1 > j1:
            count1 +=1  
    summation_max1.append(count1)
print (summation_max1)
for s1 in summation_max1:
    pe_max1 = (float(s1) / (len(gev_data1)))    
    prob_exceedance_max1.append(pe_max1)
print (prob_exceedance_max1)

for j2 in wcet_min:
    count2 = 0
    for z2 in gev_data2:
        if z2 > j2:
            count2 +=1  
    summation_max2.append(count2)
print (summation_max2)
for s2 in summation_max2:
    pe_max2 = (float(s2) / (len(gev_data2)))    
    prob_exceedance_max2.append(pe_max2)
print (prob_exceedance_max2)

for j3 in wcet_min:
    count3 = 0
    for z3 in gev_data3:
        if z3 > j3:
            count3 +=1  
    summation_max3.append(count3)
print (summation_max3)
for s3 in summation_max3:
    pe_max3 = (float(s3) / (len(gev_data3)))    
    prob_exceedance_max3.append(pe_max3)
print (prob_exceedance_max3)

for j4 in wcet_min:
    count4 = 0
    for z4 in gev_data4:
        if z4 > j4:
            count4 +=1  
    summation_max4.append(count4)
print (summation_max4)
for s4 in summation_max4:
    pe_max4 = (float(s4) / (len(gev_data4)))    
    prob_exceedance_max4.append(pe_max4)
print (prob_exceedance_max4)

for j5 in wcet_min:
    count5 = 0
    for z5 in gev_data5:
        if z5 > j5:
            count5 +=1  
    summation_max5.append(count5)
print (summation_max5)
for s5 in summation_max5:
    pe_max5 = (float(s5) / (len(gev_data5)))    
    prob_exceedance_max5.append(pe_max5)
print (prob_exceedance_max5)

#print (wcet_min)
plt.plot(wcet_max,p, label = 'Expected upper bound gev method')
#plt.plot(WCET, prob_exceedance_max, label = 'Measured upper bound gev method')
plt.plot(wcet_min,p_tick2, label = 'Expected lower bound gev method')
plt.plot(wcet_min, prob_exceedance_max4, label = 'Measured value 17th November')
plt.plot(wcet_min, prob_exceedance_max1, label = 'Measured value of 20th November')
plt.plot(wcet_min, prob_exceedance_max2, label = 'Measured value 21st November')
#plt.plot(wcet_min, prob_exceedance_max3, label = 'Measured value 22nd December')
plt.plot(wcet_min, prob_exceedance_max5, label = 'Measured value 28th November')
#plt.plot(rank_data, Probccdf, label = 'Expected WCET gpd method')
#plt.plot(train_data, rankeccdf, label = 'Measured upper bound gpd method')
#plt.plot(rank_data1, Probccdf1, label = 'Expected WCET mbpta method')
#plt.plot(train_data, rankeccdf1, label = 'Measured upper bound mbpta method')
plt.yscale('log')
plt.xlabel('Price in $')
#pylab.xlim([33, 48])
plt.ylabel('Exceedance Probability')
pylab.legend(loc='lower right')
plt.title('Predicted vs. Measured for Goldman Sachs')
plt.show()

