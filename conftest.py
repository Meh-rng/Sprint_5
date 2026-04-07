import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from data_generators import (
    generate_unique_email,
    generate_valid_password,
    generate_short_password,
    generate_name
)

BASE_URL = "https://stellarburgers.education-services.ru"


@pytest.fixture
def driver():
    """
    Фикстура для создания драйвера браузера.
    Важно: драйвер НЕ закрывается здесь, так как по требованию 
    driver.quit() должен быть в каждом тесте
    """
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    return driver


@pytest.fixture
def web_wait(driver):
    """Фикстура для ожидания элементов на странице"""
    return WebDriverWait(driver, 10)


@pytest.fixture
def base_url():
    """Возвращает базовый URL сервиса"""
    return BASE_URL


@pytest.fixture
def test_user_data():
    """
    Фикстура для генерации тестовых данных пользователя
    Используется для успешной регистрации и входа
    """
    return {
        'name': generate_name(),
        'email': generate_unique_email(),
        'password': generate_valid_password()
    }


@pytest.fixture
def test_user_with_short_password():
    """
    Фикстура для генерации данных с коротким паролем
    Используется для проверки ошибки при регистрации
    """
    return {
        'name': generate_name(),
        'email': generate_unique_email(),
        'password': generate_short_password()
    }
