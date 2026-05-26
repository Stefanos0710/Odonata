import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15 import AnalogIn
import threading

# first initialize the i2c bus
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# AIN2 is cell3 where the whole battery voltage is measured
battery_voltage_channel = AnalogIn(ads, ADS.P2)

# voltage factor to get the real voltage, after it was decided by the R16 3.3k Ohm, osthat
voltage_divider_ratio = 4.31

def get_battery_status():
    # read the raw voltage from the battery channel
    raw_voltage = battery_voltage_channel.value * voltage_divider_ratio
    
    # calculate the percentage of the battery (3C Lipo battery, 9V is 0% and 12.6V is 100%)
    battery_percentage = ((raw_voltage - 9.0) / (12.6 - 9.0)) * 100
    battery_percentage = max(0, min(100, battery_percentage))  # Ensure it's within 0-100%

    return battery_percentage