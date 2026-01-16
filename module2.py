import os
os.system('cls')

from datetime import date

yil = int(input("Yil: "))
oy = int(input("Oy: "))
kun = int(input("Kun: "))

tugilgan_sana = date(yil, oy, kun)
bugun = date.today()


kunlar_soni = (bugun - tugilgan_sana).days

print(f"{kunlar_soni} kun o'tdi")
