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
        print(f"A megadott szám nem esik a {range_start}-{range_end} intervallumba!")
    except ValueError:
      print("A megadott érték nem szám!")

# 1. feladat
a = take_int(1, 10)

for i in range(1, a+1):
  print(f"{i}. Egy fecske nem csinál nyarat.")

# 2. feladat
a = take_int(1, 10)

for i in range(1, a+1):
  print(f"Megmondtam már {i}-szer, hogy semmit nem mondok el kétszer.")


# 3. feladat
for i in range(0, 51):
  print(i)

for i in range(182, 213):
  print(i)

for i in range(100, 201, 2):
  print(i)

for i in range(89, 56, -2):
  print(i)

for i in range(1, 21):
  print(f"{i} {i**2}")

for i in range(99, 0, -3):
  print(i)

for i in range(101, 49, -5):
  print(i*2)

for i in range(1, 1001):
  if i == 1000:
    print(i, end=".")
  else:
    print(i, end=", ")

for i in range(1000, 0, -3):
  print(i, end=", ")


# 4. feladat

for i in range(100):
  print("*", end="")

a = take_int()
b = input("Kérek egy karaktert: ")

for i in range(a):
  print(b, end="")

a = input("Kérek egy szöveget: ")
print("*"*(len(a)+2))
print(f"*{a}*")
print("*"*(len(a)+2))

for i in range(8):
  if i % 2 == 0:
    print("* * * * ")
  else:
    print(" * * * *")


# 5. feladat
a = take_int()
b = take_int()
c = take_int(msg="Kérem a lépésközt: ")

for i in range(a, b+1, c):
  print(i, end=" ")


# 6. feladat
a = take_int()

for i in range(1, a+1):
  print(i**2, end="; ")


# 7. feladat
a = take_int()

for i in range(1, a+1):
  print(i**3)
  

# 8. feladat
a = take_int()

for i in range(1, a+1):
  print(f"{i} {i**0.5:.2f}")


# 9. feladat
a = take_int()

f = 1
for i in range(1, a+1):
  f *= i
print(f)


# 10. feladat
a = take_int()

for i in range(1, a+1):
  print(i**2)


# 11. feladat
a = take_int()
t = 0
for i in range(0, a):
  if i % 2:
    t += i
print(t)


# 12. feladat
a = take_int()

t = 0
for i in range(1, a+1):
  t += i*(i+1)


# 13. feladat
a = take_int()

for i in range(1, a+1):
  print(i*3)


# 14. feladat
n = take_int()

def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)
  
for i in range(n):
  print(fib(i), end=" ")


# 15. feladat
n = take_int()

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for i in range(1, n+1):
  if is_prime(i):
    print(i, end=" ")


# 16. feladat
for i in range(1, 11):
  for j in range(1, 11):
    print(f"{i*j:4}", end="")
  print()


# 17. feladat
from random import randint
def rand(range_start, range_end):
  return randint(range_start, range_end)

ranges = [[0,10], [0,25], [0,50], [10,75], [-50,50], [-100,-70]]
for x in ranges:
  print(f"{rand(x[0], x[1])} ", end="")

# 18. feladat
a = take_int()

# 1 sor
print("*"*a)

# négyzet
for i in range(a):
  print("*"*a)


# 19. feladat
a = take_int()
b = take_int()

for i in range(a):
  print("*"*b)


# 20. feladat
a = take_int()
b = take_int()

for i in range(a):
  print(" "*(a-i), "*"*b)


# 21. feladat
a = take_int()

for i in range(a):
  print(" "*(a-i) + "*"*(i*2+1))


# 22. feladat
a = take_int()
b = take_int()

for i in range(a):
  if i == 0 or i == a-1:
    print("*"*b)
  else:
    print("*" + " "*(b-2) + "*")


# 23. feladat
from random import randint
def rand(range_start, range_end):
  return randint(range_start, range_end)

a = take_int()

good = 0
bad = 0

for i in range(a):
  x = rand(1, 100)
  y = rand(1, 100)
  print(f"{x} + {y} = ", end="")
  z = take_int()
  if z == x+y:
    print("Helyes!")
    good += 1
  else:
    print("Helytelen!")
    bad += 1
  
  print(f"{x} - {y} = ", end="")

  z = take_int()
  if z == x-y:
    print("Helyes!")
    good += 1
  else:
    print("Helytelen!")
    bad += 1

print(f"Helyes: {good}, Helytelen: {bad}")
print(f"Arány: {good/(good+bad)*100:.2f}%")

# 24. feladat
for i in range(32, 256):
  print(f"{i:3} {chr(i)}")


# 25. feladat
a = take_int()

for i in range(1, a+1):
  if a % i == 0:
    print(i, end=" ")


# 26. feladat
a = take_int()

s = 0
for i in range(1, a+1):
  if a % i == 0:
    s += i

print(s)


# 27. feladat
a = take_int()

s = 0
for i in range(1, a):
  if a % i == 0:
    s += i

if s == a:
  print("Tökéletes szám!")
else:
  print("Nem tökéletes szám!")


# 28. feladat
a = take_int(msg="Kérem a hatványalapot: ")
b = take_int(msg="Kérem a kitevőt: ")

print(a**b)


# 29. feladat
for i in range(65, 91):
  for j in range(65, 91):
    print(chr((i+j-130)%26+65), end="")
  print()

