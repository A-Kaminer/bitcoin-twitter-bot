import pandas_datareader as pdr
import pandas as pd
import twitter
import matplotlib.pyplot as plt
import numpy as npm
import os
import datetime

'''
Tweet format:
    Today bitcoin's price changed by {change}%. It opened at {opening} and
    closed at {close}. The high was {high}, and the low was {low}, resulting in
    a range of {range}. {Graph of today} {Graph of this month} {Graph of 365 days}
'''

def plot():
    # plot the month
    fig = plt.figure()
    fig.suptitle("The price of BTC")

    mplot = fig.add_subplot(2, 1, 1)
    mplot.set_xlabel("Date")
    mplot.set_ylabel("Price (USD)")
    mplot.set_title("Price over a month")
    x = month_dates
    y = month_close
    mplot.plot_date(x, y, xdate=True, linestyle='solid')

    # plot the year
    yplot = fig.add_subplot(2, 1, 2)
    yplot.set_xlabel("Date")
    yplot.set_ylabel("Price (USD)")
    yplot.set_title("Price over a year")
    x = year_dates
    y = year_close
    mplot.plot_date(x, y, xdate=True, linestyle='solid')

    

data = pdr.get_data_yahoo('BTC-USD')

dates = data.index.day

high_all = npm.round(data.High, 2)
low_all = npm.round(data.Low, 2)
close_all = npm.round(data.Close, 2)
opening_all = npm.round(data.Open, 2)

year_dates = dates[-365:]
year_close = close_all[-365:]

month_dates = dates[-30:]
month_close = close_all[-30:]

high = high_all[-1]
low = low_all[-1]
close = close_all[-1]
opening = opening_all[-1]
high_low_range = npm.round(high - low, 2)
percent_change = npm.round((close - opening) / opening * 100, 2)

if high_low_range <= 500:
    volatility = "low"
elif high_low_range <= 1500:
    volatility = "medium"
elif high_low_range <= 5000:
    volatility = "high"
else:
    volatility = "insane"

tweet = f"Today, bitcoin's (BTC-USD) price changed by {percent_change}%. It opened at ${opening} and closed at ${close}. The high was ${high}, and the low was ${low}, resulting in a range of ${high_low_range}. This suggests {volatility} volatility. Take a look at the month and year graphs below."

if volatility == "insane":
    tweet += " I would take a look to see what's happening!"



print(tweet)
#print(month_dates)
#plot()
#plt.show()
# print(year_dates)
