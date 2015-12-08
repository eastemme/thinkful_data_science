# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 07:56:56 2015

@author: emmebroo
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import csv


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

# create a new column called IR-TF which indicates if the interest rate is less than 12%
loansData['IR_TF'] = [(interest < .12) for interest in loansData['Interest.Rate']]

# create a column for a constant intercept
loansData['Intercept'] = 1

# create csv with loan data 
test = loansData.to_csv('loansData_clean.csv', header=True, index=False)
ind_vars = list(loansData.columns)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score'] 


# ==============================
# CREATING A LOGISTIC REGRESSION
# Determine whether or not a $10k loan with an interest rate less than or equal to 12% to a person with a FICO score of 750.

# read data from clean data into dataframe
df = pd.DataFrame(test, columns=ind_vars)

# Define the logistic regression model
logit = sm.Logit(df['IR_TF'], df[ind_vars])


