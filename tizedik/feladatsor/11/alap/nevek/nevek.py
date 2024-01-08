with open("input.txt") as f:
    d = f.read().splitlines()

g = []
b = []

for x in d:
    n = x.split(" ")
    if len(n) < 2:
        pass
    else:
        s = 0
        for m in n:
            if m[0].isupper():
                s += 1
        if s == 2:
            g.append(x)
        else:
            b.append(" ".join([y.capitalize() for y in x.split(" ")]))

with open("megfeleloek.txt", "w") as f:
    f.write("\n".join(g))

with open("javitott.txt", "w") as f:
    f.write("\n".join(b))
