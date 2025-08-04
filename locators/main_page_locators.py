from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = lambda index: (By.ID, f"accordion__heading-{index}")
    QUESTION_ELEMENT_SCROLL= By.ID, "accordion__heading-7"
    TEXT_INSIDE_THE_QUESTION = lambda index: (By.ID, f"accordion__panel-{index}")
    BUTTON_ORDER_UPPER = By.XPATH, "(//button[text()='Заказать'])[1]"
    BUTTON_ORDER_LOWER = By.XPATH, "(//button[text()='Заказать'])[2]"
    COOKIE_BUTTON_LOCATOR = By.ID, 'rcc-confirm-button'
