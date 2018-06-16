from dateutil.parser import parse
import pandas as pd

df = pd.read_csv("AAPL.csv", delimiter=",")
first_hundred = df.head(100)

print(type(first_hundred.close[0]))
first_hundred.date = first_hundred.date.apply(lambda x: parse(x).strftime('%Y-%m-%d'))
first_hundred.close = first_hundred.close.apply(lambda x : float(x))
# first_hundred.close = first_hundred.close.apply(lambda x : float(x))
first_hundred.close = first_hundred.close[first_hundred.close>=0.513393]


print("first_hundred : ",len(first_hundred))
new_close_prices = []
for i in first_hundred.close.values:
    new_close_prices.append(float(i))
print("new_close_prices : ",new_close_prices)
new_close_prices = pd.DataFrame({"close":new_close_prices})
# new_close_prices = pd.DataFrame(new_close_prices)

print(new_close_prices.head())
print("mean : ",new_close_prices.close.mean())
print("Max  : ",new_close_prices.close.max())
print("Min  : ",new_close_prices.close.min())
print("Variance : ",new_close_prices.close.var())
print("Mode : ",new_close_prices.close.mode())
# print("Mode : ",new_close_prices.close.stddev())


# Calculate Mean of Close Price for first hundred entries
# output1 = first_hundred.close.mean()
# print("output1 : ",output1)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Date')
ax.set_ylabel('Closing price ($)')
ax.plot(first_hundred.date, first_hundred.close, label="AAPL")
plt.show()
