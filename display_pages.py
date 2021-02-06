from page import *
from tkinter import *
import requests 
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def_bg = "#201F1E"
def_fg = "lightgrey"

class HomePage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)

        s = Label(self, text="Diçka rreth XSS", bg=def_bg, fg=def_fg,font=("Bold",20))
        t = Label(self,text="Sulmuesi injekton skriptën arbitrare (zakonisht në JavaScript) \nnë lokacion legjitim apo në aplikacion në internet. \nAjo skriptë pastaj ekzekutohet brenda browser-it të viktimës.", bg=def_bg, fg=def_fg)
        r = Label(self,text="XSS do të thotë Cross-site Scripting.",bg=def_bg, fg=def_fg)
        
        s.place(x=160, y=50)
        t.place(x=100, y=100)
        r.place(x=160, y=150)
        
class SettingsPage(Page):    
        
    def __init__(self, parent):

        Page.__init__(self, parent)
        t = Text(self, width=50, height=20, font=("Bold",12))
        t.place(x=50, y=100)

        def get_all_forms(url):
            soup = bs(requests.get(url).content, "html.parser")
            return soup.find_all("form")
        
        def get_form_details(form):         
            details = {}
            action = form.attrs.get("action").lower()
            method = form.attrs.get("method", "get").lower()
            inputs = []
            for input_tag in form.find_all("input"):
                input_type = input_tag.attrs.get("type", "text")
                input_name = input_tag.attrs.get("name")
                inputs.append({"type": input_type, "name": input_name})
            details["action"] = action
            details["method"] = method
            details["inputs"] = inputs
            return details
        
        def submit_form(form_details, url, value):
            target_url = urljoin(url, form_details["action"])
            inputs = form_details["inputs"]
            data = {}
            for input in inputs:
                if input["type"] == "text" or input["type"] == "search":
                    input["value"] = value
                input_name = input.get("name")
                input_value = input.get("value")
                if input_name and input_value:
                    data[input_name] = input_value

            if form_details["method"] == "post":
                return requests.post(target_url, data=data)
            else:
                return requests.get(target_url, params=data)
