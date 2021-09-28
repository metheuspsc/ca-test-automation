from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.browser import Tab


class RecallArticlePage(BasePage):
    """Assumption: locators are inside the methods to simplify"""

    @property
    def expected_twitter_share_url(self):
        return f"{'https://twitter.com/intent/tweet/?'}text={self.get_title()}&via=ConsumerAffairs&url={self.url}"

    @property
    def expected_facebook_share_url(self):
        return "https://www.facebook.com/sharer.php?u=" + self.url

    @property
    def expected_email_share_url(self):
        return "mailto:?subject=Check this ConsumerAffairs News&body=Check out this news: " + self.url

    def get_disclaimer_text(self):
        locator = (By.CLASS_NAME, "js-discl")
        return self.browser.text(locator)

    def get_title(self):
        locator = (By.XPATH, "//h1[@itemprop='headline']")
        return self.browser.text(locator)

    def get_footer_text(self):
        locator = (By.XPATH, "//div[@class='ca-ft__ctnt']//p")
        return self.browser.text(locator)

    def get_how_it_works_href(self):
        locator = (By.XPATH, "//a[@aria-label='Learn more about us via our FAQ page']")
        return self.browser.get_href(locator)

    def get_facebook_share_href(self):
        locator = (By.XPATH, "//a[@title='Share on Facebook']")
        return self.browser.get_href(locator)

    def get_twitter_share_href(self):
        locator = (By.XPATH, "//a[@title='Share on Twitter']")
        return self.browser.get_href(locator)

    def get_email_share_href(self):
        locator = (By.XPATH, "//a[@title='Share via Email']")
        return self.browser.get_href(locator)

    def fill_zip_code(self, zip_code):
        locator = (By.XPATH, "//input[@name='zip']")
        return self.browser.do_send_keys(locator, zip_code)

    def click_find_my_match(self):
        locator = (By.CLASS_NAME, "ca-mt-zip__btn")
        self.browser.click_and_wait_redirect(locator)
        return Tab(self.browser)

    def close_modal(self):
        locator = (By.XPATH, "//a[@class='ca-modal_close']")
        if self.browser.find_elements(locator[0], locator[1]):
            self.browser.do_click(locator)

    def get_related_news(self):
        """Returns a list with the first and the last news on the latest news modal"""
        locator = (By.CSS_SELECTOR, "#sidebar > nav.h-sect--pad-2.h-coll-vert.article-links.related-links")
        related_news_box = self.browser.wait_for_element(locator)
        related_news = related_news_box.find_elements(By.CSS_SELECTOR, "a")
        if related_news:
            if len(related_news) == 1:
                return related_news[0].get_attribute("href")
            return [
                related_news[0].get_attribute("href"),
                related_news[-1].get_attribute("href"),
            ]
        return []
