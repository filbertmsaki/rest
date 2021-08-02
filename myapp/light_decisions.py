import RPi.GPIO as IO 
import time 
import requests
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

IO.setwarnings(False)
IO.setmode(IO.BCM)

lst = [1,2,3,4]

IO.setup(14,IO.OUT)
IO.setup(15,IO.OUT)
IO.setup(18,IO.OUT)

IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(25,IO.OUT)

IO.setup(8,IO.OUT)
IO.setup(7,IO.OUT)
IO.setup(1,IO.OUT)

IO.setup(17,IO.IN)
IO.setup(27,IO.IN)
IO.setup(22,IO.IN)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(26,IO.IN)

countA = 0
countB = 0
countC = 0

lst_sen1 = [17,22,6]
lst_sen2 = [27,5,26]

lst_green = [14,23,8]
lst_yellow = [15,24,7]
lst_red = [18,25,1]

global status
status = False

def automatic():
    while True: 
        if(IO.input(lst_sen1[0])==0 and IO.input(lst_sen2[0]) == 0):
            IO.output(lst_red[0], True)
            time.sleep(2)
            IO.output(lst_yellow[0], True)
            time.sleep(1)
            IO.output(lst_red[0], False)
            IO.output(lst_yellow[0], False)
            IO.output(lst_green[0], True)
            time.sleep(5)
            IO.output(lst_yellow[0], True)
            IO.output(lst_green[0], False)
            time.sleep(0.5)
            IO.output(lst_yellow[0], False)
            countA +=1
            countB = 0
            countC = 0
            road =4
            data={'count':countA, 'status':'mp','road':road}
            res = requests.post("http://10.42.0.242:8000/api/traffic/", data=data)
            print(countA)
            time.sleep(2)

        if(IO.input(lst_sen1[0])==0 and IO.input(lst_sen2[0]) == 1):
            IO.output(lst_red[0], True)
            time.sleep(2)
            IO.output(lst_yellow[0], True)
            time.sleep(1)
            IO.output(lst_red[0], False)
            IO.output(lst_yellow[0], False)
            IO.output(lst_green[0], True)
            time.sleep(5)
            IO.output(lst_yellow[0], True)
            IO.output(lst_green[0], False)
            time.sleep(0.5)
            IO.output(lst_yellow[0], False)
            countA +=1
            countB = 0
            countC = 0
            road =4
            data={'count':countA, 'status':'mp','road':road}
            res = requests.post("http://10.42.0.242:8000/api/traffic/", data=data)
            print(countA)
            time.sleep(2)

        elif (IO.input(lst_sen1[1])==0 and IO.input(lst_sen2[1]) == 0):
            IO.output(lst_red[1], True)
            time.sleep(2)
            IO.output(lst_yellow[1], True)
            time.sleep(1)
            IO.output(lst_red[1], False)
            IO.output(lst_yellow[1], False)
            IO.output(lst_green[1], True)
            time.sleep(5)
            IO.output(lst_yellow[1], True)
            IO.output(lst_green[1], False)
            time.sleep(0.5)
            IO.output(lst_yellow[1], False)
            countA =0
            countB +=1
            countC = 0
            road =5
            data={'count':countB, 'status':'mp','road':road}
            res = requests.post("http://10.42.0.242:8000/api/traffic/", data=data)
            print(countB)
            time.sleep(2)

        elif (IO.input(lst_sen1[1])==0 and IO.input(lst_sen2[1]) == 1):
            IO.output(lst_red[1], True)
            time.sleep(2)
            IO.output(lst_yellow[1], True)
            time.sleep(1)
            IO.output(lst_red[1], False)
            IO.output(lst_yellow[1], False)
            IO.output(lst_green[1], True)
            time.sleep(5)
            IO.output(lst_yellow[1], True)
            IO.output(lst_green[1], False)
            time.sleep(0.5)
            IO.output(lst_yellow[1], False)
            countA =0
            countB = 0
            countC +=1
            print(countC)
            road =6
            data={'count':countC, 'status':'mp','road':road}
            res = requests.post("http://10.42.0.242:8000/api/traffic/", data=data)
def manual(num, state):
    if num in lst:
        ser.write(str(f'{str(num)},{state},').entcode())
    else:
        IO.output(lst_green[num], True)


if (status == False):
    automatic()
else:
    manual()