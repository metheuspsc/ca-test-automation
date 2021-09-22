import pytest
from pages.recall_article_page import RecallArticlePage
from config.config import TestData

"""
Challenge Url = https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html
- Assert redirect of "Find my match" box
- Verify links for first and last listed "related news links"
"""


@pytest.fixture(scope="module")
def recall_article_page(driver):
    recall_article_page = RecallArticlePage(driver)
    recall_article_page.driver.get(TestData.RECALL_ARTICLE_URL)
    return recall_article_page


def test_disclaimer(recall_article_page):
    disclaimer_text = recall_article_page.get_disclaimer_text()
    assert disclaimer_text == TestData.RECALL_ARTICLE_DISC_TEXT


def test_how_it_works_button(recall_article_page):
    recall_article_page.click_how_it_works()
    recall_article_page.switch_next_tab()
    assert recall_article_page.driver.current_url == TestData.FAQ_URL
    recall_article_page.close_tab()


def test_footer_text(recall_article_page):
    footer_text = recall_article_page.get_footer_text()
    assert footer_text == TestData.FOOTER_TEXT


def test_facebook_share(recall_article_page):
    recall_article_page.click_facebook_share()
    recall_article_page.switch_next_tab()
    assert TestData.FACEBOOK_SHARER_URL in recall_article_page.driver.current_url
    recall_article_page.close_tab()


def test_twitter_share(recall_article_page):
    recall_article_page.click_twitter_share()
    recall_article_page.switch_next_tab()
    assert [text in recall_article_page.driver.current_url for text in TestData.TWITTER_SHARER_URL]
    recall_article_page.close_tab()


def test_email_share(recall_article_page):
    href = recall_article_page.get_email_share_href()
    assert TestData.EMAIL_SHARER_URL in href
