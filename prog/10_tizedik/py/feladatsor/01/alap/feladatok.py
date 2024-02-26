# 1. feladat
print("Hello World!")


# 2. feladat
# A megoldás
name = "Vince"
print(f"Kedves {name}!")
print("\tIsten hozott a Python világában!")
print("\t\tÜdv: a program")

# B megoldás
print(f"Kedves {name}\n\tIsten hozott a Python világában!\n\t\tÜdv: a program")


# 3. feladat
quote = "Ha meg tudod álmodni, meg is tudod tenni!"
author = "Walt Disney"
# A megoldás
print(quote, end=f"\t{author}\n")

# B megoldás
print(quote, end="\t")
print(author)

# C megoldás
print(quote, end=" - ")
print(author)


# 4. feladat
# A megoldás
print("tej", "kenyér", "sajt", "vaj", sep="*")

# B megoldás
print("tej", "kenyér", "sajt", "vaj", sep="-")


# 5. feladat
text = "A 'whitespace' vagy 'white space' angol szóösszetétel, jelentése fehér tér. \nAz informatikában, elsősorban a \n\tszövegszerkesztésben és\n\tprogramozásban\nhasználatos kifejezés.\n\nAlapvetően azokat a karaktereket értjük alatta, amelyek nem láthatóak a szövegben, viszont valamilyen egyedi funkcióval bírnak. Nincs elterjedt magyar kifejezés rá.\" \n -- A Wikipédiából, (a szabad enciklopédiából)"
print(text)


# 6. feladat
name = "Vince"
age = 15
height = 1.8
print([type(x) for x in [name,age,height]])


# 7. feladat
name = "Vince"
pad = "*"*(len(name)+2)
print(pad)
print(f"*{name}*")
print(pad)


# 8. feladat
a = 5
b = 10

def print_vars(a,b):
    print(f"\ta={a}, b={b}")

print(a*2, b*2)
print_vars(a,b)
b*=2
print_vars(a,b)
a+=1;b-=1
print_vars(a,b)
a=100
print_vars(a,b)
s=a+b
print(s)


# 9. feladat
a = 1
b = 7
c = -3

print("(a-b)/c")
print(f"({a}-{b})/{c}")
print((a-b)/c)

print("(a+b)*(2a-c)")
print(f"({a}+{b})*(2{a}-{c})")
print((a+b)*(2*a-c))

print("(3a-3b)/c")
print(f"(3{a}-3{b})/{c}")
print((3*a-3*b)/c)

print("2ac+4b")
print(f"2{a}{c}+4{b}")
print(2*a*c+4*b)


# 10. feladat
x=10
y=3

print(f"x\t=\t{x}")
print(f"y\t=\t{y}")
print("-"*(8*3))
print(f"x+y\t=\t{x+y}")
print(f"x-y\t=\t{x-y}")
print(f"x*y\t=\t{x*y}")
print(f"x/y\t=\t{round(x/y, 3)}")
print(f"x//y\t=\t{x//y}")
print(f"x%y\t=\t{x%y}")
print(f"x**2\t=\t{x**2}")
print(f"x**3\t=\t{x**3}")