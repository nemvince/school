with open("input.txt") as f:
    d = f.read().splitlines()

t = {}

print(f"{len(d)} diák jár az osztályba.")

for x in d:
    g = x.split(";")
    n = g[0]
    e = g[1].split(",")
    for y in e:
        if y not in t:
            t[y] = []
        t[y].append(n)

print(", ".join(t.keys()))

for x in t:
    print(f"{x}: {len(t[x])} diák választotta.")

for x in t:
    print(f"{x}: {', '.join(t[x])}")
