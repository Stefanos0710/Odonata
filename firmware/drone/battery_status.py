import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading

class Battery:
    def __init__(self):
        # first initialize the i2c bus
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)

        # AIN2 is cell3 where the whole battery voltage is measured
        self.battery_voltage_channel = AnalogIn(self.ads, ADS.P2)

        # voltage factor to get the real voltage, after it was decided by the R16 3.3k Ohm and R17 10k Ohm voltage divider
        self.voltage_divider_ratio = 4.31

        # is the battery status thread running
        self.running = False

        # the current battery percentage
        self.battery_percentage = float(None)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.battery_status)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def get_battery_percentage(self):
        return self.battery_percentage

    def battery_status(self):
        while self.running:
            # read the raw voltage from the battery channel
            raw_voltage = self.battery_voltage_channel.value * self.voltage_divider_ratio

            # calculate the percentage of the battery (3C Lipo battery, 9V is 0% and 12.6V is 100%)
            battery_percentage = ((raw_voltage - 9.0) / (12.6 - 9.0)) * 100
            battery_percentage = max(0, min(100, battery_percentage))  # Ensure it's within 0-100%

            self.battery_percentage = battery_percentage

            time.sleep(2)  # update every 2 seconds