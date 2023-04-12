# GreenGuess

## Introduction
TODO

## Raspberry Pi Network
The network is comprised of a server (currently just a computer running the server script) and clients (Raspberry Pi Pico W microcontrollers). The idea is to have each client be responsible for reading one sensor and sending the data to the server in order to be stored and processed. Since each client only gathers and reports data, the network has star topology with each client only being able to communicate with the server. 

The network is created by a router disconnected from the Internet, which creates a private LAN (intranet). 

The clients communicate using TCP sockets via the Python sockets library. 
