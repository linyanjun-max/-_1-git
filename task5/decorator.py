import time
from typing import Callable, Any


def timer_decorator(func: Callable) -> Callable:
    """
    Декоратор для измерения времени выполнения функции.
    
    Args:
        func (Callable): Функция для декорирования
        
    Returns:
        Callable: Декорированная функция
    """
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.6f} секунд")
        return result
    return wrapper


@timer_decorator
def add_numbers(a: int, b: int) -> int:
    """
    Складывает два числа и выводит результат в консоль.
    
    Args:
        a (int): Первое число
        b (int): Второе число
        
    Returns:
        int: Сумма чисел
    """
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result


@timer_decorator
def calculate_from_file(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    """
    Читает числа из файла, вычисляет сумму и записывает результат в файл.
    
    Args:
        input_file (str): Имя входного файла
        output_file (str): Имя выходного файла
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            a = int(lines[0].strip())
            b = int(lines[1].strip())
        
        result = a + b
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Сумма чисел {a} и {b} равна {result}\n")
        
        print(f"Результат записан в файл {output_file}")
    
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
    except ValueError:
        print("Ошибка: в файле должны быть целые числа")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def demonstrate_decorator():
    """Демонстрация работы декоратора."""
    print("=== Тестирование декоратора ===")
    
    # Тест первой функции
    print("\n1. Тест сложения чисел:")
    add_numbers(10, 20)
    add_numbers(100, 250)
    
    # Тест второй функции
    print("\n2. Тест работы с файлами:")
    calculate_from_file()


if __name__ == "__main__":
    demonstrate_decorator()