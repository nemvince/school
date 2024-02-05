class Rect():
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def isSquare(self):
    return self.a == self.b

  def area(self):
    return self.a * self.b

  def perimeter(self):
    return 2 * (self.a + self.b)

  def __str__(self):
    return f"({self.a}, {self.b}), {'négyzet' if self.isSquare() else 'téglalap'}, területe: {self.area()}, kerülete: {self.perimeter()}"

  def __repr__(self):
    return f"Rect({self.a}, {self.b})"

def main():
  a = int(input("Kérem az a oldalt: "))
  b = int(input("Kérem a b oldalt: "))

  r = Rect(a, b)

  print(r)

if __name__ == "__main__":
  main()