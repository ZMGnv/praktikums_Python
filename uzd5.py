"""
Uzrakstiet programmu Python, 
kas pieņem veselu skaitli (n) un 
aprēķina n + nn + nnn vērtību.
"""

n=float(input("Ievadi vesalu skaitli:"))

x=n+pow(n, 2)+pow(n, 3)
print(x)
"""
def skaitlis(n):
    y=n+pow(n, 2)+pow(n,3)
    return y
print(skaitlis(2))
"""