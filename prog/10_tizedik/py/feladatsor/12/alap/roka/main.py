class Match():
  def __init__(self, t1, t2, day, price) -> None:
    self.teams = [t1, t2]
    self.day = int(day)
    self.price = int(price)

  def __str__(self) -> str:
    return f"{self.teams} {self.day} {self.price}"

with open("input.txt") as f:
  d = f.read().strip().split("\n")
  n = int(d[0].split(" ")[1])
  d = d[1:]

  d = [Match(*x.split(" ")) for x in d]

p = []

vr = [x for x in d if "Voros_Rokak" in x.teams]

om = [x for x in d if x.teams[0] == "Computerbontok" or x.teams[0] == "Bohocok"]
om.sort(key=lambda x: x.price)

for x in vr:
  n -= x.price
  p.append(x)

print(f"A Voros_Rokak {len(vr)} meccset játszottak, a jegyárak összege {sum([x.price for x in vr])} Ft")

for x in om:
  if n - x.price >= 0:
    n -= x.price
    p.append(x)

vr.sort(key=lambda x: x.day)
print(f"Először a {vr[0].day}. napon játszott a Voros_Rokak, utoljára a {vr[-1].day}. napon.")

print(f"Utolsó mérkőzés napja: {max([x.day for x in d])}")

print(f"A következő napokra vesz jegyet: {' '.join([str(x.day) for x in p])}")

ft = ["Computerbontok", "Bohocok", "Voros_Rokak"]

for t in ft:
  print(f"{t}: {len([x for x in p if t in x.teams])}")