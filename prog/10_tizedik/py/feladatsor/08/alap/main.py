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


import random
import math
import re

# 1. feladat
l = [random.randint(2, 120) for _ in range(12)]
p(l)
print(f"{min(l)/25} m/s, {l.index(min(l))}. barát")
print([l.index(x) for x in l if x > 60])


# 2. feladat
c = 100
n = take_int()
t = []
while n != 0:
    t.append(n)
    n = take_int()

print(f"{math.ceil(sum(t)/10000)}-szer kell feltölteni a drónt")
if t[-1] > 5000:
    print("A drón lezuhant!")
else:
    print("A drón nem zuhant le!")


# 3. feladat
c = []
l = []
while True:
    n = input("Mi az előadás címe és milyen hoszzú? (pl. 'A kis herceg,120'): ")
    if n == "":
        break
    try:
        c.append(n.split(",")[0])
        l.append(int(n.split(",")[1]))
    except:
        print("Hibás formátum!")
        continue

print(f"{c[l.index(max(l))]} a leghosszabb előadás")


# 4. feladat
words = [
    "fuvola",
    "csirke",
    "adatok",
    "asztal",
    "fogoly",
    "bicska",
    "farkas",
    "almafa",
    "babona",
    "gerinc",
    "dervis",
    "bagoly",
    "ecetes",
    "angyal",
    "boglya",
]
sel = [x for x in random.choice(words)]
show = ["." for _ in sel]
lives = 5

while True:
    print("".join(show))
    guess = input("Tipp: ")
    if guess in sel:
        for i, x in enumerate(sel):
            if x == guess:
                show[i] = guess
    else:
        lives -= 1
        print(f"Rossz tipp! Még {lives} életed maradt!")
        if lives == 0:
            print("Vesztettél!")
            break
    if "." not in show:
        print("Nyertél!")
        break


# 5. feladat
def validate_taj(a):
    a = re.sub(r"[^0-9]", "", a)
    if len(a) != 9:
        return False

    c = 0
    d = ""
    for b in range(len(a)):
        if b <= 7:
            c += 7 * int(a[b]) if (b + 1) % 2 == 0 else 3 * int(a[b])
            d += a[b]

    return a == d + str(c % 10)


a = input("Enter TAJ number: ")
result = validate_taj(a)
print("A TAJ szám érvényes." if result else "A TAJ szám érvénytelen.")
