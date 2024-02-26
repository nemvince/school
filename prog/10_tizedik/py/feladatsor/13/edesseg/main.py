import random

class Snack():
  def __init__(self, n, t, w ,s):
    self.name = n
    self.type = t
    self.weight = w
    self.sweet = s

  def eatLot(self):
    self.weight /= 2

  def eatSmall(self):
    self.weight -= 1

  def getValue(self):
    return self.weight / 100 * (100 + (self.weight - 10) / 10) * (1 + (1 if self.sweet else -1) * 0.1)

  def __str__(self):
    return f"{self.name} ({self.type}), {self.weight} g, {'édes' if self.sweet else 'sós'}"

  def __repr__(self):
    return f"Snack({self.name}, {self.type}, {self.weight}, {self.sweet})"

def genSnack():
  names = ["Mars", "Twix", "Snickers", "Bounty", "KitKat", "Lion", "Milky Way", "Kinder Bueno", "Toblerone", "Ferrero Rocher"]
  types = ["csoki", "cukorka", "rágógumi", "chips", "perec", "keksz"]
  salty = random.choice([True, False])
  return Snack(random.choice(names), ("sós " if salty else "")+random.choice(types), random.randint(10, 100), salty)

def main():
  snacks = []
  for _ in range(10):
    snacks.append(genSnack())

  for index, snack in enumerate(snacks):
    print(f"{index}. {snack}")

  while True:
    index = int(input("Melyik rágcsát szeretné elfogyasztani? "))
    print("Mennyit szeretne enni? (kevés/sok)")
    answer = input()
    if answer == "kevés":
      snacks[index].eatSmall()
    else:
      snacks[index].eatLot()
    print(snacks[index])

    print("Szeretne még enni? (i/n)")
    answer = input()
    if answer == "n":
      break

if __name__ == "__main__":
  main()