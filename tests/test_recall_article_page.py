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
    recall_article_page.get_title()
    recall_article_page.close_modal()
    yield recall_article_page
    recall_article_page.driver.close()


def test_disclaimer(recall_article_page):
    """Asserts disclaimer text is right."""
    disclaimer_text = recall_article_page.get_disclaimer_text()
    assert disclaimer_text == TestData.RECALL_ARTICLE_DISC_TEXT


def test_how_it_works_button(recall_article_page):
    """Asserts FAQ button's href is right."""
    assert recall_article_page.get_how_it_works_href() == TestData.FAQ_URL


def test_footer_text(recall_article_page):
    """Asserts footer text is right."""
    assert recall_article_page.get_footer_text() == TestData.FOOTER_TEXT


def test_facebook_share(recall_article_page, current_url=TestData.RECALL_ARTICLE_URL):
    """Asserts facebook share button's href is right."""
    assert (
        TestData.FACEBOOK_SHARER_URL + current_url
        == recall_article_page.get_facebook_share_href()
    )


def test_twitter_share(recall_article_page, current_url=TestData.RECALL_ARTICLE_URL):
    """Asserts twitter share button's href is right."""
    href = recall_article_page.get_twitter_share_href()
    title = recall_article_page.get_title()
    assert (
        f"{TestData.TWITTER_SHARER_URL}text={title}&via=ConsumerAffairs&url={current_url}"
        == href
    )


def test_email_share(recall_article_page, current_url=TestData.RECALL_ARTICLE_URL):
    """Asserts email share button's href is right."""
    assert (
        TestData.EMAIL_SHARER_URL + current_url
        == recall_article_page.get_email_share_href()
    )


def test_find_my_match(recall_article_page):
    """Asserts find my match redirects correctly"""
    recall_article_page.fill_zip_code(TestData.ZIP_CODE)
    recall_article_page.click_find_my_match()
    recall_article_page.switch_next_tab()
    assert (
        recall_article_page.driver.current_url
        == TestData.FIND_MY_MATCH_URL + TestData.ZIP_CODE
    )
    recall_article_page.close_tab()


def test_related_news(recall_article_page):
    """Asserts the first and last links on the related news modal redirect to a working article"""
    related_news = recall_article_page.get_related_news()
    if not related_news:
        pytest.skip("This article has no related news")
    for news in related_news:
        recall_article_page.driver.get(news)
        test_disclaimer(recall_article_page)
        test_footer_text(recall_article_page)
        test_facebook_share(recall_article_page, news)
        test_email_share(recall_article_page, news)
        test_twitter_share(recall_article_page, news)
