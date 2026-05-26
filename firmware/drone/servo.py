from gpiozero import AngularServo
import time

# the gpio pin for the servo
gpio_pin = 18 

# safe angle range for the servo
min_angle = -90
max_angle = 90

# define the servo
servo = AngularServo(gpio_pin, min_angle=min_angle, max_angle=max_angle)

def calibrate_servo():
    # calibrate the servo
    servo.angle = 0
    time.sleep(1)

def move_servo(angle):
    # confirm and potentially adjust the angle to be within the safe zone
    safe_angle = max(min_angle, min(max_angle, angle)) # ensure the angle is within the safe range

    # move the servo to desired angle
    servo.angle = safe_angle
