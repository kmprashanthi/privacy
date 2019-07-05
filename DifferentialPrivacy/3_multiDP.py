import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def ret_noise (salary_temp,scale):
    loc = 0.
    temp = []
    for val in salary_temp:
        temp_val = val + (np.random.laplace(loc, scale,1))
        temp.append(temp_val)
    print (salary_temp)
    return temp


d = pd.read_csv('salary_test.csv')
annual_salary = d['Salary']
#scale values computed by taking sensitivity to be 2 (global sensitivity for histogram)
scale_1 = 20    #epsilon = 0.1
scale_2 = 2     #epsilon = 1
scale_3 = 0.2   #epsilon = 10

noise_1 = ret_noise (annual_salary,scale_1)
noise_2 = ret_noise (annual_salary,scale_2)
noise_3 = ret_noise (annual_salary,scale_3)

legend = ['Plain Data', 'epsilon = 0.1' , 'epsilon = 1','epsilon = 10']

bin_spec = [0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000]
plt.hist([annual_salary,noise_1,noise_2,noise_3],bins=bin_spec,edgecolor='k')
plt.xlabel('Salary')
plt.ylabel('No of Employees')
plt.title('Employees Data')
plt.legend(legend)
plt.show()
