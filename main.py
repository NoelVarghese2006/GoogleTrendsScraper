from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time

import numpy as np
import tensorflow as tf
# from tensorflow.keras import layers, models


pytrends = TrendReq(hl="en-US", tz = 360)
count = int(input("Enter how many items you wish to compare: "))
kw_list = []
for i in range(count):
    kw_list.append(input("Enter keyword " + str(i+1) + ": "))
pytrends.build_payload(kw_list, timeframe='today 12-m')
time.sleep(60)
data = pytrends.interest_over_time()
print(data)
print(len(data))
data.plot(figsize=(10,6))
plt.title('Keyword Popularity Over Time')
plt.xlabel('Date')
plt.ylabel('Interest')


plt.show()
