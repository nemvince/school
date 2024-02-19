class Bus:
  def __init__(self, route, passengers, articulated, start, destination) -> None:
    self.route = route
    self.passengers = passengers
    self.articulated = articulated
    self.start = start
    self.destination = destination

  def __str__(self) -> str:
    return f"{self.route}, {self.passengers} utas, {self.start} -> {self.destination}"

  def saturation(self):
    if self.passengers < 8:
      return "A járat veszteséges."
    elif self.passengers < 20:
      return "A járat gazdaságos."
    else:
      return "A járat nyereséges."

def main():
  buses = [
    Bus("1", 5, False, "Budapest", "Pécs"),
    Bus("2", 12, True, "Pécs", "Budapest"),
    Bus("3", 25, False, "Budapest", "Pécs"),
  ]

  for bus in buses:
    print(bus)
    print(bus.saturation())

if __name__ == "__main__":
  main()