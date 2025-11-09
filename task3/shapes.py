import math
from abc import ABC, abstractmethod
from typing import Union


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур."""
    
    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Вычисляет периметр фигуры."""
        pass
    
    def area_greater_than(self, other: 'Shape') -> bool:
        """
        Сравнивает площадь с другой фигурой.
        
        Args:
            other (Shape): Другая фигура для сравнения
            
        Returns:
            bool: True если площадь текущей фигуры больше
        """
        return self.area() > other.area()
    
    def perimeter_greater_than(self, other: 'Shape') -> bool:
        """
        Сравнивает периметр с другой фигурой.
        
        Args:
            other (Shape): Другая фигура для сравнения
            
        Returns:
            bool: True если периметр текущей фигуры больше
        """
        return self.perimeter() > other.perimeter()


class Square(Shape):
    """Класс квадрата."""
    
    def __init__(self, side: float):
        """
        Args:
            side (float): Длина стороны квадрата
        """
        self.side = side
    
    def area(self) -> float:
        """Вычисляет площадь квадрата."""
        return self.side ** 2
    
    def perimeter(self) -> float:
        """Вычисляет периметр квадрата."""
        return 4 * self.side
    
    def __str__(self):
        return f"Квадрат со стороной {self.side}"


class Rectangle(Shape):
    """Класс прямоугольника."""
    
    def __init__(self, width: float, height: float):
        """
        Args:
            width (float): Ширина прямоугольника
            height (float): Высота прямоугольника
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"


class Triangle(Shape):
    """Класс треугольника."""
    
    def __init__(self, a: float, b: float, c: float):
        """
        Args:
            a, b, c (float): Длины сторон треугольника
        """
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        """Вычисляет площадь треугольника по формуле Герона."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        """Вычисляет периметр треугольника."""
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c}"


class Circle(Shape):
    """Класс круга."""
    
    def __init__(self, radius: float):
        """
        Args:
            radius (float): Радиус круга
        """
        self.radius = radius
    
    def area(self) -> float:
        """Вычисляет площадь круга."""
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Вычисляет длину окружности."""
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Круг с радиусом {self.radius}"


def demonstrate_shapes():
    """Демонстрация работы с фигурами."""
    shapes = [
        Square(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Circle(3)
    ]
    
    for i, shape1 in enumerate(shapes):
        print(f"\n{shape1}:")
        print(f"  Площадь: {shape1.area():.2f}")
        print(f"  Периметр: {shape1.perimeter():.2f}")
        
        # Сравнение с другими фигурами
        for j, shape2 in enumerate(shapes):
            if i != j:
                area_comp = "больше" if shape1.area_greater_than(shape2) else "меньше или равно"
                perimeter_comp = "больше" if shape1.perimeter_greater_than(shape2) else "меньше или равно"
                print(f"  По сравнению с {type(shape2).__name__}: площадь {area_comp}, периметр {perimeter_comp}")


if __name__ == "__main__":
    demonstrate_shapes()