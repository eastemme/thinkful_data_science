# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 07:56:56 2015

@author: emmebroo
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm


# ==============================
# CLEANING THE DATA

#read data into dataframe
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove % symbol from interest rate and convert to float
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

#remove "month" at the end of loan length and convert to integer
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

#create a new column called Fico Score with lower limit value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]


# ==============================
# CREATING THE LINEAR MODEL

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()

x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()