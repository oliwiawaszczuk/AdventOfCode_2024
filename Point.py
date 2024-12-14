class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("Cannot add Point of type " + str(type(other)))

    def is_out_of_bounds(self, _min, _max):
        return self.x > _max or self.x < _min or self.y > _max or self.y < _min

    def move(self, x, y):
        self.x += x
        self.y += y
