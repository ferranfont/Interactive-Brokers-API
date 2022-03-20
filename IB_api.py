from ib_insync import *
import pandas as pd
print(pd.__version__)

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=14)
stock = Forex('GBPUSD')

bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='100 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)
df1 = util.df(bars)
df1.describe()
print(df1.describe())
