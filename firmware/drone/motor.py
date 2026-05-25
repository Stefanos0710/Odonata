from pymavlink import mavutil
import tof_sensor

def arm_drone(master):
    print("Arming motors...")
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,
        1, 0, 0, 0, 0, 0, 0
    )
    time.sleep(2) # Give motors time to spin up safely


def motor(motor_number, throttle_value, time_seconds):
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

def takeoff():
    """here we need sensor number 2 (one that is facing downwards) to measure the distance to the ground, and then we can use that distance to take off to a certain height"""

    