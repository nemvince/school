from datetime import date

class Racer:
    def __init__(self, name, dob, nationality, sn):
        self.name = name
        self.dob = date.fromisoformat(dob.replace(".", "-"))
        self.nationality = nationality
        try:
            self.sn = int(sn)
        except:
            self.sn = None

    def __str__(self):
        return f"{self.name} ({self.dob}) - {self.nationality} - {self.sn}"
        

with open("pilotak.csv", encoding="utf-8") as f:
    d = f.read().split("\n")[1:]
    d = [x.split(";") for x in d]

    d = [Racer(*x) for x in d]

print(f"3. feladat: {len(d)}")

print(f"4. feladat: {d[-1].name}")

print(f"5. feladat:")
for p in [p for p in d if p.dob < date(1900, 1, 1)]:
    print(f"\t{p.name} ({str(p.dob).replace("-", ". ")})")

smallest_sn = min([x for x in d if x.sn is not None], key=lambda x: x.sn)
print(f"6. feladat: {smallest_sn.nationality}")

print(f"7. feladat: {', '.join([str(x) for x in set([x.sn for x in d if x.sn is not None and sum([1 for y in d if y.sn == x.sn]) > 1])])}")