# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:57:47 2015

@author: emmebroo
"""

import collections
import scipy.stats as stats
import matplotlib.pyplot as plt

# The data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# Print frequencies for the data set
frequencies = collections.Counter(x)
print frequencies


# Create and save a box plot
plt.figure(1)
plt.boxplot(x)
plt.savefig("box-plot.svg")
plt.close()

# Create and save a histogram
plt.figure(2)
plt.hist(x, histtype='bar')
plt.savefig("histogram.svg")
plt.close()

# Create and save a qqplot
plt.figure(3)
qqplot = stats.probplot(x, plot=plt)
plt.savefig("qqplot.svg")
plt.close()
