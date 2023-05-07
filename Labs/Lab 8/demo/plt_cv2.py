import matplotlib.pyplot as plt
from pandas import *
from scipy import stats
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict


X = read_csv('cpu_usage_temp.csv', usecols=[3])
X = X.assign(t = X.index)
y = read_csv('cpu_usage_temp.csv', usecols=[2])
lr = linear_model.LinearRegression()
predicted = cross_val_predict(lr, X, y, cv=10)
plt.plot(y, predicted, 'ro')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'b-', lw=2)
plt.xlabel('Temperature C')
plt.ylabel('Predicted')
plt.title('John Laptop 2023-3-29')

plt.show()