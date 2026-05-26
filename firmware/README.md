# Firmware

In this part of the repository, you will find the software for Odonata. It is separated into [Drone](https://github.com/Stefanos0710/Odonata/blob/main/firmware/drone) and [Server](https://github.com/Stefanos0710/Odonata/blob/main/firmware/server).

In the drone folder, you will find the code and logic used to handle communication between the Raspberry Pi Zero 2 W and the flight controller, read the sensors, control the servo motor, monitor the battery status, stream the camera feed, and, of course, control the 4 motors.

In the server folder, you will find the server-side code and logic. This handles receiving information and commands sent from the drone to the server, and hosts the website where the drone and its logic are controlled.
