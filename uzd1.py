""" 
Uzrakstiet programmu, kas ielasa skaitli (kā float) -
riņķa līnijas rādiusu un izvada uz ekrāna (print) 
riņķa līnijas garumu un laukumu, atbilstoši noformējot atbildi.
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
import math

rad=float(input("Ievadi rādiusu:"))
garums=float(math.pi*rad*2)
laukums=float(math.pi*(rad**2))

print("Riņķa līnijas garums ir")
print(garums)
print("un riņķa laukums ir")
print(laukums)