from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Parent class for pages"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def click_and_wait_redirect(self, locator):
        self.do_click(locator)
        WebDriverWait(self.driver, 5).until(lambda driver: len(driver.window_handles) > 1)

    def switch_next_tab(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def close_tab(self):
        self.driver.close()

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return element.text
