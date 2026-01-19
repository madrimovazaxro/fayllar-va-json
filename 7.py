import os
import json 
os.system("cls")

with open("students.json", "r") as f:
    data = json.load(f)

print("Yiqilgan o'quvchilar:")
for i in data:
    if i['Yiqilgan'] == True:
        print(f"{i['student']}, ball: {i['Imtihon ball']}. Izoh: {i['Izoh']}")
