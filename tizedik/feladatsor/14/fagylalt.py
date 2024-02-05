class IceCream():
  def __init__(self, f, n):
    self.flavour = f
    self.number = n

  def __str__(self):
    return f"{self.flavour} ízű fagyi, {self.number} gombóc"

  def __repr__(self):
    return f"IceCream({self.flavour}, {self.number})"

def findFlavour(iceCreams, flavour):
  for iceCream in iceCreams:
    if iceCream.flavour == flavour:
      return iceCream
  return None

def main():
  iceCreams = [
    IceCream("pisztácia", 0),
    IceCream("vanília", 3),
    IceCream("tutti-frutti", 8),
    IceCream("karamell", 4),
    IceCream("rumos dió", 5),
    IceCream("kávé", 9)
  ]

  while True:
    flavour = input("Milyen ízű fagyit kér? ")
    iceCream = findFlavour(iceCreams, flavour)
    if iceCream == None:
      print("Nincs ilyen ízű fagyi!")
    elif iceCream.number == 0:
      print("Elfogyott!")
    else:
      iceCream.number -= 1
      print("Itt a fagyi!")
    if input("Még egy fagyi? (i/n) ") == "n":
      break

if __name__ == "__main__":
  main()