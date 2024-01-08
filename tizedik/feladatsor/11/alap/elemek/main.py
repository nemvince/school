with open("input.txt") as f:
    d = f.readlines()

print(len(d))

print(d[-1])

def search():
    x = input("Keresett elem:")
    return x in d

print(search())

def recommend():
    import random
    return random.choice(d)

print(recommend())