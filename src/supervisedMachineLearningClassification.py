import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

data = datasets.load_iris()

print(data.keys())
#print(data["DESCR"])

df = pd.DataFrame(data["data"], columns=data["feature_names"])


df["target"] = data["target"]


print(df.head())
df["sepal length (cm)"].hist()



df["target_name"] = df["target"].map({0: "setosa", 1 :"versocilor", 2:"virginica"})


col = "sepal length (cm)"
sns.relplot(x=col, y="target", hue="target_name", data=df)
plt.suptitle(col)
sns.pairplot(df, hue="target_name")
plt.show()





