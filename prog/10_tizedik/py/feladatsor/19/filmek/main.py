for i in range(3):
  title = input("Add meg egy film címét! ")
  runtime = int(input("Hány perces a film? "))

  # nagyon fancy vagyok ma
  article = "Az" if title[0].lower() in "aeiou" else "A"

  print(f"{article} {title} című film {runtime // 60} óra {runtime % 60} perc hosszú.")
