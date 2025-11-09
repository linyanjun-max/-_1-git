from typing import Union


class Person:
    """Базовый класс человека."""
    
    def __init__(self, full_name: str, age: int):
        """
        Args:
            full_name (str): Полное имя
            age (int): Возраст
        """
        self.full_name = full_name
        self.age = age
    
    def get_info(self) -> str:
        """Возвращает информацию о человеке."""
        return f"ФИО: {self.full_name}, Возраст: {self.age}"


class Student(Person):
    """Класс студента."""
    
    SCHOLARSHIP_EXCELLENT = 6000
    SCHOLARSHIP_GOOD = 4000
    SCHOLARSHIP_NONE = 0
    
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float):
        """
        Args:
            full_name (str): Полное имя
            age (int): Возраст
            group_number (str): Номер группы
            average_grade (float): Средний балл
        """
        super().__init__(full_name, age)
        self.group_number = group_number
        self.average_grade = average_grade
    
    def calculate_scholarship(self) -> int:
        """Вычисляет размер стипендии."""
        if self.average_grade == 5:
            return self.SCHOLARSHIP_EXCELLENT
        elif self.average_grade >= 4:
            return self.SCHOLARSHIP_GOOD
        else:
            return self.SCHOLARSHIP_NONE
    
    def get_scholarship_info(self) -> str:
        """Возвращает информацию о стипендии."""
        return f"Стипендия: {self.calculate_scholarship()} руб."
    
    def scholarship_greater_than(self, other: Union['Student', 'GraduateStudent']) -> bool:
        """
        Сравнивает стипендию с другим студентом/аспирантом.
        
        Args:
            other: Другой студент или аспирант
            
        Returns:
            bool: True если стипендия больше
        """
        return self.calculate_scholarship() > other.calculate_scholarship()
    
    def get_info(self) -> str:
        """Возвращает полную информацию о студенте."""
        base_info = super().get_info()
        return f"{base_info}, Группа: {self.group_number}, Средний балл: {self.average_grade}"


class GraduateStudent(Student):
    """Класс аспиранта."""
    
    SCHOLARSHIP_EXCELLENT = 8000
    SCHOLARSHIP_GOOD = 6000
    
    def __init__(self, full_name: str, age: int, group_number: str, 
                 average_grade: float, research_topic: str):
        """
        Args:
            full_name (str): Полное имя
            age (int): Возраст
            group_number (str): Номер группы
            average_grade (float): Средний балл
            research_topic (str): Тема научной работы
        """
        super().__init__(full_name, age, group_number, average_grade)
        self.research_topic = research_topic
    
    def get_info(self) -> str:
        """Возвращает полную информацию об аспиранте."""
        base_info = super().get_info()
        return f"{base_info}, Научная работа: '{self.research_topic}'"


def demonstrate_students():
    """Демонстрация работы со студентами и аспирантами."""
    students = [
        Student("Иванов Иван Иванович", 20, "ГР-01", 4.8),
        Student("Петров Петр Петрович", 19, "ГР-02", 5.0),
        Student("Сидорова Анна Сергеевна", 21, "ГР-01", 3.9),
        GraduateStudent("Козлов Алексей Дмитриевич", 25, "АСП-01", 5.0, 
                       "Исследование алгоритмов машинного обучения"),
        GraduateStudent("Новикова Елена Викторовна", 24, "АСП-02", 4.7,
                       "Разработка систем искусственного интеллекта")
    ]
    
    for person in students:
        print(f"\n{person.get_info()}")
        print(f"  {person.get_scholarship_info()}")
    
    # Сравнение стипендий
    print("\n--- Сравнение стипендий ---")
    for i, student1 in enumerate(students):
        for j, student2 in enumerate(students):
            if i < j:  # Чтобы не сравнивать дважды
                result = "больше" if student1.scholarship_greater_than(student2) else "меньше или равна"
                print(f"{student1.full_name}: стипендия {result}, чем у {student2.full_name}")


if __name__ == "__main__":
    demonstrate_students()