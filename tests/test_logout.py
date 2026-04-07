import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators


class TestLogout:
    """
    Тесты для проверки выхода из аккаунта
    """
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    def register_and_login(self, driver, web_wait, user_data):
        """Регистрация и вход пользователя"""
        # Регистрация
        driver.get(f"{self.BASE_URL}/register")
        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys(user_data['name'])
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(user_data['email'])
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys(user_data['password'])
        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON).click()
        web_wait.until(EC.url_to_be(f"{self.BASE_URL}/login"))
        
        # Вход
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(user_data['email'])
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(user_data['password'])
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM).click()
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
    
    def test_logout_from_personal_account(self, driver, web_wait, test_user_data):
        """
        Проверка выхода по кнопке «Выйти» в личном кабинете
        """
        # Регистрируем и входим
        self.register_and_login(driver, web_wait, test_user_data)
        
        # Переходим в личный кабинет
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        web_wait.until(EC.url_contains("/profile"))
        
        # Нажимаем кнопку «Выйти»
        driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()
        
        # Проверяем, что перешли на страницу входа
        web_wait.until(EC.url_to_be(f"{self.BASE_URL}/login"))
        assert driver.current_url == f"{self.BASE_URL}/login"
        
        driver.quit()
        