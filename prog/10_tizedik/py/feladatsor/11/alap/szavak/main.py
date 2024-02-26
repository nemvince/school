with open("input.txt") as f:
    d = [s.strip() for s in f.readlines()]

def filter():
    for s in d:
        if len(s) > 8:
            yield s

print(list(filter()))

def wordmap():
    return [s.capitalize() for s in d]

print(wordmap())

def count():
    return sum([len(s) for s in d])

print(count())

def select():
    t = [s for s in d if s[0] == "aáeéiíoóöőuúüű"]
    return t

print(select())

def random():
    import random
    return random.choice(d)[::-1]

print(random())

def parts(x):
    return d.count(x)

print(parts("almma"))