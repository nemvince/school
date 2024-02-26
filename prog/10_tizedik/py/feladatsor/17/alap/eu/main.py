from datetime import datetime

with open("input.txt") as f:
  data = [x.split(";") for x in f.read().split("\n")]

for x in data:
  x[1] = datetime.strptime(x[1], "%Y.%m.%d")

print(f"EU tagállamainak száma: {len(data)}")
print(f"2007-ben {len([x for x in data if x[1].year == 2007])} tagállam csatlakozott az EU-hoz")
print(f"Magyarország csatlakozásának dátuma: {next(x[1] for x in data if x[0] == "Magyarország").strftime('%Y. %B %d.')}")
print("Májusban volt csatlakozás" if any(x[1].month == 5 for x in data) else "Májusban nem volt csatlakozás")
print(f"Statisztika:")
for year in sorted(set(x[1].year for x in data)):
  print(f"  {year}: {len([x for x in data if x[1].year == year])} csatlakozás")