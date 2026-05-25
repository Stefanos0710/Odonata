from pymavlink import mavutil
import main   

def motor(motor_number, throttle_value, time_seconds):
    # activate the motors
    master.arducopter_arm()

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
    pass