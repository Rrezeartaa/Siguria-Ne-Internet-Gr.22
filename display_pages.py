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
          
        s.place(x=130, y=50)
        t.place(x=100, y=100)                
        r.place(x=160, y=150)
        
class TestingPage(Page):    
        
   def __init__(self, parent):
            
        Page.__init__(self, parent)
                
        t = Text(self, width=50, height=20, font=("Bold",12))
        t.place(x=50, y=100)

        titull = Label(self, text="Testimi", bg=def_bg, fg=def_fg,font=("Bold",18))
        titull.place(x=220, y=5)

        tt = Text(self, width=43, height=1, font=("Bold",12))
        tt.place(x=50, y=50)




        b=Button(self,text=" Kërko ",command=main,bg='#7B7F7F',fg=def_fg)
        b.place(x=460,y=50)

        b=Button(self,text="Shkruaj në file",command=shkruajNeFile,bg='#7B7F7F',fg=def_fg)
        b.place(x=420,y=470)





 
