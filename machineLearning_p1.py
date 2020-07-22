# Libraries needed
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn import linear_model

# Student grades dataset
data = pd.read_csv('student-mat.csv', sep=';')

# Converting string values to integer values
dict = {
    'no': 0,
    'yes': 1
}

for item in dict:
    data.internet = dict[item]

    
# Choosing features in the dataset
data = data[['studytime', 'failures', 'absences', 'internet', 'freetime', 'G1', 'G2', 'G3']]

# Choosing label
predict = 'G3'

# Setting features as array X
X = np.array(data.drop([predict], 1))

# Setting the label as array y
y = np.array(data[predict])

# Randomly splitting training and testing data. 90% is training and 10% is testing.
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.1)

# Creating the model
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)

# Printing the accuracy of the model
print(accuracy)
