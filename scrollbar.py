from tkinter import *
import tkinter.ttk as ttk

ScrollOnItemsList = []

class ScrollBar(Frame):
    def __init__(self, parent):
        self.height = 518
        self.width = 200

        Frame.__init__(self, parent, width=self.width, height=self.height, bg="grey")
        self.place(x=0, y=-2)
