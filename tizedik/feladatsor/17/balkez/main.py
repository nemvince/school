from datetime import date, datetime
import csv

class Player:
  def __init__(self, name, fp, lp, weight, height) -> None:
    self.name = name
    self.fp = datetime.strptime(fp, "%Y-%m-%d")
    self.lp = datetime.strptime(lp, "%Y-%m-%d")
    self.weight = int(weight)
    self.weight_kg = self.weight*0.453592
    self.height = int(height)
    self.height_cm = self.height*2.54
    self.height_str = f"{self.height//12}'{self.height%12}\""

  def __str__(self) -> str:
    return f"{self.name} ({self.fp.strftime('%Y.%m.%d')}-{self.lp.strftime('%Y.%m.%d')}) - {self.weight} lb, {self.height_str}"

with open("balkezesek.csv", "r", encoding="utf-8") as file:
  reader = csv.reader(file, delimiter=";")

  # skip over header
  next(reader)
  players = [Player(*row) for row in reader]

print(f"{len(players)} játékos adatai beolvasva")

print(f"1999 októberében utoljára játszottak:")
for player in players:
  if player.lp.year == 1999 and player.lp.month == 10:
    print(f"{player.name} - {round(player.height_cm, 1)} cm")

y = int(input("Évszám? "))
while not 1990 <= y <= 1999:
  y = int(input("Érvénytelen évszám! Kérek egy másikat: "))

print(f"{y}-ben a pályára lépett játékosok átlagsúlya: {round(sum(player.weight_kg for player in players if player.fp.year == y) / len([player for player in players if player.fp.year == y]), 2)} kg")

