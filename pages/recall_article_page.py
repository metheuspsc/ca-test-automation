from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecallArticlePage(BasePage):
    DISCLAIMER = (By.CLASS_NAME, "js-discl")
    FAQ_BTN = (By.CLASS_NAME, "ca-a--thrd")
    FOOTER = (By.CLASS_NAME, "ca-ft")
    FACEBOOK_SHARE = (By.CSS_SELECTOR, "//a[@title='Share on Facebook']")
    TWITTER_SHARE = (By.CSS_SELECTOR, "//a[@title='Share on Twitter']")
    EMAIL_SHARE = (By.CSS_SELECTOR, "//a[@title='Share via Email']")
    FIND_MY_MATCH_ZIP_INPUT = (By.CLASS_NAME, "ca-mt-zip__input")
    FIND_MY_MATCH_ZIP_SUBMIT = (By.CLASS_NAME, "ca-mt-zip__btn")
    LATEST_NEWS = (By.CLASS_NAME, "article-links")
    NEWS_CART = (By.CLASS_NAME, "ca-card")

    def __init__(self, driver):
        super().__init__(driver)

    def get_disclaimer_text(self):
        return self.get_element_text(self.DISCLAIMER)

    def click_how_it_works(self):
        self.click_and_wait_redirect(self.FAQ_BTN)

