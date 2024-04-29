class Food():
    def __init__(self, c, n, p, g):
        self.category = c
        self.name = n
        self.price = int(p)
        self.gluten = g == "igen"

    def __str__(self):
        return f"{self.category} {self.name} {self.price} {self.gluten}"
    
with open("feladat3_forras.csv") as f:
    d = [Food(*i.strip().split(";")) for i in f.read().strip().split("\n")[1:]]

print("Az ételek nevei")
print(', '.join([i.name for i in d]))

print(f"A legdrágább étel: {max(d, key=lambda x: x.price).name} Ára: {max(d, key=lambda x: x.price).price} Ft")

from random import choice
gfd = [i for i in d if not i.gluten and i.category == "desszert"]
print(f"{'Nincs' if not gfd else 'Van'} gluténmentes desszert az étlapon {f'({choice(gfd).name})' if len(gfd) else ''}")
del choice

print("Az étlapon eléhető kategóriák:")
print(', '.join(set([i.category for i in d])))