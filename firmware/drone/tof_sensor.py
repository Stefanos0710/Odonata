import time
import board
import busio
import adafruit_tca9548a
from adafruit_vl53l0x import VL53L0X
import threading

class ToFSensor:
    def __init__(self):
        # list to store the tof sensors
        self.tof_sensors = []

        # current distances
        self.current_distances = []

        # is it runniing?
        self.running = False

    def setup(self):
        # initialize the i2c bus 
        i2c = busio.I2C(board.SCL, board.SDA)

        # initialize the tca9548a multiplexer and set the adress to 0x70
        tca = adafruit_tca9548a.TCA9548A(i2c, address=0x70)

        # channels, which are used for the sensors
        channels = [0, 1, 2, 3]

        for channel in channels:
            # initialize the tof sensor on the corresponding channel of the multiplexer and adding it to the list of tof sensors
            tof_sensor = VL53L0X(tca[channel])
            self.tof_sensors.append(tof_sensor)

            print(f"ToF sensor on channel {channel} initialized and ready to use")

        # wait a short amount of tim to ensure all sensors are ready
        time.sleep(0.5)


    def start(self):
        # start the thread for the distance measurement loop
        self.running = True
        thread = threading.Thread(target=self.measure_distances)
        thread.start()

    def stop(self):
        # stop the thread for the distance measurement loop
        self.running = False


    def get_distances(self):
        """
        returns a list of 4 distances, representing the distances from the 4 sensors in the order of the channels (0, 1, 2, 3),
        and it is measured in milimeters
        """
        return self.current_distances

    def measure_distances(self):
        while self.running:
            # here starts the real measurment loop, which measures the distance from all sensors
            distances = []
            for channel, tof_sensor in enumerate(self.tof_sensors):
                # measure the distace from the sensor and add it to the list of the distances
                distance = tof_sensor.range
                distances.append(distance)

                # print the distance from the sensor
                print(f"Distance from sensor on channel {channel}: {distance} mm")

            # updating the current distances
            self.current_distances = distances

            # wait fro 100ms before the next measurment, sothat there are about 10 measurments per second
            time.sleep(0.1)
