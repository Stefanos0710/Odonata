from pymavlink import mavutil
import tof_sensor
import time
import math

def arm_drone(master):
    """
    Arm the drone by sending the appropriate command to the flight controller.
    
    """
    print("Arming motors...")
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,
        1, 0, 0, 0, 0, 0, 0
    )
    time.sleep(2) # Give motors time to spin up safely


def test_motor(master, motor_number, throttle_value, time_seconds):
    """
    Test a specific motor by sending a motor test command.

    :param motor_number: the number of the motor to test (1-4)
    :param throttle_value: the throttle value in percentage (0-100)
    :param time_seconds: the duration of the test in seconds
    """
    # activate the motors
    arm_drone(master)

    master.mav.command_long_send(
        1, # system id of the fc
        0, # autopilot mode of the fc
        mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST, 
        0, # confirmation
        motor_number, # motor number
        0, # throttle  in percentage 
        throttle_value, # throttle value in percentage
        time_seconds, # time in seconds of the test
        0, # -
        0, # -
        0  # -
    )


def takeoff(master, target_altitude=1.0, climbing_speed=0.3):
    """
    here we need sensor number 2 (one that is facing downwards) to measure the distance to the ground, and then we can use that distance to take off to a certain height

    :param target_altitude: the target altitude in meters
    :param climbing_speed: the climbing speed in m/s
    """
    # changing to GUIDED_NOGPS mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')

    # wait a bit to ensure the mode is changed
    time.sleep(1)

    # activate the motors
    arm_drone(master)

    # convert the target altitude int milimeters, because the distance from the sensor is measured in milimeters
    target_altitude_mm = target_altitude * 1000

    # chnaging climbing speed to negative, beacause the mavlinkt takes negative values for climbing up and positive values for climbing down
    climb_speed = -abs(climbing_speed)

    print(f"Taking off to {target_altitude} meters with climbing speed of {climbing_speed} m/s")

    while True:
        distance = tof_sensor.get_distances()[2] # get the distance from the sensor number 2, which is facing downwards

        if distance >= target_altitude_mm*0.95: # if the drone is at 95% of the target altitude, we can stop climbing
            print(f"Reached target altitude of {target_altitude} meters")
            break

        master.mav.set_position_target_local_ned_send(
            0, # time_boot_ms
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000110111000111, # type_mask (only vertical velocity is enabled)
            0, 0, 0, # x, y, z positions (not used)
            0, 0, climb_speed, # x, y, z velocity in m/s
            0, 0, 0, # x, y, z acceleration (not used)
            0, 0 # yaw, yaw_rate (not used)
        )
        
        # wait a bit before the next command <- drone is controlled every 100ms
        time.sleep(0.1) 

    # now the drone has to hover in that position
    print("Entering hover mode")

    # changing to ALT_HOLD mode, to be able to hover in that position
    master.set_mode('ALT_HOLD')

    # wait a bit to ensure the mode is changed
    time.sleep(1)


def move_drone(master, direction="front", speed=0.5, distance=1.0, stopping_distance=0.5):
    """
    :param direction: the direction in which the drone should move, can be "front", "back", "left" or "right"
    :param speed: the speed at which the drone should move in m/s
    :param distance: the distance the drone should move in meters
    :param tof_sensors: the list of the tof sensors, which are used to measure the distance to the obstacles in the corresponding direction, and they are in the order of the channels (0, 1, 2, 3)
    :param stopping_distance: the distance at which the drone should stop in meters
    """

    # initialize the velocity values for the x and y direction
    vy, vx = 0.0, 0.0

    # activate the no_gps mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')
    time.sleep(1) # wait a bit to ensure the mode is changed

    if direction == "front":
        vy = speed
        sensor_index = 1
    elif direction == "back":
        vy = -speed
        sensor_index = None # we don't have a sensor facing backwards, so we can't measure the distance to obstacles in that direction, the drone has to yaw firstly and then it will move
        return 
    elif direction == "left":
        vx = -speed
        sensor_index = 3
    elif direction == "right":
        vx = speed
        sensor_index = 0
    else:
        print("Invalid direction, please choose from 'front', 'back', 'left' or 'right'")
        return
    
    # calculate the time needed to move to the target distance with the given speed and time
    time_needed = distance / speed

    # start the timer to control the movement for the calculated time
    start_time = time.time()

    # here happens the real movment logic
    while True:
        elapsed_time = time.time() - start_time
        current_distance = tof_sensor.get_distances()[sensor_index]

        # if the sensor send a error value, becasue the distance is to far, we rely on the time to control the movement
        if current_distance == 8190 or current_distance == 8191 or current_distance == 0: 
            print("Distance measurement error, moving for the calculated time")

            # if the elapsed time is greater than or equal to the calculated time, we can stop the movement, because we reached the target distance
            if elapsed_time >= time_needed:
                print(f"Reached target distance of {distance} meters")
                break
        
        # if the sensor send valid distances, we use the distance control
        else:
            # if the current distance is less than or equal to the stopping distance, we stop the movement to avoid collision
            if current_distance <= distance*1000 or current_distance <= stopping_distance*1000: 
                print(f"Reached stopping distance of {stopping_distance} meters, stopping to avoid collision")
                break

        # here we will now happen the movement command

        master.mav.set_position_target_local_ned_send(
            0, # time_boot_ms
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000111111000111, # type_mask (only horizontal velocity is enabled)
            0, 0, 0, # x, y, z positions (not used)
            vx if 'vx' in locals() else 0, vy if 'vy' in locals() else 0, 0, # x, y, z velocity in m/s
            0, 0, 0, # x, y, z acceleration (not used)
            0, 0 # yaw, yaw_rate (not used)
        )

        time.sleep(0.1) # for the next command after 100ms becasue we have to keep 10Hz control of the drone

    # here comes if the drone is to close to an object and stoping distance is overreached, go backwards for a half second
    if current_distance <= stopping_distance*1000:
        print("Too close to an object, moving backwards for 0.5 seconds to avoid collision")
        master.mav.set_position_target_local_ned_send(
            0, # time_boot_ms
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000111111000111, # type_mask (only horizontal velocity is enabled)
            0, 0, 0, # x, y, z positions (not used)
            -vx if 'vx' in locals() else 0, -vy if 'vy' in locals() else 0, 0, # x, y, z velocity in m/s
            0, 0, 0, # x, y, z acceleration (not used)
            0, 0 # yaw, yaw_rate (not used)
        )
        time.sleep(0.5)

    # now the drone has to hover in that position
    print("Entering hover mode")
    master.set_mode('ALT_HOLD')
    time.sleep(1) # wait a bit to ensure the mode is changed


def yaw_drone(master, yaw_rate=90, duration=2):
    """
    Yaw the drone in a specific direction with a specific yaw rate for a specific time.

    :param yaw_rate: the yaw positive values for right and negative values for left in degrees
    :param duration: the time for which to yaw the drone in seconds
    """

    # activate the no_gps mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')
    time.sleep(1) # wait a bit to ensure the mode is changed

    # calculate the yaw rate in radians per second -> mavlink takes yaw rate in radians per second
    yaw_rate_rad_s = yaw_rate * (math.pi / 180)

    start_time = time.time()

    # here happens the real yawing logic, with a mask to only control the yaw rate: 0b010111100111
    while time.time() - start_time < duration:
        # here comes the movment with mask to only control the yaw rate: 0b010111100111
        master.mav.set_position_target_local_ned_send(
            0, # time_boot_ms
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b010111100111, # type_mask (only yaw rate is enabled)
            0, 0, 0, # x, y, z positions (not used)
            0, 0, 0, # x, y, z velocity in m/s (not used)
            0, 0, 0, # x, y, z acceleration (not used)
            0, # yaw rate in radians per second, yaw in degrees (not used)
            yaw_rate_rad_s
        )
        time.sleep(0.1) # for the next command after 100ms becasue we have to keep 10Hz control of the drone

    # now the drone has to hover in that position
    print("Entering hover mode")
    master.set_mode('ALT_HOLD')
    time.sleep(1) # wait a bit to ensure the mode is changed
