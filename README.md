# GreenGuess

## Plant Life Expectancy Predictor
This code uses machine learning to predict the life expectancy of a plant based on environmental factors such as light intensity, temperature, soil moisture level, water level, and relative humidity.

## Installation
This code requires the following dependencies:

* NumPy
* Pandas
* Scikit-learn

To install these dependencies, you can use:

pip install numpy pandas scikit-learn
## Usage
Select a plant by entering a number between 1 and 3:

1. Spider Plant
2. Snake Plant
3. Pothos

Enter environmental factors:

* Light intensity (in foot-candles)
* Temperature (in degrees Celsius)
* Soil moisture level (as a percentage)
* Water level (as a percentage)
* Relative humidity (as a percentage)

View the predicted life expectancy in days.

## Mock Data
The mock data for this code was generated using arbitrary values for each plant and environmental factor. You can modify or replace this data with real data by editing the SpiderPlant, SnakePlant, and Pothos dictionaries.

## Raspberry Pi Network
The network is comprised of a server (currently just a computer running the server script) and clients (Raspberry Pi Pico W microcontrollers). The idea is to have each client be responsible for reading one sensor and sending the data to the server in order to be stored and processed. Since each client only gathers and reports data, the network has star topology with each client only being able to communicate with the server. 

The network is created by a router disconnected from the Internet, which creates a private LAN (intranet). 

The clients communicate using TCP sockets via the Python sockets library. 
