class Time():
  def __init__(self, h, m):
    self.h = h
    self.m = m

  def addMin(self, min):
    self.m += min
    self.h += self.m // 60
    self.m %= 60

  def subMin(self, min):
    self.m -= min
    self.h -= self.m // 60
    self.m %= 60

  def __str__(self):
    return f"{self.h:02d}:{self.m:02d}"

def main():
  h = int(input("Kérem az órát: "))
  m = int(input("Kérem a percet: "))

  t = Time(h, m)

  print(t)

  print("Hány percet szeretne hozzáadni?")
  min = int(input())
  t.addMin(min)
  print(t)

  print("Hány percet szeretne kivonni?")
  min = int(input())
  t.subMin(min)
  print(t)

if __name__ == "__main__":
  main()