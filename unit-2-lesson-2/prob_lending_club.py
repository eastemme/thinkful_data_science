# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:22:27 2015

@author: emmebroo
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Import lending data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Remove null values
loansData.dropna(inplace=True)

# Save a blox plot of amount requested
plt.figure(1)
loansData.boxplot(column="Amount.Requested")
plt.savefig("amount-requested-box-plot.svg")
plt.close()

# Save a histogram of amount requested
plt.figure(2)
loansData.hist(column="Amount.Requested", histtype="bar")
plt.savefig("amount-requested-histogram.svg")
plt.close()

# Save a QQ plot of amount requested
plt.figure(3)
graph = stats.probplot(loansData['Amount.Requested'], dist='norm', plot=plt)
plt.savefig("amount-requested-qqplot.svg")
plt.close()