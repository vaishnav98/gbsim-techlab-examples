import os
import time

def clrscrn():
    with open("/dev/vcs1", "w") as oled_file:
        oled_file.write("                        ") #write 24 ' ' to blank the screen

def printintensity(intensity):
    with open("/dev/vcs1", "w") as oled_file:
        oled_file.write("light level:    {} %".format(intensity))

def getintensity():
    with open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r") as lightsensor_file:
        raw_intensity = int(lightsensor_file.readline())
    return round(raw_intensity/40.9,1)

while True:
    clrscrn()
    printintensity(getintensity())
    time.sleep(0.1)