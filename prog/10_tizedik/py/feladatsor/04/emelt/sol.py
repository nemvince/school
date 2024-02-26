from datetime import datetime as dt

class Connection:
  def __init__(self, country, date) -> None:
    self.country = country
    self.date = dt.strptime(date, "%Y.%m.%d")

  def __str__(self) -> str:
    return f"{self.country} {self.date.strftime('%Y.%m.%d')}"

  def __repr__(self):
    return self.__str__()

countries = []

with open("input.txt", encoding="utf-8") as f:
  d = f.read().split("\n")
  d = [countries.append(Connection(*x.split(";"))) for x in d]

in_eu = [c for c in countries if c.date < dt(2018,1,1)]
print(f"3. feladat: EU tagállamainak száma: {len(in_eu)} db")

joined_in = len([c for c in countries if c.date.year == 2007])
print(f"4. feladat: 2007-ben {joined_in} ország csatlakozott")

print(f"5. feladat: Magyarország csatlakozásának dátuma: {[c.date.strftime('%Y.%m.%d') for c in countries if c.country == 'Magyarország'][0]}")

print(f"6. feladat: Májusban {'volt csatlakozás' if len([c for c in countries if c.date.month == 5]) > 0 else 'nem volt csatlakozás'}!")

print(f"7. feladat: Legutoljára csatlakozott ország: {[c.country for c in countries if c.date == max([c.date for c in countries])][0]}")

print(f"8. feladat: Statisztika")
for year in sorted(set([c.date.year for c in countries])):
  print(f"    {year}: {len([c for c in countries if c.date.year == year])} ország")