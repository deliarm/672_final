from calendar import month
from turtle import clear
from numpy import full
import yfinance as yf
import full_company_names
import pandas as pd
import csv

START_MONTH = 1
START_DAY = 1
START_YEAR = 2010
END_MONTH = 1
END_DAY = 1
END_YEAR = 2022

START_DATE = "{}-{}-{}".format(START_YEAR, START_MONTH, START_DAY)
END_DATE = "{}-{}-{}".format(END_YEAR, END_MONTH, END_DAY)

data = yf.download(full_company_names.ticker_set1,start=START_DATE, end=END_DATE,interval="1mo")[['Close']]
data = data.transpose()
data.to_excel("output1.xlsx")

data2 = yf.download(full_company_names.ticker_set2,start=START_DATE, end=END_DATE,interval="1mo")[['Close']]
data2 = data2.transpose()
data2.to_excel("output2.xlsx")

data3 = yf.download(full_company_names.ticker_set3,start=START_DATE, end=END_DATE,interval="1mo")[['Close']]
data3 = data3.transpose()
data3.to_excel("output3.xlsx")