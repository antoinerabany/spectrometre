#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import tkinter as tk
from tkinter import ttk

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

        self.QUIT = tk.Button(self, text="Quitter", fg="red",
            command=root.destroy).grid(column=2, row=1)

    def tracer(self):
        f = Figure(figsize=(5,4), dpi=100)
        a = f.add_subplot(111)
        t = arange(0.0,3.0,0.01)
        s = sin(2*pi*t)

        a.plot(t,s)

        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
