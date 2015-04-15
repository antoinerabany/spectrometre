#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import tkinter as tk
from tkinter import ttk
import serial

from Capteur import Capteur

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt

from matplotlib.figure import Figure

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, padding="2 2 12 12")
        master.title("Spectromètre")
        self.capteur = Capteur()
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.pack()
        self.createWidgets()

        self.f = Figure(figsize=(5,4), dpi=100)
        self.ax = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()

    def createWidgets(self):
        self.tracer = ttk.Button(self, text="Tracer",
            command=self.tracer).grid(column=1, row=1)

        self.QUIT = ttk.Button(self, text="Quitter",
            command=root.destroy).grid(column=2, row=1)

    def tracer(self):

        self.ax.clear()
        #self.capteur.start()
        #self.ax.plot(self.capteur.t,self.capteur.resultats)

        self.ax.plot(arange(0.0,3.0,0.01),sin(2*pi*arange(0.0,3.0,0.01)))#,color=plt.get_cmap('gist_rainbow'))
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
