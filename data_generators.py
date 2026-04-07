import random
import string

def generate_unique_email():
    """
    Генерирует уникальный email в формате:
    имя_фамилия_номер_когорты_3цифры@домен
    """
    first_name = "ivan"
    last_name = "popovich"
    cohort = "4344"  # Укажите номер вашей когорты
    
    # Генерируем 3 случайные цифры
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
    
    # Домен можно указать любой
    domain = "@yandex.ru"
    
    email = f"{first_name}_{last_name}_{cohort}_{random_digits}{domain}"
    return email

def generate_valid_password():
    """
    Генерирует валидный пароль (6 и более символов)
    """
    length = random.randint(6, 12)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_short_password():
    """
    Генерирует короткий пароль (менее 6 символов) для проверки ошибки
    """
    length = random.randint(3, 5)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_name():
    """
    Генерирует случайное имя
    """
    names = ["Алексей", "Мария", "Дмитрий", "Елена", "Максим", "Анна"]
    return random.choice(names)
