# countries.txt faylida davlat nomlari yozilgan capitals.txt faylida davlatlarning poytaxti berilgan. 
# Yangi faylga davlatlar va poytaxtlarini birlashtirib yozing.

import os
os.system("cls")
import json

result = {}
f2 = open("capitals.txt", "r")
capitals = f2.read().split()

with open ("countries.txt", "r") as f1:
    countries = f1.read().split()
    for i in range(len(capitals)):
        result[countries[i]] = capitals[i]

with open("mamlakatlar.txt", "x") as n:
    json.dump(result, n, indent = 4)
f2.close()