#  Telefon kitobi dasturi. Foydalanuvchilarning telefon raqamlarini saqlovchi va
#  boshqaruvchi dastur tayyorlash. JSON fayl (contacts.json) ichida 
# foydalanuvchi ismi va telefon raqami dict ko’rinishida yozilgan bo’ladi.
#  Input orqali foydalanuvchi ismini kiriting va shu ismdagi foydalanuvchining telefon raqamini chiqaring.
#  Dasturga yangi foydalanuvchi qo’shish imkoniyatini bering. 
# Bunda foydalanuvchi ismi va telefon raqamini input orqali qabul qilib,
#  u ma’lumotni JSON faylga qo’shib qo’yish.

import os
import json
os.system("cls")

with open("contacts.json", "r") as f:
    contacts = json.load(f)

print("1 - Mavjud foydalanuvchini qidirish\n2 - Yangi foydalanuvchi kiritish")
tanlov = int(input("Tanlovingiz: "))

if tanlov == 1:
    name = input("Foydalanuvchi ismi: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Bunday foydalanuvchi mavjud emas!")
elif tanlov == 2:
    name = input("Foydaluvchi ismi: ")
    number = input("Foydaluvchi  tel raqami: ")
    contacts[name] = number
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent = 4)

    print("Foydalanuvchi muvaffaqiyatli qo'shildi!")
else:
    print("Noto'g'ri tanlov!")

    
    
