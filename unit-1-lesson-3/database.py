# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:43:16 2015

@author: emmebroo
"""

import sqlite3 as lite
import pandas as pd

# Connect to the database
con = lite.connect('/Users/emmebroo/Google Drive/Correlate/thinkful/challenge.db')

# Table data
cities = (('New York City', 'NY'),
                    ('Boston', 'MA'),
                    ('Chicago', 'IL'),
                    ('Miami', 'FL'),
                    ('Dallas', 'TX'),
                    ('Seattle', 'WA'),
                    ('Portland', 'OR'),
                    ('San Francisco', 'CA'),
                    ('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January', 62),
                     ('Boston', 2013, 'July', 'January', 59),
                     ('Chicago', 2013, 'July', 'January', 59),
                     ('Miami', 2013, 'August', 'January', 84),
                     ('Dallas', 2013, 'July', 'January', 77),
                     ('Seattle', 2013, 'July', 'January', 61),
                     ('Portland', 2013, 'July', 'December', 63),
                     ('San Francisco', 2013, 'September', 'December', 64),
                     ('Los Angeles', 2013, 'September', 'December', 75))

with con:
    
    cur = con.cursor()
    
    # Create tables. Drop tables if they already exist.
    cur.execute("drop table if exists cities")
    cur.execute("drop table if exists weather")
    cur.execute("create table cities(name text, state text)")
    cur.execute("create table weather(city text, year integer, warm_month, cold_month, average_high)")
    
    # Insert data into two tables
    cur.executemany("insert into cities values(?,?)", cities)
    cur.executemany("insert into weather values(?,?,?,?,?)", weather)
    
# Join the tables together
query = "select name, state from cities inner join weather on name = city group by city having warm_month = 'July'"

# Load into data frame
df = pd.read_sql(query, con)

# Assign data to variables
together = df.apply(lambda x:'%s, %s' % (x['name'],x['state']),axis=1)

# Print data
print "The cities that are warmest in July are:", ', '.join(together.tolist())



    
    