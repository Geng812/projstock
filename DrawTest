#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

from talib import abstract
from twstock import Stock

stock = Stock('2330')

df = pd.DataFrame(stock.fetch_from(2019,7))

df.set_index('date', inplace = True)

df['close'].plot(figsize=(16, 8))

plt.show()
