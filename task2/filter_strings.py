from typing import List, Callable


def filter_strings(filter_func: Callable[[str], bool], string_array: List[str]) -> List[str]:
    """
    Фильтрует массив строк с помощью лямбда-функции.
    
    Args:
        filter_func (Callable): Лямбда-функция для фильтрации
        string_array (List[str]): Массив строк для фильтрации
        
    Returns:
        List[str]: Отфильтрованный массив строк
    """
    return list(filter(filter_func, string_array))


def main():
    """Демонстрация работы функции фильтрации."""
    test_strings = [
        "apple", "banana", "apricot", "cherry", "blue berry",
        "kiwi", "orange", "avocado", "grape", "pineapple"
    ]
    
    print("Исходный массив:", test_strings)
    print()
    
    # 1. Исключить строки с пробелами
    no_spaces = filter_strings(lambda s: ' ' not in s, test_strings)
    print("1. Без пробелов:", no_spaces)
    
    # 2. Исключить строки, начинающиеся с буквы "а"
    no_a_start = filter_strings(lambda s: not s.lower().startswith('а'), test_strings)
    print("2. Не начинаются с 'а':", no_a_start)
    
    # 3. Исключить строки, длина которых меньше 5
    min_length_5 = filter_strings(lambda s: len(s) >= 5, test_strings)
    print("3. Длина >= 5:", min_length_5)


if __name__ == "__main__":
    main()