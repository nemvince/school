class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, other):
    return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __str__(self):
    return f"({self.x}, {self.y})"

  def __repr__(self):
    return f"Point({self.x}, {self.y})"

def readPoint():
  x = int(input("Kérem az x koordinátát: "))
  y = int(input("Kérem az y koordinátát: "))
  return Point(x, y)

def main():
  first = readPoint()
  prev = first
  sum = 0
  while True:
    curr = readPoint()
    sum += prev.distance(curr)
    if curr == first:
      break
    prev = curr
  print(f"A kerítés hossza: {sum}")

if __name__ == "__main__":
  main()