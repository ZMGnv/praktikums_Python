"""
Uzrakstiet programmu Python,
lai aprēķinātu dienu skaitu starp diviem datumiem.
"""
pirmmen=float(input("Pirmā datuma mēnesis:"))
pirmdat=float(input("Pirmā datuma diena:"))
otrmen=float(input("Otrā datuma mēnesis:"))
otrdat=float(input("Otrā datuma diena:"))

x=(otrmen-pirmmen)*30
y=otrdat-pirmdat
z=x+y
print (z)