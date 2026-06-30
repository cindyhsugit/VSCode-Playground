import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV  
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("c:/Users/cindy/Documents/VSCode Playground/src/titanicDataset.csv")
data.info()
print(data.isnull().sum())

def preprocess_data(df):
    # Drop irrelevant columns
    df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)
    df = df.dropna()
    df.fillna({"Embarked": "S"}, inplace=True)
    # Fill missing values
    df.drop(columns=["Embarked"], inplace=True)

    df["Sex"] = df["Sex"].map({"male": 1, "female": 0}) 

    df["FamilySize"] = df["SibSp"] + df["Parch"] 
    df["isAlone"] = np.where(df["FamilySize"] == 0, 1, 0)
    df["FareBin"] = pd.qcut(df["Fare"], 4, labels=False)
    return df

print(data.info)


data = preprocess_data(data)
X = data.drop(columns=["Survived"]) 
y = data["Survived"]

# X front of flashcards, y back of flashcards
# Only give front of flashcards
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# ML Processing
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def tune_model(X_train, y_train):
      param_grid = {
          "n_neighbors":range(1,21),
          "metric":["euclidean", "manhattan", "minkowski"],
          "weights":["uniform", "distance"]
     }

      model = KNeighborsClassifier()
      grid_search = GridSearchCV(model, param_grid, cv=5,n_jobs=-1)
      grid_search.fit(X_train, y_train)
      return grid_search.best_estimator_

best_model = tune_model(X_train, y_train)

def evaluate_model(model, X_test, y_test):
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)
    matrix = confusion_matrix(y_test, prediction)
    return accuracy, matrix

#accuracy, matrix = evaluate_model(best_model, X_test, y_test)





