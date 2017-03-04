#!/usr/bin/env python

import pandas as pd
import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

# Datathon project with Trip Advisor dataset by Richen Zhang, Vikram Saraph, Altan Allawala.


def saveData(df):
	df.to_pickle("datathon_pickled")

def loadData():
	df = pd.read_csv('datathon_tadata.csv')
	return df

def cleanData():
	# We can complete this
	return

print "Loading dataset"
df = loadData()

#print "Saving dataset as pickle"
#saveData(df)

del df['user_id']
del df['osTypeName']
del df['daysToCheckin']
del df['p_TotalPrice']

df['day'] = pd.to_datetime(df['day'])
df['weekday'] = df['day'].apply(lambda x: x.weekday())

minimumDate = df['day'].min(axis=1)

df['day'] = (pd.to_datetime(df['day']) - minimumDate)
#df['day'] = df['day'].apply(lambda x: x.days)

df['p_trafficChannel'] = df['p_trafficChannel'].apply(lambda x: ord(x))

print df.head(3)

#print df
