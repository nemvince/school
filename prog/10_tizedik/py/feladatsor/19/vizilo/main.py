from datetime import datetime

class Vizilo:
  def __init__(self, name, born, gender, weight) -> None:
    self.name = name
    self.born = int(born)
    self.gender = gender
    self.weight = float(weight)

  def __str__(self) -> str:
    return f"{self.name}\t{self.born}\t{self.gender}\t{self.weight}"

with open("vizilo.txt", encoding="utf-8") as f:
  d = [Vizilo(*x.strip().split(";")) for x in f.read().split("\n")[1:]]

print(len([x for x in d if x.gender == "him"]))

print(min(d, key=lambda x: x.born).name, max(d, key=lambda x: x.born).name)

cYear = datetime.now().year
print("Van" if any([cYear - x.born == 10 for x in d]) else "Nincs" + " olyan víziló, aki idén tölti a 10. életévét.")

print(sum([x.weight for x in d]))
print(round(sum([x.weight for x in d]) / len(d), 2))

print(len([x for x in d if x.weight >= 1000]))

with open("himek.txt", "w", encoding="utf-8") as f:
  for x in reversed(sorted([x for x in d if x.gender == "him"], key=lambda x: cYear - x.born)):
    f.write(str(x) + "\n")

# 7. Mely vizilovak azonos súlyúak?
known = {}
printed = False
for x in d:
  if x.weight in known:
    known[x.weight].append(x)
  else:
    known[x.weight] = [x]

for k, v in known.items():
  if len(v) > 1:
    printed = True
    print(k, [x.name for x in v])

if not printed: print("Nincs azonos súlyú víziló.")