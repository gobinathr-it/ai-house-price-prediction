import pandas as pd
from sklearn.linear_model import LinearRegression

# load dataset
data = pd.read_csv("data.csv")

X = data[['area','bedrooms']]
y = data['price']

# train model
model = LinearRegression()
model.fit(X,y)

# user input
area = int(input("Enter area: "))
bedrooms = int(input("Enter bedrooms: "))

# prediction
prediction = model.predict([[area, bedrooms]])

print("Predicted Price:", prediction[0])