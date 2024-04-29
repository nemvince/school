with open("feladat2_forras.txt", encoding="utf-8") as f:
    d = f.read().strip().split("\n")

print(f"A menüben {len(d)} darab étel szerepel.")

print(d[int(input('Hányadik ételre kiváncsi az étlapon? ').strip())-1])

from random import choice
print(f"A nap ajánlata: {choice(d)}")
del choice

t = input("Adja meg a keresett étel pontos nevét! ")
print(f"Az étel {'nem ' if t not in d else ''}szerepel az étlapon.")
