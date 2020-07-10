#Soru1
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")

tarih = input("Istediginiz tarihi GG/AA/YYYY seklinde giriniz: ")
girilen = datetime.strptime(tarih, "%d/%m/%Y")
print ("Girilen tarih:", girilen.strftime("%d %B %Y"))

#Soru2
sayi= int(input("Bir 0-16 arasında bir sayı giriniz: "))
if(sayi>=0 and sayi<9):
    faktoriyel = 1
    for i in range(sayi*3):
        faktoriyel *= i + 1
    print(faktoriyel)
elif(sayi>=9 and sayi<16):
    cift = 0
    for i in range(1, int(sayi)+1):
        if (i % 2 == 0):
            cift += i
    print(cift)
else:
    print("Yanlış bir sayı girişi yaptınız.")

#Soru3
import numpy as np
import string
import random

boyut = 3
anahtar = np.matrix([[1, 2, -1], [2, 5, 2], [-1, -2, 2]])
metin = 'furkankabadayif'
alfabe = string.ascii_lowercase
sifre = ""
for index, i in enumerate(metin):
    values = []
    if index % boyut == 0:
        for j in range(0, boyut):
            if(index + j < len(metin)):
                values.append([alfabe.index(metin[index + j])])
            else:
                values.append([random.randint(0,25)])
        vector = np.matrix(values)
        vector = anahtar * vector
        vector %= 26
        for j in range(0, boyut):
            sifre += alfabe[vector.item(j)]
print(sifre)

#Soru4
f = []
for u in range(1,4):
    if u > 1:
        for r in range(2,u):
            if u % r ==0:
                break
        else:
            f.append(u)
print(f)
