import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators


class TestPersonalAccount:
    """
    Тесты для проверки личного кабинета
    """
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    def register_and_login(self, driver, web_wait, user_data):
        """Вспомогательный метод: регистрация и вход пользователя"""
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
    
    # ============================================================
    # ТЕСТ 1: Переход в личный кабинет
    # ============================================================
    
    def test_go_to_personal_account(self, driver, web_wait, test_user_data):
        """
        Проверка перехода в личный кабинет по клику на «Личный кабинет»
        """
        # Регистрируем и входим
        self.register_and_login(driver, web_wait, test_user_data)
        
        # Нажимаем на «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем, что перешли в личный кабинет (URL содержит /profile)
        web_wait.until(EC.url_contains("/profile"))
        assert "/profile" in driver.current_url
        
        driver.quit()
    
    # ============================================================
    # ТЕСТ 2: Переход из ЛК в конструктор по кнопке «Конструктор»
    # ============================================================
    
    def test_go_from_personal_account_to_constructor_by_button(self, driver, web_wait, test_user_data):
        """
        Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»
        """
        # Регистрируем и входим
        self.register_and_login(driver, web_wait, test_user_data)
        
        # Переходим в личный кабинет
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        web_wait.until(EC.url_contains("/profile"))
        
        # Нажимаем на «Конструктор»
        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
        
        # Проверяем, что перешли на главную страницу
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.current_url == f"{self.BASE_URL}/"
        
        driver.quit()
    
    # ============================================================
    # ТЕСТ 3: Переход из ЛК в конструктор по клику на логотип
    # ============================================================
    
    def test_go_from_personal_account_to_constructor_by_logo(self, driver, web_wait, test_user_data):
        """
        Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
        """
        # Регистрируем и входим
        self.register_and_login(driver, web_wait, test_user_data)
        
        # Переходим в личный кабинет
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        web_wait.until(EC.url_contains("/profile"))
        
        # Нажимаем на логотип
        driver.find_element(*StellarBurgersLocators.LOGO).click()
        
        # Проверяем, что перешли на главную страницу
        web_wait.until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.current_url == f"{self.BASE_URL}/"
        
        driver.quit()