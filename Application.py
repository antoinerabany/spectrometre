#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import tkinter as tk
from tkinter import ttk

from Capteur import Capteur
from Converter import wav2RGB

from numpy import arange, sin, pi, outer, ones, array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.colors as col

from matplotlib.figure import Figure

class Application(ttk.Frame):

    helium_max1=435
    helium_max2=546

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, padding="5 2 12 12")
        master.title("Spectromètre")
        self.capteur = Capteur()
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.pack()
        self.createWidgets()

        self.f = Figure(figsize=(5,6), dpi=100)
        self.ax = self.f.add_subplot(211)
        self.ax2 = self.f.add_subplot(212,axisbg='k')
        self.canvas = FigureCanvasTkAgg(self.f, master=root)

        self.toolbar = NavigationToolbar2TkAgg( self.canvas, root )
        self.toolbar.update()

        self.canvas.show()
        self.canvas.get_tk_widget().pack()


        #canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


    def createWidgets(self):
        self.tracer = ttk.Button(self, text="Acquisition",
            command=self.tracer).grid(column=1, row=1)

        self.calibrer = ttk.Button(self, text="Calibrer",
            command=self.calibrer).grid(column=2, row=1)

        self.QUIT = ttk.Button(self, text="Quitter",
            command=root.destroy).grid(column=3, row=1)

        self.max1 = tk.StringVar()
        self.max2 = tk.StringVar()

        self.max1_entry = ttk.Entry(self, width=7,
            textvariable=self.max1).grid(column=4, row=1)

        self.max2_entry = ttk.Entry(self, width=7,
            textvariable=self.max2).grid(column=5, row=1)

    def tracer(self):
        self.ax.clear()
        self.capteur.start()
        self.ax.plot(self.capteur.t,self.capteur.resultats)
        if(self.capteur.calibre):
            res = []
            for x in range(10):
                a=[]
                for i,y in enumerate(self.capteur.t):
                    a.append(wav2RGB(y,alpha=abs(self.capteur.resultats[i])))
                res.append(a)
            self.ax2.imshow(res,aspect='auto',
                extent=(self.capteur.t[0],self.capteur.t[len(self.capteur.t)-1],0,1))
        self.canvas.draw()

    def calibrer(self, *args):
        try:
            value1 = float(self.max1.get())
            value2 = float(self.max2.get())
            #Calcul du pas
            pas = (self.helium_max2-self.helium_max1)/(value2-value1)
            #Calcul du point initial
            xo= self.helium_max1 - pas*value1
            #self.capteur.t = xo+pas*self.capteur.t
            self.capteur.t = [xo+pas*t for t in self.capteur.t]
            self.capteur.calibre = 1
            self.tracer
        except ValueError:
            pass

        self.ax.clear()
        self.ax.plot(self.capteur.t,self.capteur.resultats)
        if(self.capteur.calibre):
            res = []
            for x in range(10):
                a=[]
                for i,y in enumerate(self.capteur.t):
                    a.append(wav2RGB(y,alpha=abs(self.capteur.resultats[i])))
                res.append(a)
            self.ax2.imshow(res,aspect='auto',
                extent=(self.capteur.t[0],self.capteur.t[len(self.capteur.t)-1],0,1))
        self.canvas.draw()



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
