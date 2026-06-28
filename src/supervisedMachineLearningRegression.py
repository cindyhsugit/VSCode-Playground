import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("c:/Users/cindy/Documents/VSCode Playground/src/Salary_dataset.csv")
print(df.head())

X = np.array(df["YearsExperience"]).reshape(-1, 1)
y = np.array(df["Salary"]).reshape(-1, 1)
print(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


plt.scatter(X, y, c='r')
plt.plot(X, y, c='b')
plt.plot(X_test, y_pred, c = 'g', linewidth = 3)
plt.show()