Ky projekt është bërë në lëndën Siguria në Internet.

Si detyrë kemi pasur zhvillimin e aplikacionit i cili përdor regular expressions për të kërkuar në log fajlla të cilët mund të jenë event i sistemit operativ apo log fajlla të ndonjë app për të gjetur IP adresa të caktuara dhe MAC adresa.

### Ekzekutimi

Për të filluar ekzekutimin e aplikacionit, duhet të shkoni tek fajlli ss.py dhe të klikoni në Run > Run Module. Në mënyrë që ekzekutimi të funksionojë duhet t'i instaloni libraritë të cilat mund të mos i keni me anë të komandës pip install <emri i librarisë> .

![Screenshot (9)](https://user-images.githubusercontent.com/56273238/107850004-84617680-6dff-11eb-84fa-a8206962e4ae.png)

### Pamja e aplikacionit

Aplikacionin e kemi krijuar në atë formë që të përmbajë dy faqe, njërën për një përshkrim të shkurtër të aplikacionit dhe tjetrën për testim. 

![aplikacioni](https://user-images.githubusercontent.com/56273238/107849815-fafd7480-6dfd-11eb-8833-26329b16d193.JPG)

Pjesa për testim përmban tre textbox-a: njërin për të shënuar path-in e log fajllit, njërin për të shënuar regular expression dhe tjetrin për shfaqjen e gjetjeve në log file. Në të njëjtën dritare përdoruesi ka mundësi që përmes klikimit të fotos së caktuar të gjejë rezultatet e caktuara në log file. Textbox-i i tretë përmban edhe një scrollbar që në rast që ka më shumë rezultate sesa që nxë, të mund t'i shohim.

![Screenshot (8)](https://user-images.githubusercontent.com/56273238/107849852-3d26b600-6dfe-11eb-8ffb-c6ab74a2baae.png)
 
### Rastet e testimit

Për të realizuar gjetjen në log files duhet së pari të shënojmë path-in e log file në textbox-in e parë në mënyrë që të shfaqen gjetjet e caktuara nga log file vetëm nga një herë (pra nuk shfaqen si duplikate):

![gjejIP](https://user-images.githubusercontent.com/56273238/107850346-f9ce4680-6e01-11eb-8bbc-afdc6a551ecb.JPG)

Nëse shkruajmë diçka i cili nuk është log file apo nuk shkruajmë asgjë, atëherë paraqitet një mesazh në label-in poshtë textbox-it të tretë se çfarë kemi shkruar nuk është log file. 

![loja](https://user-images.githubusercontent.com/56273238/107850157-9bed2f00-6e00-11eb-9013-11181a8ebdeb.JPG)

![pashkruar](https://user-images.githubusercontent.com/56273238/107850183-db1b8000-6e00-11eb-9878-b8a05bab9746.JPG)

Nëse e shkruajmë path-in e gabuar, atëherë paraqitet mesazhi në label-in poshtë textbox-it të dytë se log file i caktuar nuk ekziston. 

![Screenshot (10)](https://user-images.githubusercontent.com/56273238/107850230-26ce2980-6e01-11eb-99af-6945f7e0eb24.png)

Nëse përdorim metodën me anë të klikimit të fotove nuk kemi nevojë për të shkruar regular expression, por vetëm të shënojmë emrin e log. Rezultatet e gjetura paraqiten ne textbox-in e tretë:

![gjejIPv6](https://user-images.githubusercontent.com/56273238/107850318-c986a800-6e01-11eb-824d-2d3d8e538df3.JPG)

Nëse nuk shënojmë emrin e log file apo shënojmë emrin e ndonjë log file që nuk ekziston na paraqiten mesazhet e njëjta si në rastin e mëparshëm:

![pashenu](https://user-images.githubusercontent.com/56273238/107850597-e02dfe80-6e03-11eb-8a1d-b741604e1be0.JPG)

Në këtë aplikacion ofrohet edhe mundësia për ruajtjen e rezultateve në një text file të caktuar. Këtë mund ta bëjmë duke klikuar në butonin Shkruaj në file. Në këtë rast hapet një pop-up ku paraqitet një textbox ku duhet të shkruajmë path-in e text file ku dëshirojmë të ruajmë rezultatin. Më poshtë është një shembull kur pas gjetjes së rezultateve i ruajmë ato në text file: 

![Shkruajfile](https://user-images.githubusercontent.com/56273238/107849534-2aab7d00-6dfc-11eb-818a-d82bd05a4cbf.JPG)

Nëse file nuk është text file, atëherë paraqitet një mesazh se nuk kemi shënuar një text file:

![jotxtfile](https://user-images.githubusercontent.com/56273238/107850624-0ce21600-6e04-11eb-9bbf-65b532835859.JPG)

Nëse kemi shkruar një text file atëherë pop-up mbyllet dhe rezultati ruhet në atë file me sukses dhe kjo tregohet edhe me një mesazh poshtë textbox-it të dytë.

![ruaj](https://user-images.githubusercontent.com/56273238/107850633-23886d00-6e04-11eb-9c4c-c496dae8d769.JPG)

![rezultatiRuaj](https://user-images.githubusercontent.com/56273238/107850641-34d17980-6e04-11eb-8018-3089f54896c8.JPG)

Nëse nuk ka rezultat në dalje, atëherë del mesazhi poshtë textbox-it të tretë që nuk ka asnjë rezultat që të shkruhet në text file:

![skarezultat](https://user-images.githubusercontent.com/56273238/107849667-1b78ff00-6dfd-11eb-9737-052c97e142ca.JPG)

Nëse nuk kemi shënuar ndonjë log file që të dalin rezultatet e caktuara del mesazhi se nuk kemi shkruar log file:

![ruajF](https://user-images.githubusercontent.com/56273238/107858739-1dab7f80-6e36-11eb-8ce2-720a78458948.JPG)

Në kuadër të aplikacionit kemi përfshirë edhe një menubar ku përmes saj mund të dalim nga aplikacioni (Exit) si dhe të kopjojmë tekst, të zhbëjmë ndonjë veprim, etj.
Më poshtë kemi pamjet se çfarë përmban menubar:

![screenshot](https://user-images.githubusercontent.com/56273238/107850702-a3163c00-6e04-11eb-9401-8675da30e07b.png)

![screenshot2](https://user-images.githubusercontent.com/56273238/107850715-b45f4880-6e04-11eb-8e35-ea05e33922a9.png)


Për të realizuar këtë aplikacion jemi bazuar në tutoriale të ndryshme për tkinter:

https://pythonicways.wordpress.com/2016/12/20/log-file-parsing-in-python/

https://www.tutorialspoint.com/python/tk_scrollbar.htm

http://etutorials.org/Programming/Python+tutorial/Part+III+Python+Library+and+Extension+Modules/Chapter+16.+Tkinter+GUIs/16.9+Tkinter+Events/
