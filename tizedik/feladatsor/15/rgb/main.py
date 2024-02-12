class Pixel:
  def __init__(self, r, g, b) -> None:
    self.r = int(r)
    self.g = int(g)
    self.b = int(b)
    self.sum = self.r + self.g + self.b

  def __str__(self) -> str:
    return f"Pixel({self.r}, {self.g}, {self.b})"

with open("input.txt") as file:
  data = file.read().strip().split("\n")

image = []
width = 0
height = len(data)

for line in data:
  values = line.split(" ")
  row = []
  for i in range(0,len(values),3):
    row.append(Pixel(*values[i:i+3]))
  width = len(row)
  image.append(row)

print(width, height)

def getColorForPixel(image, pos):
  return image[pos[0]][pos[1]]

def countLightPixels(image):
  s = sum([len([y for y in x if y.sum > 600]) for x in image])
  return s

def getDarkestPixel(image):
  min = image[0][0]
  for row in image:
    for pixel in row:
      if pixel.sum < min.sum:
        min = pixel
  return [pixel for row in image for pixel in row if pixel.sum == min.sum]

def borderCalc(row, limit):
  for i in range(len(row)-1):
    if abs(row[i].b - row[i+1].b) > limit:
      return True
  return False

def getCloudLine(image):
  data = {}
  for index, row in enumerate(image):
    data[index] = borderCalc(row, 10)

  first = 0
  last = 0
  for i in range(len(data)):
    if data[i]:
      first = i
      break
  for i in range(len(data)-1, 0, -1):
    if data[i]:
      last = i
      break

  return [first+1, last+1]

pos = [int(x) for x in input("Kérlek add meg a pixel pozícióját 640x360 formátumban!").split("x")]
print(getColorForPixel(image, pos))

print(countLightPixels(image))

print(*getDarkestPixel(image), sep="\n")

print(getCloudLine(image))
