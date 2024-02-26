with open("input.txt") as f:
    d = f.readlines()

d = [s[0].lower()+s[1:] for s in d]

print('\n'.join(d))

print(len(d))

def search():
    x = input("Keresett gyógynövény:")
    print("A(z) {} gyógynövény {}.".format(x, "megtalálható" if x in d else "nem található meg", "a fájlban"))

search()

print('\n'.join([s for s in d if s[0] in "aáeéiíoóöőuúüű"]))

print(' '.join(sorted(d)))