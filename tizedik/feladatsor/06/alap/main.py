def take_int(range_start=None, range_end=None, msg="Kérek egy számot"):
    while True:
        try:
            if not range_start == None and not range_end == None:
                msg += f" ({range_start}-{range_end}): "
            else:
                msg += ": "
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
a = take_int(1, 100, "Kérek egy számot")

# print as word
word = ""
num = [a // 100 % 10, a // 10 % 10, a % 10]
if a == 0:
    word = "nulla"
if num[0] != 0:
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
    ][num[0]]
    word += "száz"
if num[1] != 0:
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
