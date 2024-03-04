from datetime import datetime

class Absence:
  def __init__(self, name, grade, first_day, last_day, missed_hours) -> None:
    self.name = name
    self.grade = grade
    self.first_day = datetime(2024, 9, int(first_day))
    self.last_day = datetime(2024, 9, int(last_day))
    self.missed_hours = int(missed_hours)

  def __str__(self) -> str:
    return f"{self.name} {self.grade} {self.first_day} {self.last_day} {self.missed_hours}"
with open("szeptember.csv") as f:
  d = [Absence(*x.split(";")) for x in f.read().strip().split("\n")[1:]]

print(f"Összes mulasztott óra: {sum([x.missed_hours for x in d])}")

t = input("Kérek egy időpontot (nap, 1-30): ")
n = input("Kérek egy nevet: ")

if n in [x.name for x in d]:
  print("A tanuló hiányzott szepemberben.")
else:
  print("A tanuló nem hiányzott szeptemberben.")

dt = datetime(2024, 9, int(t))
print(f"Hiányzók {dt.strftime('%Y.%m.%d')}-én:")
for x in d:
  if x.first_day <= dt <= x.last_day:
    print(f"{x.name} ({x.grade})")

print(*d, sep="\n")
with open("osszesites.csv", "w") as f:
  for x in [[x, sum([y.missed_hours for y in d if y.grade == x])] for x in sorted(set([z.grade for z in d]))]:
    f.write(f"{x[0]};{x[1]}\n")