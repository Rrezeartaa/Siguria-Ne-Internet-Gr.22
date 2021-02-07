Ky projekt është bërë në lëndën Siguria në Internet.

Si detyrë kemi pasur zhvillimin e aplikacionit i cili përdor regular expression për të kërkuar në log fajlla të cilët mund të jenë event i sistemit operativ apo log fajlla të ndonjë app për të gjetur IP adresa të caktuara.

Aplikacionin e kemi krijuar në atë formë që të përmbajë dy faqe, njërën për një përshkrim të shkurtër të aplikacionit dhe tjetrën për testim. Pjesa për testim përmban dy textbox-a: njërin për të shënuar path-in e log fajjlit dhe njërin për shfaqjen e gjetjeve në log file.

Për të realizuar gjetjen në log files duhet së pari të shënojmë path-in e log file në textbox-in e parë në mënyrë që të shfaqen gjetjet e caktuara nga log file. Nëse shkruajmë diçka i cili nuk është log file, atëherë paraqitet një mesazh në textbox-in e dytë se çfarë kemi shkruar nuk është log file. Nëse e shkruajmë path-in e gabuar apo nuk shkruajmë asgjë, atëherë paraqitet mesazhi në textbox-in e dytë se log file i caktuar nuk ekziston.

Në këtë aplikacion ofrohet edhe mundësia për ruajtjen e rezultateve në një text file të caktuar. Këtë mund ta bëjmë duke klikuar në butonin Ruaj... Në këtë rast hapet një pop-up ku paraqitet një textbox ku duhet të shkruajmë path-in e text file ku dëshirojmë të ruajmë rezultatin. Nëse file nuk është text file, atëherë paraqitet një mesazh, nëse kemi shkruar një text file atëherë pop-up mbyllet dhe rezultati ruhet në atë file me sukses.
