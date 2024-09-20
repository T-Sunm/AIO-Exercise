from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import MinMaxScaler

# Load_dataset
machine_data, machine_labels = datasets.fetch_openml(
    name='machine_cpu', return_X_y=True)

# scaler = MinMaxScaler()
# machine_data = scaler.fit_transform(machine_data)

x_train, x_test, y_train, y_test = train_test_split(
    machine_data, machine_labels,
    test_size=0.2,
    random_state=42
)


tree_reg = DecisionTreeRegressor(random_state=0, max_depth=3)

tree_reg.fit(x_train, y_train)
y_pred = tree_reg.predict(x_test)

print(mean_squared_error(y_test, y_pred))
