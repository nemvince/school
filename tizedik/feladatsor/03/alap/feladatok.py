# 1. feladat
a = int(input("Add meg az első számot!"))
b = int(input("Add meg a második számot!"))

print(f"A két szám összege: {a+b}")
print(f"A két szám hányadosa: {a/b}")


# 2. feladat
a = float(input("Adj meg egy számot: "))
print(a%2)
print(a%3)


# 3. feladat
a = int(input("Kérlek add meg a számot: "))
if a % 2 != 0:
    print("A szám nem páros!.")
else:
    print(a/2)


# 4. feladat
a = float(input("Kérlek add meg a számot: "))
print(a/3)


# 5. feladat
d = float(input("Átmérő: "))
m = int(input("Mélység: "))
print(f"A medence térfogata: {d**2*m*3.14/4}")


# 6. feladat
a = int(input("A értéke: "))
b = int(input("B értéke: "))

x = -b / a
print(f"Az x értéke: {x}")


# 7. feladat
t = int(input("Tank mérete: "))
b = int(input("Távolság: "))

print(f"Az autó fogyasztása: {b/t*100} liter/100km")


# 8. feladat
a = int(input("Hány kg krumplit veszünk?"))
b = int(input("Mennyi egy kg krumpli?"))

print(f"Kell: {a*b} Ft")


# 9. feladat
a = int(input("Mennyi a fizetésed?"))
b = int(input("Mennyi a fizetésemelés százaléka?"))

print(f"A fizetésed: {a*(1+b/100)} Ft")


# 10. feladat
a = int(input("Mennyit teszel félre?"))
b = int(input("Mennyi a laptop ára?"))

print(f"Ennyi hónap múlva tudod megvenni: {b/a} hónap")


# 11. feladat
a = int(input("Mennyi a kölcsön összege?"))
b = int(input("Mennyi a futamidő?"))

print(f"A törlesztő részlet: {a/b} Ft")


# 12. feladat
a = int(input("Mennyi a terület szélessége?"))
b = int(input("Mennyi a terület hosszúsága?"))
c = int(input("Mennyi a terület magassága?"))

print(f"A területhez {a*b*c/(20**3)} db 20x20x20-as kocka kell.")


# 13. feladat
a = [input(f"Add meg az első {x}") for x in ["órát", "percet", "másodpercet"]]
b = [input(f"Add meg a második {x}") for x in ["órát", "percet", "másodpercet"]]

print(f"A két idő között {abs(int(a[0])*3600+int(a[1])*60+int(a[2])-(int(b[0])*3600+int(b[1])*60+int(b[2])))} másodperc van.")


# 14. feladat
a = int(input("Mennyi az első szám?"))
b = int(input("Mennyi a második szám?"))
c = int(input("Mennyi a harmadik szám?"))

print(f"Van {a*5+b*2+c} eurónk van.")


# 15. feladat
a = int(input("Mennyi az átmérő?"))
b = int(input("Hány dinnye?"))

print(f"Összesen {b*(a*2+60)} cm szalag kell.")


# 16. feladat
a = int(input("Mennyi a kert hossza?"))
b = int(input("Mennyi a kert szélessége?"))
t = a*b

print(f"A befüvesítéshez {math.ceil(t/5)} zacskó fűmag kell.")



# 17. feladat
import math
a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))

print(f"A két szám négyzetgyöke: {math.sqrt(a)} és {math.sqrt(b)}")


# 18. feladat
a = int(input("Add meg a számot: "))

print(f"A megadott szám a {math.floor(a)} és {math.ceil(a)} között van, és {math.floor(a)}-hez van közelebb.")
print(f"A szám egész része: {math.floor(a)}")
print(f"A szám tizedes része: {a-math.floor(a)}")


# 19. feladat
a = int(input("Add meg a számot: "))

print(f"{round(a, 2)}")


# 20. feladat
a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))

if a > b:
    print(a-b)
else:
    print(b-a)


# 21. feladat
import requests
r = requests.get("https://open.er-api.com/v6/latest/USD").json()
u = r["rates"]["HUF"]
r = requests.get("https://open.er-api.com/v6/latest/EUR").json()
e = r["rates"]["HUF"]
del requests

a = int(input("Add meg a forintok összegét: "))

print(f"{a} Ft = {a/u} USD")
print(f"{a} Ft = {a/e} EUR")


# 22. feladat
a = input("Adja meg a kordinátákat X,Y formátumban: ").split(",")
b = input("Adja meg a kordinátákat X,Y formátumban: ").split(",")

print(f"A két pont távolsága: {math.sqrt((int(a[0])-int(b[0]))**2+(int(a[1])-int(b[1]))**2)}")


# 23. feladat
a = input("Add meg az első ember nevét,testmagasságát,testsúlyát X,Y,Z formátumban: ").split(",")
b = input("Add meg a második ember nevét,testmagasságát,testsúlyát X,Y,Z formátumban: ").split(",")
c = input("Add meg a harmadik ember nevét,testmagasságát,testsúlyát X,Y,Z formátumban: ").split(",")

print(f"Az átlagmagasság: {(int(a[1])+int(b[1])+int(c[1]))/3}")
print(f"Az összsúly: {int(a[2])+int(b[2])+int(c[2])}")
print(f"A tanulók BMI-je: {int(a[2])/(int(a[1])/100)**2}, {int(b[2])/(int(b[1])/100)**2}, {int(c[2])/(int(c[1])/100)**2}")
print(f"A legnehezebb tanuló: {max(a[0], b[0], c[0], key=lambda x: int(x[2]))}")

# 24. feladat
