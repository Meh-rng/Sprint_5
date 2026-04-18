from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # ===== ГЛАВНАЯ СТРАНИЦА =====
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Кнопка "Личный кабинет" в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    
    # Кнопка "Конструктор" в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    
    # Логотип Stellar Burgers
    LOGO = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a")
    
    # Кнопка "Оформить заказ" (индикатор загрузки главной страницы)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # ===== ФОРМА РЕГИСТРАЦИИ =====
    # Кнопка "Зарегистрироваться" на странице входа
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    
    # Поле ввода имени
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    # Кнопка "Зарегистрироваться" в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Сообщение об ошибке для некорректного пароля
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    
    # ===== ФОРМА ВХОДА =====
        # Заголовок формы входа
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    
    # Поле Email в форме входа - ищем по тексту label
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Поле пароля в форме входа 
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    # Кнопка «Войти» в форме входа
    LOGIN_BUTTON_FORM = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылка «Восстановить пароль» в форме входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    
    # ===== ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ =====
    # Поле ввода Email на странице восстановления пароля
    RESTORE_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    
    # Кнопка "Войти" на странице восстановления пароля
    LOGIN_BUTTON_RESTORE = (By.XPATH, "//a[@href='/login']")
    
    # ===== ЛИЧНЫЙ КАБИНЕТ =====
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # ===== КОНСТРУКТОР =====
    # ===== ТАБЫ ДЛЯ ПЕРЕКЛЮЧЕНИЯ РАЗДЕЛОВ =====
    # Таб "Булки"
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and text()='Булки']")
    
    # Таб "Соусы"
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and (text()='Соусы')]")
    
    # Таб "Начинки"
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and text()='Начинки']")
    
    # Заголовок раздела «Булки»
    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']")

    # Заголовок раздела «Соусы» (с учетом опечатки)
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы' or text()='Coyack']")

    # Заголовок раздела «Начинки»
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']")
    
    # ===== ВСПОМОГАТЕЛЬНЫЕ ЛОКАТОРЫ =====

    # Кнопка закрытия модального окна
    CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS']")