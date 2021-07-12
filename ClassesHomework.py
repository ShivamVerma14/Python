class Cylinder:
    pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.radius + self.height)

class Line:

    def __init__(self, coordinate1, coordinate2):
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2

    def distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())

l = Line((3, 2), (8, 10))
print(l.distance())
print(l.slope())