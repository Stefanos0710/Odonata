# Firmware

This part of the project contains the firmware for the drone Odonata. The code is split into two parts: the software running on the drone itself and the control server with the cockpit.

## Drone (/drone)
This folder has the scripts for the drone's computer (Raspberry Pi Zero 2 W). These files:

* **main.py**: The main program that manages the drone's logic, flights and tests, runs the main loop, and handles communication with the server.
* **motor.py**: Defines commands into signals for the flight controller to move the 4 motors.
* **camera.py**: Captures and processes the video feed from the drone's camera.
* **servo.py**: Controls the movement of the servo motor.
* **tof_sensor.py**: Reads distance data from the ToF sensor (used for altitude height measurement).
* **battery_status.py**: Measures the battery percentage (converts voltage to percent).

## Server (/server)
This folder contains the cockpit and the communication scripts for the server.

* **main.py**: The backend code that hosts the server. It receives and sends commands from the drone and represents them in the Odonata cockpit.
* **frontend/**: The web-based cockpit that you open in your browser to monitor and control the drone.
  * **index.html**: The structure and layout of the control dashboard in HTML.
  * **static/script.js**: The logic of the website (handling button clicks, joystick inputs, and video streaming).
  * **static/style.css**: The styling of the website.