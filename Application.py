#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import tkinter as tk
from tkinter import ttk
import serial

from Capteur import Capteur
from Converter import wav2RGB

from numpy import arange, sin, pi, outer, ones, array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.colors as col

import colorpy

from matplotlib.figure import Figure

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, padding="3 2 12 12")
        master.title("Spectromètre")
        self.capteur = Capteur()
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.pack()
        self.createWidgets()

        self.f = Figure(figsize=(5,4), dpi=100)
        self.ax = self.f.add_subplot(211)
        self.ax2 = self.f.add_subplot(212,axisbg='k')
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()

    def createWidgets(self):
        self.tracer = ttk.Button(self, text="Tracer",
            command=self.tracer).grid(column=1, row=1)

        self.calibrer = ttk.Button(self, text="Calibrer",
            command=self.calibrer).grid(column=2, row=1)

        self.QUIT = ttk.Button(self, text="Quitter",
            command=root.destroy).grid(column=3, row=1)

    def tracer(self):
        self.ax.clear()
        #self.capteur.start()
        #self.ax.plot(self.capteur.t,self.capteur.resultats)

        self.ax.plot(arange(380,750,1),abs(sin(2*pi*arange(380,750,1)/200)))#,color=plt.get_cmap('gist_rainbow'))
        #res = abs(sin(2*pi*arange(380,780,1)))
        res = []
        for x in range(10):
            a=[]
            for y in arange(380,750):
                a.append(wav2RGB(y,alpha=abs(sin(2*pi*y/200))))
                #res[x,y] = wav2RGB(x)
            res.append(a)

                #res = outer(ones(100),[wav2RGB(x) for x in arange(380,780,1)])

        #res = [wav2RGB(x) for x in arange(380,780,1)]
        #res = outer(ones(100),arange(380,780))
        #res = outer(ones(100),abs(sin(2*pi*arange(380,780,1)/200)))
        #print(res)
        #interp = 'bilinear';
        #self.ax2.imshow(res,aspect='auto',cmap=plt.get_cmap('gist_rainbow'), extent=(350,800,0,1))
        self.ax2.imshow(res,aspect='auto',extent=(350,750,0,1))
        self.canvas.draw()

    def calibrer(self):
        pass



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
