
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

def flight_control_loop():
    # start the drone and get the connection to the flight controller and arm
    master = turn_on_drone()
    motor.arm_drone(master)
    
    # take off to 1 meter altitude
    motor.takeoff_drone(master, target_altitude=1.0)

    # fly forward for 1 meter and then back
    for _ in range(2):
        # rotate the drone by 180 degrees
        motor.yaw_drone(master, yaw_rate=180, duration=2)

        # fly forward for 1 meter
        motor.move_drone(master, direction="front", speed=0.5, distance=1.0, stopping_distance=0.20)

    # land the drone
    motor.land_drone(master, landing_speed=0.25)

    # shutdown the drone and disconnect from the flight controller
    shutdown_drone(master)


def turn_on_drone():
    # build the connection to the flight controller
    master = mavutil.mavlink_connection('/dev/serial0', baud=115200)  

    # wait until the first heartbeat is received
    master.wait_heartbeat()
    print("Successfully connected to the flight controller")

    # here comes the logic of the drone

    return master

def shutdown_drone(master):
    """Shut down the drone"""
    # disconnet the motors
    master.arducopter_disarm()

    print("finished!")

    # disconnect the connection to the flight controller
    master.close()

