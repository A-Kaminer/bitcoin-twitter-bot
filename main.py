import pandas_datareader as pdr
import python-twitter
import matplotlib as plt
import numpy as npm

data = pdr.get_data_yahoo('BTC-USD')


high = data.High
low = data.Low
close = data.Close
opening = data.Open

print(high, low, close, opening)
