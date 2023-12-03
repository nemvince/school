with open("input.txt") as f:
    d = [x.split(" ") for x in f.read().splitlines()]

print("Út(km)\tFogyasztás(l)\tÁtlag(l/100km)")
for x in d:
    km = int(x[0])
    f = float(x[1])
    print(f"{km}\t{f}\t\t{f * 100 / km:.1f}")
