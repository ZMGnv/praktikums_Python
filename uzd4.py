"""
Izveidot funkciju, kura atgriež skaitļu kvadrātus, lietotāja norādītā apgabalā.
"""
import math

maz=float(input("Ievadi apgabala minimumu:"))
daudz=float(input("Ievadi apgabala maximumu:"))

a=math.ceil(maz)
b=math.floor(daudz)
x=a
while x<=b and x>=a:
    y=pow(x,2)
    print(y)
    x=x+1