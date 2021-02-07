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
        titull = Label(self, text="Testimi", bg=def_bg, fg=def_fg,font=("Bold",18))
        titull.place(x=220, y=5)
        
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
        
        def printoi():
            t.delete("1.0","end")
            t.insert('1.0', '\nOpsionet në këtë aplikacion janë:\n\n -version - tregon versionin e aplikacionit\n -h - shfaq ndihmën \n -u URL - performon skanimin mbi URL-në e caktuar\n -i READFILE - lexon URL-të nga një fajll\n')

        p=Button(self,text="Ndihma",command=printoi,bg='#7B7F7F',fg=def_fg)
        p.place(x=100,y=50)

        def versioni():
            t.delete('1.0','end')
            t.insert('1.0', 'Version - 1.1\nAplikacioni i krijuar nga Grupi22')

        r=Button(self,text="Versioni",command=versioni,bg='#7B7F7F',fg=def_fg)
        r.place(x=255,y=50)

        def scan_xss():
            
            url=t.get('1.0',"end-1c")
            if "http:" not in url:
                t.delete('1.0','end')
                t.insert("1.0","Shenoni emrin e url në formën e duhur!")
            else:
                forms = get_all_forms(url)
                js_script = "<script>alert('hi')</scripT>"

                for form in forms:
                    form_details = get_form_details(form)
                    content = submit_form(form_details, url, js_script).content.decode()
                    if js_script in content:
                        
                        t.delete("1.0","end")
                        t.insert("1.0",form_details)
                        t.insert("1.0",f"\n[*] Detajet e formes:\n")
                        t.insert("1.0",f"\n[+] XSS në {url}")                
                        t.insert('1.0',f"[+] Janë vërejtur {len(forms)} forma në {url}.")
                    else:
                        
                        t.delete("1.0","end")
                        t.insert("1.0","Nuk kërcënohet nga XSS")
            
        q=Button(self,text="Skano URL",command=scan_xss,bg='#7B7F7F',fg=def_fg)
        q.place(x=170,y=50)
                       
        def scan_xssFile():

            fajlli=t.get('1.0',"end-1c")
            
            if ".txt" not in fajlli:
                t.delete('1.0','end')
                t.insert("1.0","Shënoni emrin e fajllit në formën e duhur!")
                
            else:
                file1 = open(fajlli, 'r')
                Lines = file1.readlines()
                t.delete('1.0','end')
                for line in Lines:
                    forms = get_all_forms(line)
                    js_script = "<Script>alert('hi')</scripT>"
                    is_vulnerable = False
                    for form in forms:
                        form_details = get_form_details(form)
                        content = submit_form(form_details, line, js_script).content.decode()
                        if js_script in content:
                            t.insert("1.0",form_details)
                            t.insert("1.0",f"\n[*] Detajet e formes:\n")
                            t.insert("1.0",f"\n[+] XSS në {line}")                
                            t.insert('1.0',f"[+] Janë vërejtur {len(forms)} forma në {line}.")
                        else:
                            t.insert("1.0",f"\n\n"+line.strip()+" nuk kërcënohet nga XSS\n")
        
                     
        z=Button(self,text="Skano fajllin me URL",command=scan_xssFile,bg='#7B7F7F',fg=def_fg)
        z.place(x=330,y=50)

        def fshije():
            t.delete('1.0','end')

        fshi=Button(self,text="Fshije përmbajtjen",command=fshije,bg='#7B7F7F',fg=def_fg)
        fshi.place(x=50,y=470)

       # def ruajDaljen():
        #    print("hh")

        #ruaj=Button(self,text="Ruaj daljen ne text fajll",command=fshije,bg='#7B7F7F',fg=def_fg)
        #ruaj.place(x=375,y=470)   
