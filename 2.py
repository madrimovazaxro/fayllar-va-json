# Faylda sonlar probel bilan ajratib yozilgan(bir qatorda). Shu fayldagi sonlarning 
# kvadrat ildizlarini ildiz.txt fayliga yozing.
# Input: faylda:     16 36 25 49 81
# Output: ildiz.txt: 4 6 5 7 9

import os
from math import sqrt
import json
os.system("cls")

with open("file2.txt", "r") as f1:
    numbers = f1.read().split()
    numbers2 = list(map(int, numbers))
    squares = []
    for num in numbers2:
        num2= (sqrt(num))
        squares.append(num2)
with open("ildiz.txt", "w") as f2:
    # f2.write(str(squares))
    json.dump(squares, f2)