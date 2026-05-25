from pymavlink import mavutil
import tof_sensor
import time

def arm_drone(master):
    print("Arming motors...")
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,
        1, 0, 0, 0, 0, 0, 0
    )
    time.sleep(2) # Give motors time to spin up safely


def motor(master, motor_number, throttle_value, time_seconds):
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



def takeoff(master, 
            target_altitude=1.0, # target altitude in meters
            climbing_speed=0.3 # climbing speed in m/s
            ):
    """here we need sensor number 2 (one that is facing downwards) to measure the distance to the ground, and then we can use that distance to take off to a certain height"""
    # changing to GUIDED_NOGPS mode, to be able to control the drone without gps
    master.set_mode('GUIDED_NOGPS')

    # wait a bit to ensure the mode is changed
    time.sleep(1)

    # activate the motors
    arm_drone(master)

    current_altitude = tof_sensor.get_distances()[2] # get the distance from the sensor number 2, which is facing downwards

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



    