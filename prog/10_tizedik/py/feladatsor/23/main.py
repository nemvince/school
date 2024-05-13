from datetime import date

class Discovery:
    def __init__(self, year, name, sym, reg, by) -> None:
        self.year = date(1,1,1) if year == "Ókor" else date(int(year), 1, 1)
        self.name = name
        self.sym = sym
        self.reg = int(reg)
        self.by = by

    def __str__(self) -> str:
        return f"{self.year.year}: {self.name} ({self.sym}) {self.reg} {self.by}"

with open("felfedezesek.csv", encoding="utf-8") as f:
    d = [Discovery(*line.strip().split(";")) for line in f.read().strip().split("\n")[1:]]

print(f"3. Feladat: Elemek száma: {len(d)}")

print(f"4. Feladat: Felfedezések száma az ókorban: {len([x for x in d if x.year == date(1,1,1)])}")

inp = ""
while not inp.isalpha() and len(inp) not in [1,2]:
    inp = input("5. Feladat: Kérek egy vegyjeletet: ").capitalize()
    
print(f"6. Feladat: Keresés")
s = [x for x in d if x.sym == inp]
if len(s) == 0:
    print("Nincs ilyen elem az adatforrásban!")
else:
    s = s[0]
    print(f"\tAz elem vegyjele: {s.sym}")
    print(f"\tAz elem neve: {s.name}")
    print(f"\tRendszáma: {s.reg}")
    print(f"\tFelfedezés éve: {s.year.year}")
    print(f"\tFelfedező: {s.by}")


# leghosszabb időszak két felfedezés között
d = [x for x in d if x.year != date(1,1,1)]
t = [d[i+1].year - d[i].year for i in range(len(d)-1)]
print(f"7. feladat: {max(t).days//365} év volt a leghosszabb időszak két felfedezés között.")

print("8. feladat: Statisztika")
for x in set([y.year.year for y in d if y.year.year != 1]):
    if len([y for y in d if y.year.year == x]) > 3:
        print(f"\t{x}: {len([y for y in d if y.year.year == x])} db")