# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:54:08 2015

@author: emmebroo
"""

import pandas as pd
#from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# Split data at new lines
data = data.splitlines()

# Split data into columns
data = [i.split(',') for i in data]

column_names = data[0]  
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

# Convert Alcohol and Tobacco to floats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Combine expenditures to one number
expenditures = df['Alcohol'] + df['Tobacco']

# Find mean, median and mode
print "Combined alcohol and tabacco household expenditures:" 
print "The mean is {}".format(expenditures.mean()) 
print "The median is {}".format(expenditures.median()) 
print "There is no mode for this dataset." # stats.mode(expenditures) returns the lowest values since there is no mode.
print "The range is {}".format(max(expenditures) - min(expenditures))
print "The standard deviation is {}".format(expenditures.std()) 
print "The variance is {}".format(expenditures.var()) 




