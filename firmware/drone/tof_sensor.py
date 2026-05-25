import time
import board
import busio
import adafruit_tca9548a
from adafruit_vl53l0x import VL53L0X

def measure_distances():
    # initialize the i2c bus 
    i2c = busio.I2C(board.SCL, board.SDA)

    # initialize the tca9548a multiplexer and set the adress to 0x70
    tca = adafruit_tca9548a.TCA9548A(i2c, address=0x70)

    # channels, which are used for the sensors
    channels = [0, 1, 2, 3]

    # list to store the tof sensors
    tof_sensors = []
    for channel in channels:
        # initialize the tof sensor on the corresponding channel of the multiplexer and adding it to the list of tof sensors
        tof_sensor = VL53L0X(tca[channel])
        tof_sensors.append(tof_sensor)

        print(f"ToF sensor on channel {channel} initialized and ready to use")

    # wait a short amount of tim to ensure all sensors are ready
    time.sleep(0.5)

    # here starts the real measurment loop, which measures the distance from all sensors
    while True:
        distances = []
        for channel, tof_sensor in int(tof_sensors.items()):
            # measure the distace from the sensor and add it to the list of the distances
            distance = tof_sensor.range
            distances.append(distance)

            # print the distance from the sensor
            print(f"Distance from sensor on channel {channel}: {distance} mm")

        return distances

        # wait fro 100ms before the next measurment, sothat there are about 10 measurments per second
        time.sleep(0.1)
