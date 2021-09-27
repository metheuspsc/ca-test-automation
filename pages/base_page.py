from urllib.parse import unquote

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Parent class for pages"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def do_submit(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).submit()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(text)
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element_value(locator, text))

    def click_and_wait_redirect(self, locator):
        self.do_submit(locator)
        WebDriverWait(self.driver, 5).until(lambda driver: len(driver.window_handles) > 1)

    def switch_next_tab(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def close_tab(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_href(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        href = element.get_attribute('href')
        return unquote(href)
