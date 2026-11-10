# decorators.py

from functools import wraps
from functions import get_greeting, get_info

def bold_html_decorator(func):
    """Декоратор, який обгортає текстовий результат функції у теги <b>...</b>."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Перевіряємо, чи результат є стрічкою, і обгортаємо його
        if isinstance(result, str):
            return f"<b>{result}</b>"
        return result
    return wrapper

# Застосовуємо декоратор до функцій з іншого файлу
decorated_greeting = bold_html_decorator(get_greeting)
decorated_info = bold_html_decorator(get_info)

if __name__ == "__main__":
    print("--- Результат роботи декоратора ---")
    print(decorated_greeting("Олексій"))
    print(decorated_info())