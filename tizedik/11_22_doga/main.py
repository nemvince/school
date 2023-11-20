import random

# 1. feladat
print("1. feladat")

l = [random.randint(1, 6) for _ in range(100)]

egyesek = [x for x in l if x == 1]
hatosok = [x for x in l if x == 6]

print(f"Egyesek száma: {len(egyesek)}")
print(f"Hatosok száma: {len(hatosok)}")


# 2. feladat
print("2. feladat")

i = int(input("Adj meg egy számot: "))
l = []
while i != 15:
    l.append(i)
    i = int(input("Adj meg egy számot: "))

print(f"Összeg: {sum(l)}")
print(f"Legkisebb szám: {min(l)}, a {l.index(min(l))}. helyen van")
print(f"Legnagyobb szám: {max(l)}, a {l.index(max(l))}. helyen van")


# 3. feladat
print("3. feladat")

l = []
while len(l) != 5:
    r = random.randint(1, 90)
    if r not in l:
        l.append(r)


g = []
for i in range(5):
    g.append(int(input("Adj meg egy számot:")))

print(" ".join([str(x) for x in l]))
t = sum([1 for x in g if x in l])
print(f"{t}/5 eltalált")
r = [str(x) for x in g if x in l]
if len(r) != 0:
    print(" ".join(r))


# 4. feladat
print("4. feladat")

n = int(input("Adj meg egy számot:"))
l = [random.randint(0, 20) for _ in range(n)]
print(l)

for i in range(1, len(l) - 1):
    if l[i - 1] + l[i + 1] == 20:
        print(l[i])
