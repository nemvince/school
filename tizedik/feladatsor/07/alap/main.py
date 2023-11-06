def take_int(range_start=None, range_end=None, msg="Kérek egy számot"):
    if not range_start == None and not range_end == None:
        msg += f" ({range_start}-{range_end}): "
    else:
        msg += ": "
    while True:
        try:
            num = int(input(msg))
            if range_start == None and range_end == None:
                return num
            elif range_start <= num <= range_end:
                return num
            else:
                print(
                    f"A megadott szám nem esik a {range_start}-{range_end} intervallumba!"
                )
        except ValueError:
            print("A megadott érték nem szám!")

def p(l):
    for i, x in enumerate(l):
        print(f"{i}.\t{x}\t{'-' if x < 0 else '+'}")

# 1. feladat
l = [0,0,0,0,0]
for item in l:
    item = take_int()


# 2. feladat
import random

l = []
for i in range(7):
    v = True if random.randint(1) else False
    l.append(v)
    print("IGAZ" if v else "HAMIS")


# 3. feladat
l = []
for i in range(10):
    l.append(random.randint(5,26))

print(l)
print(reversed(l))
print(l[::2])
i = take_int(1,10)
print(l[i-1])


# 4. feladat
a = [69.1, 420.69]
b = [420.2, 69.69]
c = []
for x in zip(a, b):
    c.append(sum(x))
print(c)


# 5. feladat
from collections import deque
items = deque([1, 2, 3, 4, 5, 6])
print(items)
items.rotate(1)
print(items)
items.rotate(-1)
print(items)


# 6. feladat
n = take_int()
l = [random.randint(0,10) for _ in range(n)]
print(l)
l = l[::-1]
print(l)


# 7. feladat
n = take_int()
l = [random.random()*10 for _ in range(n)]
print(sum(l))


# 8. feladat
l = [random.random()*10 for _ in range(10)]
print(l)
for i in range(len(l)):
    if i % 2:
        l[i] += l[i+1]
print(l)


# 9. feladat
l = [random.randint(-10,10)*random.random() for _ in range(n)]
t = 0
for i in range(len(l)):
    if l[i] > 0 and l[i+1] < 0:
        t += 1
print(t)


# 10. feladat
import math

l = [random.randint(-10,10)*random.random() for _ in range(n)]
print(l)
for x in l:
    x = round(x, 2)
print(l)


# 11. feladat
l = [random.randint(-100,100) for _ in range(20)]
print(l)
p(l)
for x in l[::3]:
    x += 1
p(l)
for i in range(len(l)):
    if i % 2 == 0 and i != 0:
        l[i] -= l[i-1]
p(l)


# 12. feladat
n = take_int()
a = take_int(msg="intervallum start")
b = take_int(msg="intervallum end")
if a > b:
    print("nem")
    exit()
l = [random.randint(a,b) for _ in range(n)]
p(l)
d = input("mi legyen\na. novelni\nb. csokkenteni\nc. szorozni\nd. kilepni")
while True:
    while d not in ["a", "b", "c", "d"]:
        d = input("mi legyen\na. novelni\nb. csokkenteni\nc. szorozni\nd. kilepni")
    if d == "d":
        exit()
    m = take_int(msg="mérték?")
    if d == "a":
        l = [x+m for x in l]
    elif d == "b":
        l = [x-m for x in l]
    elif d == "c":
        l = [x*m for x in l]
    p(l)


# 13. feladat
l = ["alma", "körte", "őszibarackbarack", "sárgabarack", "szilva", "málna", "áfonya"]
print(', '.join(l))


# 14. feladat
l = []
n = take_int()
while n != 0:
    if n not in l:
        e = input("eleje vagy vege (e/v)")
        if e not in ["e", "v"]:
            print("ne nezz hatra")
        elif e == "e":
            l = [n, *l]
        else:    
            l.append(n)
    else:
        print("NEM NEM!")
        print(l.index(n))
    

# 15. feladat
l = [random.randint(0,100) for _ in range(20)]
p(l)
l = [x for x in l if x > 50 and x % 2 == 0]
p(l)
m = [x for x in l if x % 2]
l = [x for x in l if not x % 2]
print(len([x for x in l if x >= 10]))