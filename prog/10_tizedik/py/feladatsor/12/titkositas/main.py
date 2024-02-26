f = input("Filename: ")

with open(f, "r") as f:
  d = f.readlines()

c = "abcdefghijklmnopqrstuvwxyz"

with open("enc1.txt", "w") as f:
  for l in d:
    f.write([c[c.index(s)+3 % len(c)] for s in l])

with open("enc2.txt", "w") as f:
  for i, l in enumerate(d):
    f.write([c[c.index(s)+i+1 % len(c)] for s in l])