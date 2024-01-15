with open("input.txt") as f:
  d = [x.split(" ") for x in f.read().strip().split("\n")[2:]]

print(f"A táblázatban {sum([x.count('0') for x in d])} nulla van.")

m = str(max([max([int(y) for y in x]) for x in d]))

print(f"A legnagyobb elem: {m}")

for i, x in enumerate(d):
  for j, y in enumerate(x):
    if y == m:
      print(f"{i+1}. sor, {j+1}. oszlop")
      break

avg = [sum([int(y) for y in x if y != "0"])/len(x) for x in d]

print(f"A számok átlaga: {round(sum(avg)/len(avg), 2)}")