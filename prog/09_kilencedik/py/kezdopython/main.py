def viz():
    while True:
        t=int(input("hany fokos a vized\n"))
        print("goz" if t>=100 else "viz" if t>=0 else "jeg")
        exit() if input("folytatod i/n\n") == "n" else None

def greet():
    from datetime import datetime, time
    from getpass import getuser

    c = datetime.now().time()
    t = (c > time(12)) + (c > time(18))
    g = ["reggelt", "napot", "estét"]

    print(f"Jó {g[t]}, {getuser()}!") 
greet()