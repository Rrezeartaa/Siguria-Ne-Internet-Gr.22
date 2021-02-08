from page import *

from tkinter import *
import requests
import re
import time
from time import strftime

from pathlib import Path


def_bg = "#201F1E"

def_fg = "lightgrey"

class HomePage(Page):
    def __init__(self, parent):
        
        Page.__init__(self, parent)

        s = Label(self, text="Diçka rreth këtij aplikacioni", bg=def_bg, fg=def_fg,font=("Bold",20))
        
        t = Label(self,text="Ky aplikacion... \n.......................... \n.............................", bg=def_bg, fg=def_fg)
        
        
         r = Label(self,text="..........................................",bg=def_bg, fg=def_fg)
            
            
        t.place(x=100, y=100)
        
        s.place(x=130, y=50)
        
        r.place(x=160, y=150)
        
        
        class TestingPage(Page):    
        
        def __init__(self, parent):












        #    print("hh")

        #ruaj=Button(self,text="Ruaj daljen ne text fajll",command=fshije,bg='#7B7F7F',fg=def_fg)
              
        #ruaj.place(x=375,y=470)   
