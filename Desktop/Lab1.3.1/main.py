import math

class Triangle:
    def __init__(self, a, b=0, c=0):
        if isinstance(a, Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            assert a + b > c and a + c > b and b + c > a, "Некоректні сторони трикутника"
            self.a = a
            self.b = b
            self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2.0
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a, b, c, d, h=None):
        self.a = a  # основа
        self.b = b  # основа
        self.c = c  # бічна
        self.d = d  # бічна
        self.h = h if h else abs(a - b) / 2  # умовна висота, якщо не задана

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return (self.a + self.b) * self.h / 2


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2


def read_figures_from_file(filename):
    figures = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            name = parts[0]
            params = list(map(float, parts[1:]))

            try:
                if name == "Triangle":
                    figures.append(Triangle(*params))
                elif name == "Rectangle":
                    figures.append(Rectangle(*params))
                elif name == "Trapeze":
                    figures.append(Trapeze(*params))
                elif name == "Parallelogram":
                    figures.append(Parallelogram(*params))
                elif name == "Circle":
                    figures.append(Circle(*params))
            except AssertionError as e:
                print(f"Пропущено фігуру {name} з параметрами {params}: {e}")
    return figures


def find_max_area_and_perimeter(figures):
    max_area_figure = max(figures, key=lambda f: f.square())
    max_perimeter_figure = max(figures, key=lambda f: f.perimeter())
    return max_area_figure, max_perimeter_figure


if __name__ == "__main__":
    filenames = ["inputs/input01.txt", "inputs/input02.txt", "inputs/input03.txt"]

    for filename in filenames:
        print(f"\nОбробка файлу: {filename}")
        figures = read_figures_from_file(filename)
        
        if figures:
            max_area_figure, max_perimeter_figure = find_max_area_and_perimeter(figures)
            print(f"Найбільша площа: {max_area_figure.__class__.__name__} = {max_area_figure.square():.2f}")
            print(f"Найбільший периметр: {max_perimeter_figure.__class__.__name__} = {max_perimeter_figure.perimeter():.2f}")
        else:
            print("Немає коректних фігур у файлі.")
