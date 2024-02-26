# 1. főfeladat
import datetime as dt

name = input("Név? ")
birth = None
while not birth:
    try:
        birth = int(input("Sz. dátum? "))
    except ValueError:
        print("Hiba! Nem egy szám!")
print(f"Kedves {name}! {birth}-ben születtél")
print(f"Kedves {name}! {dt.datetime.now().year-birth} éves vagy!")


# 1. feladat
a = int(input("Add meg az első számot!"))
b = int(input("Add meg a második számot!"))

print(f"A két szám összege: {a+b}")
print(f"A két szám különbsége: {a-b}")


# 2. feladat
a = float(input("Adj meg egy számot: "))
print(a*10)


# 3. feladat
d = float(input("Távolság: "))
t = int(input("Idő: "))

print(f"Az átlagsebesség: {t/d} km/h")


# 4. feladat
a = int(input("Kérlek add meg a háromszög alapját: "))
m = int(input("Kérlek add meg a háromszög magasságát: "))
print(f"A háromszög területe: {a*m/2}")


# 5. feladat
a = int(input("Kérlek adj meg egy egész számot: "))
print(f"A szám kétszerese: {a*2}")


# 6. feladat
a = int(input("Kérlek adj meg egy egész számot: "))
print(f"A szám négyzete: {a**2}")
print(f"A szám köbe: {a**3}")


# 7. feladat
a = int(input("Kérlek adj meg egy hőmérsékletet: "))
print(f"A hőmérséklet Fahrenheitben: {a*1.8+32}")

# 8. feladat
a = int(input("Kérlek adj meg egy alapot: "))
b = int(input("Kérlek adj meg egy kitevőt: "))
print(f"{a}^{b}={a**b}")


# 9. feladat
a = int(input("Kérlek add meg az első számot: "))
b = int(input("Kérlek add meg a második számot: "))

print((a*2)+(b/2))


# 10. feladat
d = int(input("Kérlek add meg a távolságot: "))
f = int(input("Kérlek add meg a fogyasztást: "))

print(f"Az autó {d/f} liter üzemanyaggal megteszi az utat.")


# 11. feladat
p = int(input("Kérlek add meg az óradíjat: "))
t = int(input("Kérlek add meg a munkaidőt: "))

print(f"A munkás {p*t} Ft-ot kap.")


# 12. feladat
r = int(input("Kérlek add meg a kör sugarát: "))
print(f"A kör kerülete: {2*r*3.14}")


# 13. feladat
a = int(input("Kérlek add meg az életkorod: "))
b = float(input("Kérlek add meg az alvásszükségleted: "))

print(f"Átlag alvás/hó: {b*30} óra")


# 14. feladat
s = int(input("Kérlek add meg a lépésszámot: "))
a = int(input("Kérlek add meg az egy hetes napi átlagot: "))
print(f"Az egy hetes átlag: {s*a}")


# 15. feladat
n = input("Kérlek add meg a neved: ")
t = input("Kérlek add meg mire gyűjtesz: ")
a = int(input("Kérlek add meg az összeget: "))
m = int(input("Kérlek add meg a heti zsebpénzed: "))
print(f"{n} {t}-ra {a/m} hetet kell gyűjtenie.")


# 16. feladat
m = float(input("Kérlek add meg a tömeged: "))
h = float(input("Kérlek add meg a magasságod: "))
print(f"A BMI: {m/h**2}")


# 17. feladat
t = m-float(input("Kérlek add meg a célod: "))
print(f"Hetente {t/3} kg-ot kell fogynod.")


# 18. feladat
b = int(input("Kérlek add meg mikor születtél: "))
a = dt.datetime.now().year - b
p = int(input("Kérlek add meg a szemüvegkeret árát: "))
l = int(input("Kérlek add meg a lencse árát: "))

print(l+(p*(1-a/100)))
