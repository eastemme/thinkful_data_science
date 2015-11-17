# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:24:43 2015

@author: emmebroo
"""

from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Drop null rows
loansData.dropna(inplace=True)

# Print frequencies
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print freq

## Show histogram of data
#plt.figure(1)
#loansData.hist(column='Open.CREDIT.LINES')
#plt.show()
#plt.close()

# Show bar chart of frequencies
plt.figure(2)
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
plt.close

# Perform a chi-squared test
chi, p = stats.chisquare(freq.values())
print chi
print p

