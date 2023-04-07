import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# create mock data
data = {
    'Light': [500, 1000, 2000, 4000, 8000],
    'Temperature': [20, 22, 24, 26, 28],
    'Soil': [20, 40, 60, 80, 100],
    'Water': [20, 40, 60, 80, 100],
    'Humidity': [20, 40, 60, 80, 100],
    'Life Expectancy': [30, 35, 40, 45, 50]
}
df = pd.DataFrame(data)

# separate the features and target variable
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# train a linear regression model on the data
model = LinearRegression()
model.fit(X, y)

def predict_life_expectancy():
    # get user input for environmental factors
    light = float(input("Enter the light intensity (in foot-candles): "))
    temperature = float(input("Enter the temperature (in degrees Celsius): "))
    soil = float(input("Enter the soil moisture level (as a percentage): "))
    water = float(input("Enter the water level (as a percentage): "))
    humidity = float(input("Enter the relative humidity (as a percentage): "))

    # convert the input to a numpy array
    X = np.array([[light, temperature, soil, water, humidity]])

    # use the trained model to make a prediction
    life_expectancy = model.predict(X)

    # return the predicted life expectancy
    return life_expectancy[0]

predicted_life_expectancy = predict_life_expectancy()
print("Predicted life expectancy: {:.2f} days".format(predicted_life_expectancy))
5