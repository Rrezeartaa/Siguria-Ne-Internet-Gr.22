from page import *
from tkinter import *
import requests
import re
import time
from time import strftime
from pathlib import Path
from PIL import ImageTk,Image

def_bg = "#201F1E"
def_fg = "lightgrey"

class HomePage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)

        s = Label(self, text="Diçka rreth këtij aplikacioni", bg=def_bg, fg=def_fg,font=("Bold",20))
        t = Label(self,text="Ky aplikacion ka të bëjë me kërkimin në log files."+
        " \nPërdoruesi ka mundësi të japë regex-in për të gjetur ip adresa të caktuara, si: MAC adresa, \n"+
        "IP adresa të ndryshme po në bazë të regex-it mund të kërkojnë edhe gjëra të tjera në log file.", bg=def_bg, fg=def_fg, font=("Bold",12))
        s.place(x=390, y=50)
        t.place(x=240, y=100)
        image1 = Image.open("fotot/mac.png")
        imagee = image1.resize((250, 150), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(imagee)

        label1 = Label(self,image=test)
        label1.image = test
        label1.place(x=120, y=250)

        image2 = Image.open("fotot/log.png")
        imageee = image2.resize((80, 100), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(imageee)

        label2 = Label(self,image=test)
        label2.image = test
        label2.place(x=530, y=270)

        image3 = Image.open("fotot/ip.png")
        imageee3 = image3.resize((250, 150), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(imageee3)

        label3 = Label(self,image=test)
        label3.image = test
        label3.place(x=750, y=250)
        
class TestingPage(Page):    
        
   def __init__(self, parent):
            
        Page.__init__(self, parent)
                
        t = Text(self, width=50, height=20, font=("Bold",12))
        t.place(x=50, y=100)

        titull = Label(self, text="Testimi", bg=def_bg, fg=def_fg,font=("Bold",18))
        titull.place(x=220, y=5)

        tt = Text(self, width=43, height=1, font=("Bold",12))
        tt.place(x=50, y=50)

        tReg=Text(self, width=43, height=1, font=("Bold",12))
        tReg.place(x=50, y=90)
        
        lbl2=Label(self,text="",bg=def_bg,fg='red')
        lbl2.place(x=50,y=430)

        lbl3=Label(self,text="",bg=def_bg)
        lbl3.place(x=50,y=430)
        
        ipv4 = Image.open("fotot/IPv4.jpg")
        imazhi = ipv4.resize((200, 120), Image.ANTIALIAS)
        testim = ImageTk.PhotoImage(imazhi)  

        ipv6 = Image.open("fotot/ipv6.jpg")
        imazhi2 = ipv6.resize((200, 120), Image.ANTIALIAS)
        testim2 = ImageTk.PhotoImage(imazhi2)

        mac = Image.open("fotot/mac.jpg")
        imazhi3 = mac.resize((200, 120), Image.ANTIALIAS)
        testim3 = ImageTk.PhotoImage(imazhi3)

        zgjedhja = Label(self,text="Në këtë pjesë duke klikuar mbi fotografi, mund të \n"+
        "zgjedhni se çfarë dëshironi të gjeni në log file.", bg=def_bg, fg=def_fg,font=("Bold",12))

        zgjedhja.place(x=640, y=70)
        
        def main():
            t.delete('1.0','end')
            log_file_path =tt.get('1.0',"end-1c")
         
            regex=tReg.get('1.0',"end-1c")

            if ".log" not in log_file_path or not log_file_path:
                lbl2['text']="Nuk keni shkruar një log file!"
            elif not Path(log_file_path).exists():
                lbl2['text']="Nuk ekziston ky log file në këtë path!"
            else:
                lbl3['text']=""                
                lbl2['text']=""
                parseData(log_file_path, regex, read_line=True)
                
        def parseData(log_file_path, regex, read_line=True):
            with open(log_file_path, "r") as file:
                match_list = []
                if read_line == True:
                    for line in file:
                        for match in re.finditer(regex, line, re.S):
                            match_text = match.group()
                            match_list.append(match_text)
                            t.insert("1.0",match_text+"\n")
               # elif read_line==False:
                #    t.insert("1.0","Nuk u gjeten rezultate!")
                else:
                    data = file.read()
                    for match in re.finditer(regex, data, re.S):
                        match_text = match.group();
                        match_list.append(match_text)
            file.close()
            
        def shkruajNeFile():
            
                def ruaj():
                    
                    fajlli=text.get("1.0","end-1c")
                    if ".txt" not in fajlli:
                        lbl['fg']='red'
                        lbl['text'] ="Nuk keni shënuar një text file!"
                    else:                      
                        lbl3['fg']='green'
                        lbl3['text']="Rezultati u ruajt me sukses në file"
                        window.destroy()
                        with open(fajlli, "w+") as file:
                            file.write("Rezultati:\n")
                            file.write(t.get('1.0',"end-1c"))
                        file.close()                      
            
                if tt.get("1.0", END)=="\n":
                    lbl2['text']="Nuk keni shkruar asnjë log file!"
                elif t.get("1.0",END)=="\n":
                    lbl2['text']="Nuk ka asnjë rezultat që ta shkruajmë në file!"
                else:
                    lbl2['text']=""
                    window = Toplevel()
                    window.geometry("350x80")
                    lbl=Label(window,text="Shkruani file ku dëshironi të ruani daljen")
                    lbl.place(x=20,y=10)

                    btn=Button(window,text="Ruaj",command=ruaj,bg='#7B7F7F',fg=def_fg)
                    btn.place(x=270,y=28)
                    text = Text(window, width=25, height=1, font=("Bold",12))
                    text.place(x=20, y=30)  
        
        b=Button(self,text=" Kërko ",command=main,bg='#7B7F7F',fg=def_fg)
        b.place(x=460,y=50)

        b=Button(self,text="Shkruaj në file",command=shkruajNeFile,bg='#7B7F7F',fg=def_fg)
        b.place(x=420,y=470)
        
        #def fillipv4():
            
        #def fillipv6():
            
        #def fillMac():


        button1=Button(self, text = '', image = testim, command='')
        button1.image=testim
        button1.place(x=580, y=150)

        button2=Button(self, text = '', image = testim2, command='')
        button2.image=testim2
        button2.place(x=820, y=150)

        button3=Button(self, text = '', image = testim3, command='')
        button3.image=testim3
        button3.place(x=710, y=300)
        
        
        def fillipv4():
            
            t.delete('1.0','end')
            
            lbl3['text']=""              
            
             lbl2['text']=""
                
            log_file_path =tt.get('1.0',"end-1c")
            
            parseData(log_file_path, r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})", read_line=True)
            
            
            
               def fillipv6():
                    
            t.delete('1.0','end')
            
            lbl3['text']=""  
  
            lbl2['text']=""
    
            log_file_path =tt.get('1.0',"end-1c")
        
            parseData(log_file_path, r"(([0-9a-fA-F]{0,4}:){1,7}[0-9a-fA-F]{0,4})", read_line=True) #ende permiresime
            def fillMac():
                t.delete('1.0','end')
                lbl3['text']="" 

 
