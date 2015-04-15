#! /usr/bin/python
# -*- coding: utf-8 -*-

class Capteur:
    def __init__(self):
        self.baurate = 115200
        self.meusures = 2088
        self.resultats=[]
        self.t=[]

    def start1(self):
        ser = serial.Serial('/dev/ttyACM1', self.baudrate)
        self.t=range(self.meusures)
        if(ser.readline()==b'A\r\n'):
            ser.write(b'1')
            print('Démarage des meusures')
            for i in self.t:
                self.resultats.append(int(ser.readline().decode().rstrip('\r\n')))
            print('meusures terminées')
        #On enlève les meusures fausses
        del self.resultats[0:32]
        del self.resultats[len(self.resultats)-8:len(self.resultats)]
        self.t=range(len(self.resultats))

        #On normalise
        self.resultats=[-x for x in self.resultats]
        mini = min(self.resultats)
        self.resultats=[x - mini for x in self.resultats]
        maxi = max(self.resultats)
        self.resultats=[x/maxi for x in self.resultats]
