import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import StellarBurgersLocators


class TestLogin:
    """
    Тесты для проверки функционала входа
    """
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # ============================================================
    # ВСПОМОГАТЕЛЬНЫЙ МЕТОД для регистрации пользователя
    # ============================================================
    
    def register_user(self, driver, web_wait, user_data):
        """Регистрация нового пользователя"""
        driver.get(f"{self.BASE_URL}/register")
        
        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys(user_data['name'])
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(user_data['email'])
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys(user_data['password'])
        driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON).click()
        
        web_wait.until(EC.url_to_be(f"{self.BASE_URL}/login"))
    
    # ============================================================
    # ТЕСТЫ ВХОДА
    # ============================================================
    
    def test_login_by_button_on_main_page(self, driver, web_wait, test_user_data):
        """
        Проверка входа по кнопке «Войти в аккаунт» на главной странице
        """
        # Шаг 1: Регистрируем пользователя
        self.register_user(driver, web_wait, test_user_data)
        
        # Шаг 2: Переходим на главную страницу
        driver.get(self.BASE_URL)
        
        # Шаг 3: Нажимаем кнопку «Войти в аккаунт»
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        
        # Шаг 4: Заполняем форму входа
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(test_user_data['email'])
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(test_user_data['password'])
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM).click()
        
        # Шаг 5: Проверяем успешный вход (появление кнопки "Оформить заказ")
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.current_url == f"{self.BASE_URL}/"
        
        driver.quit()
    
    def test_login_by_personal_account_button(self, driver, web_wait, test_user_data):
        """
        Проверка входа через кнопку «Личный кабинет»
        """
        # Шаг 1: Регистрируем пользователя
        self.register_user(driver, web_wait, test_user_data)
        
        # Шаг 2: Переходим на главную страницу
        driver.get(self.BASE_URL)
        
        # Шаг 3: Нажимаем кнопку «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Шаг 4: Заполняем форму входа
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(test_user_data['email'])
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(test_user_data['password'])
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM).click()
        
        # Шаг 5: Проверяем успешный вход
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.current_url == f"{self.BASE_URL}/"
        
        driver.quit()
    
    def test_login_from_registration_form(self, driver, web_wait, test_user_data):
        """
        Проверка входа через кнопку в форме регистрации
        """
        # Шаг 1: Регистрируем пользователя
        self.register_user(driver, web_wait, test_user_data)
        
        # Шаг 2: На странице регистрации нажимаем ссылку «Войти»
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_RESTORE).click()
        
        # Шаг 3: Заполняем форму входа
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(test_user_data['email'])
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(test_user_data['password'])
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM).click()
        
        # Шаг 4: Проверяем успешный вход
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.current_url == f"{self.BASE_URL}/"
        
        driver.quit()
    
    def test_login_from_password_recovery_form(self, driver, web_wait, test_user_data):
        """
        Проверка входа через кнопку в форме восстановления пароля
        """
        # Шаг 1: Регистрируем пользователя
        self.register_user(driver, web_wait, test_user_data)
        
        # Шаг 2: Переходим на страницу восстановления пароля
        driver.get(f"{self.BASE_URL}/forgot-password")
        
        # Шаг 3: Нажимаем кнопку «Войти» на странице восстановления
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_RESTORE).click()
        
        # Шаг 4: Заполняем форму входа
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(test_user_data['email'])
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(test_user_data['password'])
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM).click()
        
        # Шаг 5: Проверяем успешный вход
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.current_url == f"{self.BASE_URL}/"
        
        driver.quit()