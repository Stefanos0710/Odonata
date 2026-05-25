
"""
1. make ssh connection with the drone
2. install mav proxy
3. setup fc wiht mission planner, to enable the UR ports
4.  set the boud rate to 115200 +set the protocol to mavlink 2
5. make the connection between the pi and fc: 
    1. ssh connection to the pi
    2  cd .local/bin
    3.  python3 mavproxy.py -- master=/dev/serial0 -- baudrate 115200 -- aircraft MyCopter       <-- install maxproxy 
"""

import time
from pymavlink import mavutil

# build the connection to the flight controller
master = mavutil.mavlink_connection('/dev/serial0', baud=115200)  

# activate the motors
master.arducopter_arm()

# test move the motor 1 at 20% throttle for 2 seconds
master.mav.command_long_send(
    1, # system id of the fc
    0, # autopilot mode of the fc
    mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST, 
    0, # confirmation
    1, # motor number 1
    0, # throttle value in percentage 
    20, # throttle value in percentage
    2, # time in seconds of the test
    0, # -
    0, # -
    0  # -
)

#wait for 5 seconds
time.sleep(5)

# disconnet the motors
master.arducopter_disarm()

print("finished!")

# disconnect the connection to the flight controller
master.close()
