import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn import linear_model
from matplotlib import pyplot as plt

data = pd.read_csv('student-mat.csv', sep=';')
dict = {
    'no': 0,
    'yes': 1
}

for item in dict:
    data.internet = dict[item]

data = data[['studytime', 'failures', 'absences', 'internet', 'freetime', 'G1', 'G2', 'G3']]
predict = 'G3'

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.1)
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print(accuracy)

