def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    
    Args:
        s (str): Входная строка для проверки
        
    Returns:
        bool: True если строка палиндром, иначе False
        
    Examples:
        >>> is_palindrome("радар")
        True
        >>> is_palindrome("привет")
        False
    """
    # Приводим к нижнему регистру и убираем пробелы
    cleaned_string = ''.join(s.lower().split())
    return cleaned_string == cleaned_string[::-1]


# Тестирование функции
if __name__ == "__main__":
    test_strings = ["радар", "А роза упала на лапу Азора", "привет", "madam", "level"]
    
    for test_str in test_strings:
        result = is_palindrome(test_str)
        print(f"'{test_str}' -> {'Палиндром' if result else 'Не палиндром'}")