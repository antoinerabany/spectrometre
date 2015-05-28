#! /usr/bin/python
# -*- coding: utf-8 -*-
import serial

class Capteur:
    def __init__(self):
        self.baurate = 115200
        self.meusures = 2088
        self.tini=range(self.meusures)
        self.t=range(2048)
        self.calibre=0

    def start(self):
        ser = serial.Serial('/dev/ttyACM0', self.baurate)
        if(ser.readline()==b'A\r\n'):
            ser.write(b'1')
            print('Démarrage des mesures')
            self.resultats=[]
            for i in self.tini:
                self.resultats.append(int(ser.readline().decode().rstrip('\r\n')))
            print('mesures terminées')
        #On enlève les meusures fausses
        del self.resultats[0:32]
        del self.resultats[len(self.resultats)-8:len(self.resultats)]

        #On normalise
        self.resultats=[-x for x in self.resultats]
        mini = min(self.resultats)
        self.resultats=[x - mini for x in self.resultats]
        maxi = max(self.resultats)
        self.resultats=[x/maxi for x in self.resultats]
        for i,r in enumerate(self.resultats):
            if(r<0.2):
                self.resultats[i]=0

    def calibrer(self):
        pass
