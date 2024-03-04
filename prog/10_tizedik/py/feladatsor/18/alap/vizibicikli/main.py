from datetime import datetime, timedelta
import math

class Lease:
  def __init__(self, name, vehicle, start_hours, start_minutes, end_hours, end_minutes) -> None:
    self.name = name
    self.vehicle = vehicle
    self.start = datetime(2024, 1, 1, int(start_hours), int(start_minutes))
    self.end = datetime(2024, 1, 1, int(end_hours), int(end_minutes))

  def __str__(self) -> str:
    return f"{self.name} {self.vehicle} {self.start} {self.end}"


with open("kolcsonzesek.txt") as f:
  d = [Lease(*x.split(";")) for x in f.read().strip().split("\n")[1:]]

print(f"Napi kölcsönzések száma: {len(d)}")

n = input("Kérek egy nevet: ")
if n in [x.name for x in d]:
  print(f"\t{n} kölcsönzései:")
  for x in d:
    if x.name == n:
      print(f"\t{x.start.strftime('%H:%M')} - {x.end.strftime('%H:%M')}")
else:
  print("\tNincs ilyen névvel kölcsönzés!")

t = input("Kérek egy időpontot (óra:perc): ").split(":")
t = datetime(2024, 1, 1, int(t[0]), int(t[1]))

print(f"A megadott időpontban {len([x for x in d if x.start <= t <= x.end])} járm volt a vízen.")
for x in d:
  if x.start <= t <= x.end:
    print(f"\t{x.start.strftime('%H:%M')} - {x.end.strftime('%H:%M')}: {x.name}")

print(f"A mai bevétel: {sum([math.ceil((x.end - x.start) / timedelta(minutes=30))*2400 for x in d])} Ft.")

with open("f.txt", "w") as f:
  f.write("\n".join([f"{x.start.strftime('%H:%M')}-{x.end.strftime('%H:%M')} : {x.name}" for x in d if x.vehicle == "F"]))

print(f"Statisztika: ")
for x in sorted(set([x.vehicle for x in d])):
  print(f"\t{x} - {len([y for y in d if y.vehicle == x])}")