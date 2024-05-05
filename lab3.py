#--*-- encoding: cp1251 --*--
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class InvalidInputError(Exception):
    pass

class Tetragon:
    def __init__(self, vertices):
        if len(vertices) != 4:
            raise InvalidInputError("Четырехугольник должен иметь 4 вершины.")
        self.vertices = vertices
    def translate(self, dx, dy):
        self.vertices = [(x + dx, y + dy) for x, y in self.vertices]

class Triangle:
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise InvalidInputError("Треугольник должен иметь 3 вершины.")
        self.vertices = vertices
    def translate(self, dx, dy):
        self.vertices = [(x + dx, y + dy) for x, y in self.vertices]

def is_include(Tetragon, triangle):
    for vertex in Tetragon.vertices:
        if not is_point_inside_triangle(vertex, triangle.vertices):
            return False
    return True

def is_point_inside_triangle(point, triangle_vertices):
    x, y = point
    x1, y1 = triangle_vertices[0]
    x2, y2 = triangle_vertices[1]
    x3, y3 = triangle_vertices[2]

    total_area = 0.5 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3)

    area1 = 0.5 * (-y2 * x3 + y * (-x2 + x3) + x * (y2 - y3) + x2 * y3)
    area2 = 0.5 * (-y * x3 + y1 * (-x + x3) + x1 * (y - y3) + x * y3)
    area3 = 0.5 * (-y2 * x + y1 * (-x2 + x) + x1 * (y2 - y) + x2 * y)

    if total_area == 0:
        raise InvalidInputError("Площадь треугольника равна нулю.")

    return area1 >= 0 and area2 >= 0 and area3 >= 0

Tetragon_vertices = [(1, 1), (3, 1), (3, 2), (1, 2)]
triangle_vertices = [(0, 0), (4, 0), (2, 4)]

try:
    tetragon = Tetragon(Tetragon_vertices)
    triangle = Triangle(triangle_vertices)

    if is_include(tetragon, triangle):
        print("Четырехугольник входит в треугольник.")
    else:
        print("Четырехугольник не входит в треугольник.")

except InvalidInputError as e:
    print(f"Ошибка: {e}")





fig, ax = plt.subplots()
Tetragon = Polygon(Tetragon_vertices, edgecolor='black', facecolor='none')
ax.add_patch(Tetragon)
triangle = Polygon(triangle_vertices, edgecolor='red', facecolor='none')
ax.add_patch(triangle)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
