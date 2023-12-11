from random import choice

def nevelo(fonev):
  return "az" if fonev[0] in "aáeéiíoóöőuúüű" else "a"
  
def jelzo():
  return choice(["lenyűgöző", "csodálatos", "félelmetes", "vastag", "szögletes"])

def generalas():
  x = input("Főnév: ")
  return f"{nevelo(x).capitalize()} {x} {jelzo()}."

def main():
  for i in range(3):
    print(generalas())

main()

# one liner
x=input("Főnév: ");print('\n'.join([f'{"Az" if x[0] in "aáeéiíoóöőuúüű" else "A"} {x} {choice(["kicsi", "nagy", "közepes méretű"])}.']))