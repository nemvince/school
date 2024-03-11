import random

class Animal:
  def __init__(self, name, p1, p2, weight) -> None:
    self.name = name
    self.properties = [p1, p2]
    self.weight = float(weight)

  def __str__(self) -> str:
    return f"{self.name}\t{self.properties}\t{self.weight}"

with open("allatok.txt", encoding="utf-8") as f:
  animals = [Animal(*line.strip().split(";")) for line in f]

print(' '.join(set([x.name for x in animals])))

print(sum([x.weight for x in animals]))

print('\n'.join([str(x) for x in animals if "Négylábú" in x.properties and x.weight > 100]))

print(round(sum(x.weight for x in animals) / len(animals)), "kg")

light = [x for x in animals if x.weight < 1]
print(f"{len(light)} db 1 kg alatti állat van.")
for x in light:
  print(x)

strong = [x for x in animals if "Erős" in x.properties]
print(f"{len(strong)} db erős állat van.")
for x in strong:
  print(x)

print(random.choice(animals))

names = [x.name for x in animals]
if len(names) != len(set(names)):
  print("Van azonos nevű állat.")
else:
  print("Nincs azonos nevű állat.")

with open("negylabuak.txt" , "w", encoding="utf-8") as f:
  for x in animals:
    if "Négylábú" in x.properties:
      f.write(str(x) + "\n")

with open("nagyok.txt" , "w", encoding="utf-8") as f:
  for x in animals:
    if x.weight > 100:
      f.write(str(x) + "\n")

