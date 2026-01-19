# 10 ta random son hosil qiling va sonlarni numbers.txt fayliga yozing.

import os
os.system("cls")
from random import randint

with open("random_numbers.txt", "w") as f:
    for n in range(10):
        n = randint(0,100)
        f.write(str(n) + " ")