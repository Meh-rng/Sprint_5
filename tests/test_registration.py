import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import StellarBurgersLocators


class TestRegistration:
    """
    Тесты для проверки функционала регистрации
    """
    
    def test_successful_registration(self, driver, web_wait, base_url, test_user_data):
        """
        Проверка успешной регистрации с валидными данными:
        - Имя не пустое
        - Email в формате логин@домен
        - Пароль минимум 6 символов (6-12)
        """
        # Открываем страницу регистрации
        driver.get(f"{base_url}/register")
        
        # Проверяем, что заголовок формы отображается
        title = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.REGISTER_TITLE)
        )
        assert title.is_displayed()
        
        # Заполняем форму регистрации
        name_field = driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT)
        name_field.send_keys(test_user_data['name'])
        
        email_field = driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT)
        email_field.send_keys(test_user_data['email'])
        
        password_field = driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT)
        password_field.send_keys(test_user_data['password'])
        
        # Нажимаем кнопку регистрации
        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON).click()
        
        # После успешной регистрации должен быть редирект на страницу входа
        web_wait.until(EC.url_to_be(f"{base_url}/login"))
        
        # Проверяем, что открылась страница входа
        assert driver.current_url == f"{base_url}/login"
        
        # Закрываем браузер
        driver.quit()
    
    def test_registration_with_short_password_error(self, driver, web_wait, base_url, test_user_with_short_password):
        """
        Проверка ошибки при регистрации с коротким паролем (менее 6 символов)
        """
        # Открываем страницу регистрации
        driver.get(f"{base_url}/register")
        
        # Заполняем форму регистрации
        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys(test_user_with_short_password['name'])
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(test_user_with_short_password['email'])
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys(test_user_with_short_password['password'])
        
        # Нажимаем кнопку регистрации
        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON).click()
        
        # Проверяем появление сообщения об ошибке
        error_message = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.PASSWORD_ERROR)
        )
        
        assert error_message.is_displayed()
        assert error_message.text == "Некорректный пароль"
        
        # Проверяем, что редиректа на страницу входа НЕ произошло
        assert "/login" not in driver.current_url
        
        # Закрываем браузер
        driver.quit()
        