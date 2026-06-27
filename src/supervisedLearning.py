from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

features = [[1, 0], [2, 1], [3, 1], [4, 0]]
labels = [0, 0, 1, 1]

train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.5, random_state=42
)

model = DecisionTreeClassifier()
model.fit(train_features, train_labels)

predictions = model.predict(test_features)
print(predictions)