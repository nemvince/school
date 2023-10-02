from math import ceil, floor

def take_int(msg):
    try:
        num = int(input(msg))
    except ValueError:
        print("Ez nem egy szám!")
        exit()
    return num

def feladat_1():
    capacity = 20
    target = take_int("Hány ládát szállítunk?\t")

    rounds = ceil(target / capacity)

    print(f"Józsi bácsinak {rounds} kört kell tenni.")
    print("3 kör elég." if rounds <= 3 else "3 kör nem elég.")

feladat_1()

def feladat_2():
    capacity = 100
    name = input("Kérem a gyógynövény nevét:\t")
    daily = take_int("Kérem a napi szükséges mennyiséget grammban:\t")

    enough_for = floor(capacity/daily)

    print(f"A(z) {name} összesen {enough_for} napra elegendő")

    print(f"{'Elegendő' if enough_for >= 30 else 'Nem elegendő'} 30 napra!")

feladat_2()

def feladat_3():
    num = take_int("Kérek egy számot:\t")
    print(f"A szám {'benne van' if num in range(-10, 11) else 'nincs benne'} a [-10,10] intervallumban.")

feladat_3()

def feladat_4():
    points = take_int("Kérem a pontok számát:\t")
    print(
        "elégtelen" if points <= 9 else
        "elégséges" if points <= 19 else
        "közepes" if points <= 29 else
        "jó" if points <= 39 else
        "jeles"
    )

feladat_4()

def feladat_5():
    try:
        num = float(input("Kérek egy valós számot:\t"))
    except ValueError:
        print("Ez nem egy valós szám!")
        exit()
    
    print(f"A megadott szám a {floor(num)} és {ceil(num)} egész számok között van, és ezek közül a {round(num)} számhoz van közelebb.")

    method = input("Hogy számoljam a részeket?\nA. `num-round(num)`, rendes megoldás\nB. `str(num).split(\".\")`, csúnyább megoldás\n")

    if method not in ["a", "b", "A", "B"]:
        print("Rossz választás!")
        exit()
    
    if method in ["a", "A"]:
        # A megoldás
        print(f"A szám egész része: {round(num)}")
        print(f"A szám tört része: {num-round(num)}")
    else:
        # B megoldás
        parts = str(num).split(".")
        print(f"A szám egész része: {parts[0]}")
        print(f"A szám tört része: 0.{parts[1]}")

feladat_5()