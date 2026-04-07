import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import StellarBurgersLocators

class TestConstructor:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    def test_switch_to_buns_section(self, driver, web_wait):
        """Проверка перехода к разделу 'Булки'"""
        driver.get(self.BASE_URL)
        
        # Сначала переключаемся на другой раздел, чтобы убрать активность с "Булок"
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        web_wait.until(EC.element_to_be_clickable(StellarBurgersLocators.SAUCES_TAB))
        
        # Кликаем по табу "Булки"
        driver.find_element(*StellarBurgersLocators.BUNS_TAB).click()
        
        # Проверяем, что активный таб - "Булки"
        active_tab = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Булки", "Не удалось переключиться на раздел 'Булки'"
        
        driver.quit()
    
    def test_switch_to_sauces_section(self, driver, web_wait):
        """Проверка перехода к разделу 'Соусы'"""
        driver.get(self.BASE_URL)
        
        # Кликаем по табу "Соусы"
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        
        # Проверяем, что активный таб - "Соусы"
        active_tab = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.ACTIVE_TAB)
        )
        assert active_tab.text in ["Соусы"], "Не удалось переключиться на раздел 'Соусы'"
        
        driver.quit()
    
    def test_switch_to_fillings_section(self, driver, web_wait):
        """Проверка перехода к разделу 'Начинки'"""
        driver.get(self.BASE_URL)
        
        # Кликаем по табу "Начинки"
        driver.find_element(*StellarBurgersLocators.FILLINGS_TAB).click()
        
        # Проверяем, что активный таб - "Начинки"
        active_tab = web_wait.until(
            EC.visibility_of_element_located(StellarBurgersLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Начинки", "Не удалось переключиться на раздел 'Начинки'"
        
        driver.quit()