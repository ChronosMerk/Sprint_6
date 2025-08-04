from selenium.webdriver.common.by import By

class FirstPageLocators:
    ORDER_NAME = By.XPATH, ".//input[@placeholder= '* Имя']"
    ORDER_LAST_NAME = By.XPATH, ".//input[@placeholder= '* Фамилия']"
    ORDER_ADDRESS = By.XPATH, ".//input[@placeholder= '* Адрес: куда привезти заказ']"
    ORDER_METRO = By.XPATH, ".//input[@placeholder= '* Станция метро']"
    ORDER_METRO_LIST =  lambda station_name: (By.XPATH, f"//div[@class='select-search__select']//div[text()='{station_name}']")
    ORDER_PHONE = By.XPATH, ".//input[@placeholder= '* Телефон: на него позвонит курьер']"
    ORDER_NEXT = By.XPATH, ".//button[text()='Далее']"

class SecondPageLocators:
    ORDER_DATE = By.XPATH, ".//input[@placeholder= '* Когда привезти самокат']"
    ORDER_PERIOD = By.XPATH, ".//span[@class='Dropdown-arrow']"
    ORDER_RENTAL_PERIOD = By.XPATH, "(//div[@class='Dropdown-option'])[1]"
    ORDER = By.XPATH, '(.//button[text()="Заказать"])[2]'
    ORDER_DESIGN = By.XPATH, ".//button[text()='Да']"
    ORDER_SUCCESS = By.XPATH, ".//div[text()='Заказ оформлен']"


