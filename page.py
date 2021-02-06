from tkinter import *

active_page = []

class Page(Frame):

    def __init__(self, parent):
    
        self.width = 600
        
        self.height = 600
        
        try:
        
            active_page[0].delete()
            
        except
        
