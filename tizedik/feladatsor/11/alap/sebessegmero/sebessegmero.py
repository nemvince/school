with open("input.txt") as f:
    d = f.read().splitlines()

l, r = [], []
for x in d:
    x = int(x)
    if x < 0:
        l.append(abs(x))
    else:
        r.append(x)

print(f"Balra: {l}, jobbra: {r}")
print("Balra" if l > r else "Jobbra" if r > l else "Egyenesen" + " ment el több autó.")

l_avg = sum(l) / len(l)
r_avg = sum(r) / len(r)
print(f"Balra: {l_avg}, jobbra: {r_avg}")

l_max = max(l)
r_max = max(r)
print(f"Balra: {l_max}, jobbra: {r_max}")

l_min = min(l)
r_min = min(r)
print(f"Balra: {l_min}, jobbra: {r_min}")

with open("jobbra.txt", "w") as f:
    f.write("\n".join([str(x) for x in r]))
