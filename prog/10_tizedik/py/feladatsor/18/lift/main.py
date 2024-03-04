from datetime import datetime

class LiftUse:
  def __init__(self, date, card, sfloor, tfloor):
    self.date = datetime(*[int(x) for x in date.split('.')[:-1]])
    self.card = int(card)
    self.sfloor = int(sfloor)
    self.tfloor = int(tfloor)

  def __str__(self):
    return f"{self.date} {self.card} {self.sfloor} {self.tfloor}"

with open("lift.txt") as f:
  d = [LiftUse(*line.strip().split()) for line in f]

print(f"Összes lift használat: {len(d)}")

print(f"Időszak: {d[0].date.strftime('%Y.%m.%d')} - {d[-1].date.strftime('%Y.%m.%d')}")

print(f"Célszint max: {max([x.tfloor for x in d])}")

c = input("Kérem a kártya számát: ")
f = input("Kérem a szintet: ")
try:
  c, f = int(c), int(f)
except ValueError:
  c, f = 5, 5
if any([x.card == c and x.tfloor == f for x in d]):
  print(f"A {c} kártyával a {f}. szintre volt lift használat.")
else:
  print(f"A {c} kártyával a {f}. szintre nem volt lift használat.")

print("Statisztika:")
# print uses for every day
for day in sorted(set([x.date.strftime('%Y.%m.%d') for x in d])):
  print(f"\t{day} - {len([x for x in d if x.date.strftime('%Y.%m.%d') == day])}x")
