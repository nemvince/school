items = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

def getTotalWeight(items):
    return sum(items)

def getBoxesNeeded(items):
    boxes = []
    current_box = []
    current_weight = 0

    for item in items:
        if current_weight + item > 20:
            boxes.append(current_box)
            current_box = []
            current_weight = 0

        current_box.append(item)
        current_weight += item

    if current_box:
        boxes.append(current_box)

    return [sum(box) for box in boxes]

def runProgram(items):
    print(f"2. feladat")
    print(f"A tárgyak tömegének összege: {getTotalWeight(items)}")

    print(f"3. feladat")
    boxes = getBoxesNeeded(items)

    print(f"A dobozok tartalmának tömege (kg): {' '.join(map(str, boxes))}")
    print(f"A szükseges dobozok száma: {len(boxes)}")
