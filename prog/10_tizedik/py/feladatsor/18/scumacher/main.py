from datetime import datetime

class Race:
  def __init__(self, date, name, pos, laps, points, team, status) -> None:
    self.date = datetime.strptime(date, '%Y-%m-%d')
    self.name = name
    self.pos = int(pos)
    self.laps = int(laps)
    self.points = int(points)
    self.team = team
    self.status = status

  def __str__(self) -> str:
    return f"{self.date.strftime('%Y.%m.%d')} {self.name} {self.pos}. {self.laps} {self.points} {self.team} {self.status}"

with open("schumacher.csv") as f:
  d = [Race(*line.strip().split(";")) for line in f.readlines()[1:]]

print(len(d))
print("Magyar Nagydíj helyezései:")
for x in d:
  if "Hungarian" in x.name and x.pos != 0:
    print(f"\t{x.date.strftime('%Y.%m.%d')} - {x.pos}. hely")

print("Hibastatisztika:")
er = [x.status for x in d if x.status != "Finished" and "+" not in x.status]
for x in sorted(set(er)):
  if er.count(x) > 2:
    print(f"\t{x} - {er.count(x)}")