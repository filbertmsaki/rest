import RPi.GPIO as IO 
import time 
import requests
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(18,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(1,IO.OUT)
lst_red = [18,16,1]
while True:
    IO.output(18, True)
    IO.output(16, True)
    IO.output(1, True)
