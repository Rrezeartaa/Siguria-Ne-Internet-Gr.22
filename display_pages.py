
        p.place(x=100,y=50)

        def versioni():
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
