import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import StellarBurgersLocators


class TestConstructor:
    """
    Тесты для проверки переключения разделов в конструкторе
    """
    BASE_URL = "https://stellarburgers.education-services.ru"

    def test_switch_to_buns_section(self, driver, web_wait):
        """Проверка перехода к разделу 'Булки'"""
        driver.get(self.BASE_URL)
        
        # Сначала переключаемся на другой раздел, чтобы убрать активность с "Булок"
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        web_wait.until(EC.element_to_be_clickable(StellarBurgersLocators.SAUCES_TAB))
        
        # Кликаем по табу "Булки"
        driver.find_element(*StellarBurgersLocators.BUNS_TAB).click()
        
        # Проверяем, что заголовок раздела "Булки" видим
        buns_title = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.BUNS_SECTION_TITLE)
        )
        assert buns_title.is_displayed()
        
        driver.quit()

    def test_switch_to_sauces_section(self, driver, web_wait):
        """Проверка перехода к разделу 'Соусы'"""
        driver.get(self.BASE_URL)
        
        # Кликаем по табу "Соусы"
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        
        # Проверяем, что заголовок раздела "Соусы" видим
        sauces_title = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.SAUCES_SECTION_TITLE)
        )
        assert sauces_title.is_displayed()
        
        driver.quit()

    def test_switch_to_fillings_section(self, driver, web_wait):
        """Проверка перехода к разделу 'Начинки'"""
        driver.get(self.BASE_URL)
        
        # Кликаем по табу "Начинки"
        driver.find_element(*StellarBurgersLocators.FILLINGS_TAB).click()
        
        # Проверяем, что заголовок раздела "Начинки" видим
        fillings_title = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.FILLINGS_SECTION_TITLE)
        )
        assert fillings_title.is_displayed()
        
        driver.quit()
        