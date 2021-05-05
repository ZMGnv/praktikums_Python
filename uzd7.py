"""
Uzrakstiet Python programmu, lai iegūtu sfēras
 ar lietotāja norādītu rādiusu tilpumu.
 """
import math
rad=float(input("Sfēras radius:"))

tilp=math.pi*pow(rad, 3)*(4/3)
print ("Sfēras tilpums ir")
print (tilp)

