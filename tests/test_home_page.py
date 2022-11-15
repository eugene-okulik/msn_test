from pages.home_page import HomePage


def test_weather(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.weather_is_displayed()
