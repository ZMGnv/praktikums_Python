""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
vards=str(input("ievadi vardu:"))

if vards=="Janis":
    print("Labdien, "+vards+", pirmdienā!")
elif vards!="Janis":
    print("Uzredzēšanos!")    