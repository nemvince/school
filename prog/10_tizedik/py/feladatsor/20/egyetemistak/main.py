class Student:
    def __init__(self, name, dob, course) -> None:
        self.name = name
        self.dob = int(dob)
        self.course = course

    def __str__(self) -> str:
        return f"{self.name}\t{self.dob}\t{self.course}"

def loadFile(filename="input.txt"):
    with open(filename, encoding="utf-8") as f:
        return [Student(*x) for x in [y.split(";") for y in f.read().strip().split("\n")]]

def create(d, name=None):
    if not name: name = input("Name? ")
    dob = int(input("Year of birth? "))
    course = input(f"Course? ({", ".join(set([x.course for x in d]))}) ")
    d.append(Student(name, dob, course))
    return d

def read(d, use_index=False):
    if use_index:
        for i in range(len(d)):
            print(f"{i}. {d[i]}")
    else: print(*d,sep="\n")

def update(d):
    n = input("Name? ")
    if not n in [x.name for x in d]:
        yn = input(f"Student with name, {n} not found, want to create? (Y/N) ")
        if yn in "Yy": d = create(d, name=n)
    else:
        i = [x.name for x in d].index(n)
        d[i].dob = int(input("Year of birth?"))
        d[i].course = input(f"Course? ({", ".join(set([x.course for x in d]))}) ")
        print(f"Updated {d[i].name}")
    return d

def delete(d):
    read(d, use_index=True)
    n = int(input("Index of student to delete? "))
    s = d[n]
    d.pop(n)
    print(f"Removed {s.name}")
    return d
    
def countBirthYear(d, year=1990):
    return len([x for x in d if x.dob == year])

def mostCommonCourse(d):
    c = [x.course for x in d]
    return max(set(c), key=c.count)

def averageAge(d):
    from datetime import datetime
    year = datetime.now().year
    a = [year-x.dob for x in d]
    return sum(a)/len(a)

if __name__ == "__main__":
    d = loadFile()
    
    read(d)

    d = update(d)

    d = delete(d)

    print(countBirthYear(d))

    print(mostCommonCourse(d))

    print(round(averageAge(d), 2))




