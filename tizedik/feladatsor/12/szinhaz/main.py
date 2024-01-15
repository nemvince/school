with open("input.txt") as f:
  d = f.read().strip().split("\n")

print(f"Az előadásra {sum([x.count("x") for x in d])} jegyet adtak el, ez a nézőtér {round(sum([x.count("x") for x in d])/sum([len(x) for x in d])*100, 1)}%-a.")

moc, moi = 0, 0

for i, x in enumerate(d):
  if x.count("o") > moc:
    moc = x.count("o")
    moi = i

print(f"A legtöbb szabad hely ({moc} darab) a {moi+1}. sorban van.")
