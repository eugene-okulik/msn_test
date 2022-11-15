from pages.base_page import BasePage
from selenium.webdriver.common.by import By


weather = (By.XPATH, '//div[@class="weather-text light-font-color"]')



class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def weather_is_displayed(self):
        return self.find(weather).is_displayed()

    def open(self):
        self.driver.get('https://www.msn.com/en-xl?AR=1')

