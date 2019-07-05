import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

d = pd.read_csv('salary_test.csv')
annual_salary = d['Salary']
bin_spec = [0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000]
plt.hist(annual_salary,bins=bin_spec,edgecolor='k')
plt.xlabel('Salary')
plt.ylabel('No of Employees')
plt.title('Histogram plot against Salary and the No of Employees')
plt.show()
