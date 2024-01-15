f = input("Filename: ")

with open(f, "r") as f:
    d = f.readlines()
    for c in "abcdefghijklmnopqrstuvwxyz":
        print(f"{c}: {d.count(c)}")