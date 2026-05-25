
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

from pymavlink import mavutil
import motor

# build the connection to the flight controller
master = mavutil.mavlink_connection('/dev/serial0', baud=115200)  

# wait until the first heartbeat is received
master.wait_heartbeat()
print("Successfully connected to the flight controller")

# here comes the logic of the drone

"""Shut down the drone"""
# disconnet the motors
master.arducopter_disarm()

print("finished!")

# disconnect the connection to the flight controller
master.close()