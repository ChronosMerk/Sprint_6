from selenium.webdriver.common.by import By

class LogoPageLocators:
    YANDEX_LOGO = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'
    SCOOTER_LOGO = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    BUTTON_DZEN_SEARCH = By.XPATH, ".//button[@type='submit' and text()='Найти']"
    SCOOTER_HOME_HEADER = By.CLASS_NAME, 'Home_Header__iJKdX'