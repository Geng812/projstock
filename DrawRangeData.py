import DateAgoTest
import pandas as pd
import matplotlib.pyplot as plt

from talib import abstract
from twstock import Stock

stockID = '2330'
stock = Stock(stockID)

total = []

DList = DateAgoTest('2019-07', 7)
stockData = stock.fetch_from(2019, 7)

head = ["date", "capacity", "turnover", "open", 
"high", "low", "close", "change", "transaction"]

for value in stockData:

  day = str(value[0]).split()
  
  if day[0] in DList:
  
    total.append([day[0], value[1], value[2], value[3], 
            value[4], value[5], value[6], value[7], value[8])

df = pd.DataFrame(total, columns = head)
df.set_index('date', inplace = True)
df['close'].plot(figsize=(16, 8))

plt.show()
