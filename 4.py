# Fayl ichida inglizcha gap berilgan. Shu gapni o’zbekchasini yangi tarjima.txt faylga yozing. 
# (translate modulidan foydalaning)
# Input: faylda:   Hi, I'm a student of Najot Ta'lim.
# Output: faylda: Salom, men Najot Ta'lim o'quvchisiman.

from translate import Translator
translator = Translator(from_lang="en", to_lang='uz')

f1 = open("tarjima.txt", 'w')
with open("file4.txt") as f:
    text = f.read()
    translation = translator.translate(str(text))
    f1.write(translation)
    f1.close()