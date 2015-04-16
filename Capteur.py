#! /usr/bin/python
# -*- coding: utf-8 -*-

class Capteur:
    def __init__(self):
        self.baurate = 115200
        self.meusures = 2088
        self.resultats=[]
        self.tini=range(self.meusures)
        self.t=range(2048)

    def start(self):
        ser = serial.Serial('/dev/ttyACM1', self.baudrate)
        if(ser.readline()==b'A\r\n'):
            ser.write(b'1')
            print('Démarage des meusures')
            for i in self.tini:
                self.resultats.append(int(ser.readline().decode().rstrip('\r\n')))
            print('meusures terminées')
        #On enlève les meusures fausses
        del self.resultats[0:32]
        del self.resultats[len(self.resultats)-8:len(self.resultats)]

        #On normalise
        self.resultats=[-x for x in self.resultats]
        mini = min(self.resultats)
        self.resultats=[x - mini for x in self.resultats]
        maxi = max(self.resultats)
        self.resultats=[x/maxi for x in self.resultats]

    def calibrer(self):
        pass
