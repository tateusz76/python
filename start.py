print("Hello world!")

# komentarz

a = 5
#print(type(a))

imie = "ala"
imie = imie.capitalize()

#print(imie + imie)

#print(5 + imie)

# formatowanie wyjścia
wiek = 5
print(f"{imie} ma {wiek} lat")

print("{} ma {} lat".format(imie, 5))

# listy

lista = []
lista = [1,4, "Ala", 4.5, imie, [1,2]]
print(lista)
lista[5][1]

lista.append(3)
print(lista)

lista[0] = 2
print(lista)

lista2 = lista + lista
print(lista2)

lista_nowa = list()

# słownik

slownik = {}
slownik = {"imie": "Marek",
"wiek": 35}
slownik["imie"]
print(slownik.keys())
print(slownik.values())
print(slownik.items())



def pow():
    pass

from math import *
import math as m
from math import pow 

pow()
m.pow()
