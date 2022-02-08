import pandas_datareader as pdr
import pandas as pd
import tweepy
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


class Data:
    def __init__(self):
        self.data = pdr.get_data_yahoo("BTC-USD")
        self.high_all = npm.round(self.data.High, 2)
        self.low_all = npm.round(self.data.Low, 2)
        self.close_all = npm.round(self.data.Close, 2)
        self.opening_all = npm.round(self.data.Open, 2)
        self.dates_all = self.data.index
    

    def get_year_dates(self):
        return self.dates_all[-365:]


    def get_year_close(self):
        return self.close_all[-365:]


    def get_month_dates(self):
        return self.dates_all[-30:]


    def get_month_close(self):
        return self.close_all[-30:]


    def get_day_high(self):
        return self.high_all[-1]


    def get_day_low(self):
        return self.low_all[-1]


    def get_day_close(self):
        return self.close_all[-1]


    def get_day_opening(self):
        return self.opening_all[-1]


    def get_high_low_range(self):
        return npm.round(self.get_day_high() - self.get_day_low(), 2)


    def get_percent_change(self):
        return npm.round((self.get_day_close() - self.get_day_opening()) / self.get_day_opening() * 100, 2)




def plot(month_dates, month_close, year_dates, year_close):
    # plot the month
    fig, plots = plt.subplots(1, 2)
    fig.suptitle("Price of BTC-USD")

    x = month_dates
    y = month_close
    plots[0].plot_date(x, y, xdate=True, linestyle='solid')
    plots[0].set_xlabel("Date")
    plots[0].set_ylabel("Price (USD)")
    plots[0].set_title("Price of bitcoin over a month")

    x = year_dates
    y = year_close
    plots[1].plot_date(x, y, xdate=True, linestyle='solid')
    plots[1].set_xlabel("Month")
    plots[1].set_ylabel("Price (USD)")
    plots[1].set_title("Price of bitcoin over a year")

    


def write_tweet(percent_change, opening, close, high, low, high_low_range):
    if abs(high_low_range) <= 1500:
        volatility = "low"
    elif abs(high_low_range) <= 3500:
        volatility = "medium"
    elif abs(high_low_range) <= 10000:
        volatility = "high"
    else:
        volatility = "insane"

    tweet = f"Today, bitcoin's (BTC-USD) price changed by {percent_change}%. It opened at ${opening} and closed at ${close}. The high was ${high}, and the low was ${low}, resulting in a range of ${high_low_range}. This suggests {volatility} volatility. Take a look at the month and year graphs below."

    return tweet




def main():
    # get data and plot it, then save the figure as figure.png
    data = Data()
    plot(data.get_month_dates(), data.get_month_close(), data.get_year_dates(), data.get_year_close())
    plt.savefig("figure.png")
    
    tweet = write_tweet(data.get_percent_change(), data.get_day_opening(), data.get_day_close(), data.get_day_high(), data.get_day_low(), data.get_high_low_range())
    print(tweet)

if __name__ == "__main__":
    main()
