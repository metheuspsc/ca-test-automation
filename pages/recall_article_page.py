from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecallArticlePage(BasePage):
    CLOSE_MODAL = (By.XPATH, "//a[@class='ca-modal_close']")
    DISCLAIMER = (By.CLASS_NAME, "js-discl")
    TITLE = (By.XPATH, "//h1[@itemprop='headline']")
    FAQ_BTN = (By.XPATH, "//a[@aria-label='Learn more about us via our FAQ page']")
    FOOTER = (By.XPATH, "//div[@class='ca-ft__ctnt']//p")
    FACEBOOK_SHARE = (By.XPATH, "//a[@title='Share on Facebook']")
    TWITTER_SHARE = (By.XPATH, "//a[@title='Share on Twitter']")
    RELATED_NEWS = (
        By.CSS_SELECTOR,
        "#sidebar > nav.h-sect--pad-2.h-coll-vert.article-links.related-links > a",
    )
    EMAIL_SHARE = (By.XPATH, "//a[@title='Share via Email']")
    NEWS_CART = (By.CLASS_NAME, "ca-card")
    FIND_MY_MATCH_ZIP_INPUT = (By.XPATH, "//input[@name='zip']")
    FIND_MY_MATCH_ZIP_SUBMIT = (By.CLASS_NAME, "ca-mt-zip__btn")

    def __init__(self, driver):
        super().__init__(driver)

    def get_disclaimer_text(self):
        return self.get_element_text(self.DISCLAIMER)

    def get_title(self):
        return self.get_element_text(self.TITLE)

    def get_footer_text(self):
        return self.get_element_text(self.FOOTER)

    def get_how_it_works_href(self):
        return self.get_href(self.FAQ_BTN)

    def get_facebook_share_href(self):
        return self.get_href(self.FACEBOOK_SHARE)

    def get_twitter_share_href(self):
        return self.get_href(self.TWITTER_SHARE)

    def get_email_share_href(self):
        return self.get_href(self.EMAIL_SHARE)

    def fill_zip_code(self, zip_code):
        return self.do_send_keys(self.FIND_MY_MATCH_ZIP_INPUT, zip_code)

    def click_find_my_match(self):
        self.click_and_wait_redirect(self.FIND_MY_MATCH_ZIP_SUBMIT)

    def close_modal(self):
        if self.driver.find_elements(self.CLOSE_MODAL[0], self.CLOSE_MODAL[1]):
            self.do_click(self.CLOSE_MODAL)

    def get_related_news(self):
        """Returns a list with the first and the last news on the latest news modal"""
        related_news = self.driver.find_elements(
            self.RELATED_NEWS[0], self.RELATED_NEWS[1]
        )
        if related_news:
            if len(related_news) == 1:
                return related_news[0].get_attribute("href")
            return [
                related_news[0].get_attribute("href"),
                related_news[-1].get_attribute("href"),
            ]
        return None
