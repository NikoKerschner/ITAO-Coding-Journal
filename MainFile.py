class Shape:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name


square = Shape(4, "Square")
pentagon = Shape(5, "Pentagon")
hexagon = Shape(6, "Hexagon")


print(hexagon.name, hexagon.sides)