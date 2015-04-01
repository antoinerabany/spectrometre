#! /usr/bin/python
# -*- coding: utf-8 -*-

import serial

def main():
    baudrate = 115200
    meusures = 2088
    resultats=[]
    ser = serial.Serial('/dev/ttyACM0', baudrate)
    if(ser.readline()==b'A\r\n'):
        ser.write(b'1')
    for i in range(meusures):
        resultats.append(ser.readline().decode().rstrip('\r\n'))
        #print (ser.readline())

    #terminator cr
    #A ? 1 ...2088 meusures





if __name__ == "__main__":
    main()
