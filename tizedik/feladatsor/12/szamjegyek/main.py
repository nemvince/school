with open("input.txt") as f:
  d = f.read().strip()

print(f"A számjegyek száma: {len(d)}")

print(f"A számjegyek összege: {sum(map(int, d))}")

print(f"A legtöbbször előförduló számjegy: {max(d, key=d.count)}")