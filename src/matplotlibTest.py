import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#plt.plot(x, y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple Line Plot")


import seaborn as sns
sns.lineplot(x=[1, 2, 3], y=[4, 5, 6])
# plt.show()


import pandas as pd

df = pd.read_csv(r"c:/Users/cindy/Documents/VSCode Playground/src/currencyPriceData.csv")
print(df.head())
print(df["Currency"])
print(df["Rate"].mean())
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("Simple Line Plot")
plt.show()