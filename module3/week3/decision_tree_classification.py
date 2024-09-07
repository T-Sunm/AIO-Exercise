from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


# Load the diabetes dataset
iris_x, iris_y = datasets.load_iris(return_X_y=True)

# Split train:test = 8:2

x_train, x_test, y_train, y_test = train_test_split(
    iris_x, iris_y,
    test_size=0.2,
    random_state=42
)

# Define model
dt_classifier = DecisionTreeClassifier(
    random_state=42,
    criterion="gini",
    min_samples_split=10,
    max_depth=5,
    min_samples_leaf=5
)
# Train
dt_classifier.fit(x_train, y_train)

# Predict and evaluate
y_pred = dt_classifier.predict(x_test)
print(accuracy_score(y_test, y_pred))
