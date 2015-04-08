#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import tkinter as tk
from tkinter import ttk
import serial

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, padding="2 2 12 12")
        master.title("Spectromètre")
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.tracer = ttk.Button(self, text="Tracer",
            command=self.tracer).grid(column=1, row=1)

        self.QUIT = ttk.Button(self, text="Quitter",
            command=root.destroy).grid(column=2, row=1)

    def tracer(self):
        f = Figure(figsize=(5,4), dpi=100)
        a = f.add_subplot(111)

        self.capteur()
        print(self.resultats)
        print(len(self.resultats))
        a.plot(self.t,self.resultats)
        self.canvas = FigureCanvasTkAgg(f, master=root)

        self.canvas.show()
        self.canvas.get_tk_widget().pack()


        #self.canvas = FigureCanvasTkAgg(f, master=root)
        #self.canvas.show()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        #self.canvas.get_tk_widget().pack()

    def capteur(self):
        baudrate = 115200
        meusures = 2088
        a=1
        b=1
        self.resultats=[]
        ser = serial.Serial('/dev/ttyACM1', baudrate)
        self.t=range(meusures)
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




root = tk.Tk()
app = Application(master=root)
app.mainloop()
