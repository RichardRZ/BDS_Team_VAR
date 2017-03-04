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

print "Saving dataset as pickle"
saveData(df)

print df

#print "2) Performing logistic regression on training set:"
#logisticRegression(dataFinal)

#pd.set_option('display.max_rows', None)