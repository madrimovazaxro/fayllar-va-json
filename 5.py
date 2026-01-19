# Foydalanuvchidan ismi, familiyasi, yoshi, manzili, telefon raqamini so’rang va quyidagi formatda json faylga saqlang.
# Input: Garri
# 	Poter
# 	23
# 	London
# 	+3-123-45-67
# Output: Faylda:
# {
# 	"Ism": "Garri",
# 	"Familya": "Poter",
# 	"Yosh": 23,
# 	"Manzil": "London",
# 	"Telefon": "+3-123-45-67"
# }

import os
import json
os.system("cls")

ism = input("Ism: ")
familiya = input("Familiya: ")
yosh = input("Yosh: ")
manzil = input("Manzil: ")
telefon = input("Telefon: ")

keys = ["Ism", "Familiya", "Yosh", "Manzil", "Telefon"]
values = [ism, familiya, yosh, manzil, telefon]
data = {}
for i in range(len(keys)):
    data[keys[i]] = values[i]
with open("file5.txt", "w") as f:
    json.dump(data, f, indent = 4 )
