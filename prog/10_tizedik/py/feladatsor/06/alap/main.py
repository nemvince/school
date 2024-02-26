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


import random

# 1. feladat
print(random.randint(0, 10))
print(random.randint(10, 15))
print(random.randint(0, 100))
print(random.randint(-100, 100))
print([random.getrandbits(1) for _ in range(10)])
print([random.randint(10, 30) for _ in range(4)])


# 2. feladat
x = input("Fej vagy írás? (f/i): ")
y = random.getrandbits(1)
if x == "f" and y == 0:
    print("Nyertél!")
elif x == "i" and y == 1:
    print("Nyertél!")
elif x == "f" and y == 1:
    print("Vesztettél!")
elif x == "i" and y == 0:
    print("Vesztettél!")
else:
    print("Hibás bemenet!")


# 3. feladat
a = take_int(1, 100)

word = ""
num = [a // 100 % 10, a // 10 % 10, a % 10]
if a == 0:
    word = "nulla"
if num[0] != 0:
    word += "egyszáz"
if num[1] != 0 and a % 10 != 0:
    word += [
        "",
        "tizen",
        "huszon",
        "harminc",
        "negyven",
        "ötven",
        "hatvan",
        "hetven",
        "nyolcvan",
        "kilencven",
    ][num[1]]
elif num[1] != 0 and a % 10 == 0:
    word += [
        "",
        "tíz",
        "húsz",
        "harminc",
        "negyven",
        "ötven",
        "hatvan",
        "hetven",
        "nyolcvan",
        "kilencven",
    ][num[1]]
if num[2] != 0:
    word += [
        "",
        "egy",
        "kettő",
        "három",
        "négy",
        "öt",
        "hat",
        "hét",
        "nyolc",
        "kilenc",
    ][num[2]]
print(word)


# 4. feladat
t = 1
a = take_int(0, 100)
while a != 0:
    t *= a
    a = take_int(0, 100)
    print(t)


# 5. feladat
t = ""
a = input("Kérek egy stringet: ")
while a != "":
    t += a
    a = input("Kérek egy stringet: ")
    print(t)


# 6. feladat
a = take_int(1, 100)
b = input("Kérek egy karaktert: ")
if len(b) != 1:
    print("Hibás bemenet!")
else:
    print(b * a)

# 7. feladat
a = take_int(1, 100)
b = take_int(1, 100)
c = take_int(1, 100, "Kérem a lépésközt")

print(' '.join([str(i) for i in range(a, b + 1, c)]))


# 8. feladat
a = [x for x in range(1000) if x % 3 == 0 and x % 5 == 0]
print(a)


# 9. feladat
a = take_int(1, 1000)
coins = [200, 100, 50, 20, 10, 5]
for i in coins:
    if a // i != 0:
        print(f"{a // i} db {i} Ft-os")
    a %= i


# 10. feladat
a = take_int(1, 1000)
b = take_int(1, 1000)
c = take_int(1, 1000)
print([a + i * b for i in range(c)])


# 11. feladat
a = take_int(1, 1000)
print(sum([i for i in range(a) if i % 2 == 1]))


# 12. feladat
a = take_int(1, 1000)
# print factorial
t = 1
for i in range(1, a + 1):
    t *= i
print(t)


# 13. feladat
a = take_int(1, 1000)
b = take_int(1, 1000)
t = 0
for i in range(a):
    t += b

print(t)


# 14. feladat
a = take_int(1, 1000)
b = take_int(1, 1000)
t = 1
for i in range(b):
    t *= a
print(t)


# 15. feladat
a = take_int(1, 1000)
b = take_int(1, 1000)

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)


# 16. feladat
a = take_int(1, 1000)
b = take_int(1, 1000)
t = 1
while t % a != 0 or t % b != 0:
    t += 1
print(t)


# 17. feladat
a = take_int(0, 1000)
b = take_int(1, 1000)

print(f"{a}/{b} = {a/b}")


# 18. feladat
t, x, y = 0, 0, 0
while t < 1000:
    a = take_int(1, 10)
    if a % 2 == 0:
        x += 1
    else: y += 1
    t += a
    print(f"total: {t}")
print(f"páros: {x}, páratlan: {y}")


# 19. feladat
a,b,c,d,e = [input(f"Kérek egy karaktert ({i+1}.): ") for i in range(5)]
print(f"{a}{b}{c}{d}{e}")
# mi az ősszé permutáció?
# hogy lehet egy évszakot ősszé permutálni?


# 20. feladat
a = take_int(1, 100)
while a % 2 != 0:
    print("A megadott szám nem megfelelő.")
    a = take_int(1, 100)
print("A megadott szám megfelelő.")


# 21. feladat
a = take_int(1, 100)
print(a%5)


# 22. feladat
a = take_int(1, 7)
print(["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"][a])


# 23. feladat
a = take_int(msg="Kérek egy páratlan negatív számot")
while a > 0 and a % 2 == 0:
    a = take_int(msg="Kérek egy páratlan negatív számot")
    print("A megadott szám nem megfelelő.")


# 24. feladat
a = take_int()
while a % 3 != 0 and a % 5 != 0:
    a = take_int()
    print("A megadott szám nem megfelelő.")


# 25. feladat
a = take_int()
while a % 5 != 0:
    print(a % 5)
    a = take_int()


# 26. feladat
a = take_int()
b = take_int()
while a != b:
    if a > b:
        print(f"{a} > {b}")
    else:
        print(f"{b} > {a}")
    a = take_int()
    b = take_int()


# 27. feladat
c = True
while c:
    a = random.randint(1,12)
    print(f"{a}, {a%3}")
    cq = input("Még? (i/n): ")
    c = cq == "i"


# 28. feladat
a = 1
t = []
while a != 0:
    a = take_int()
    t.append(a)

t = [x for x in t if x != 0]

print(f"Min: {min(t)}, Max: {max(t)}")


# 29. feladat
a = random.randint(1,50)
b = take_int(1,50)
while a != b:
    if a > b:
        print("Nagyobb")
    else:
        print("Kisebb")
    b = take_int(1,50)
print("Eltaláltad!")


# 30. feladat
a = random.randint(1,50)
b = take_int(1,50)
i = 1
while a != b and i < 7:
    if a > b:
        print("Nagyobb")
    else:
        print("Kisebb")
    b = take_int(1,50)
    i += 1

if i == 7:
    print(f"A gondolt szám: {a}")
else:
    print("Eltaláltad!")


# 31. feladat
a = 1
t = []
while a != 0:
    a = take_int()
    t.append(a)

t = [x for x in t if x != 0]

print(f"{len(t)} db, {sum(t)/len(t)} átlag")


# 32. feladat
a = take_int()
b = take_int()
for i in range(b):
    print(f"{i} * {a} = {i*a}")


# 33. feladat
a = take_int()
b = take_int()
while b != 0:
    if b == 0: break
    c = random.randint(0, b)
    print(f"{a} * {c} = ?")
    d = take_int()
    while d != c*a:
        print("Hibás válasz!")
        d = take_int()
    b = take_int()


# 34. feladat
a = 0
b = 0
c = 0
w = 0
while c < 10:
    a = random.randint(1,10)
    b = random.randint(1,10)
    d = random.randint(0,2)
    if d == 0:
        print(f"{a} + {b} = ?")
        e = take_int()
        while e != a+b:
            print("Hibás válasz!")
            w += 1
            e = take_int()
    elif d == 1:
        print(f"{a} - {b} = ?")
        e = take_int()
        while e != a-b:
            print("Hibás válasz!")
            w += 1
            e = take_int()
    else:
        print(f"{a} * {b} = ?")
        e = take_int()
        while e != a*b:
            print("Hibás válasz!")
            w += 1
            e = take_int()
    c += 1

print(f"{w} hibás válasz, {100-w*10}% eredményesség")


# 35. feladat
a = take_int()
b = take_int()
c = take_int()
t = []
for i in range(c):
    t.append(a+i*b)
print(t)
print(sum(t))


# 36. feladat
a = take_int()
b = take_int()
c = take_int()
t = []
for i in range(c):
    t.append(a*b**i)
print(t)
print(sum(t))


# 37. feladat
a = take_int()
b = take_int()
c = take_int()
d = take_int()
e = a*d + b*c
f = b*d
print(f"{e}/{f}")