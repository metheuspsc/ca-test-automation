import pytest
from pages.recall_article_page import RecallArticlePage


@pytest.fixture(scope="module")
def recall_article_page(browser, test_data):
    with RecallArticlePage(browser, test_data.RECALL_ARTICLE_URL) as recall_article_page:
        yield recall_article_page


def test_disclaimer(recall_article_page, test_data):
    """Asserts disclaimer text is right."""
    disclaimer_text = recall_article_page.get_disclaimer_text()
    assert disclaimer_text == test_data.RECALL_ARTICLE_DISC_TEXT


def test_how_it_works_button(recall_article_page, test_data):
    """Asserts FAQ button's href is right."""
    assert recall_article_page.get_how_it_works_href() == test_data.FAQ_URL


def test_footer_text(recall_article_page, test_data):
    """Asserts footer text is right."""
    assert recall_article_page.get_footer_text() == test_data.FOOTER_TEXT


def test_facebook_share(recall_article_page, test_data):
    """Asserts facebook share button's href is right."""
    assert (
            test_data.FACEBOOK_SHARER_URL + recall_article_page.url
            == recall_article_page.get_facebook_share_href()
    )


def test_twitter_share(recall_article_page, test_data):
    """Asserts twitter share button's href is right."""
    href = recall_article_page.get_twitter_share_href()
    title = recall_article_page.get_title()
    assert (
            f"{test_data.TWITTER_SHARER_URL}text={title}&via=ConsumerAffairs&url={recall_article_page.url}"
            == href
    )


def test_email_share(recall_article_page, test_data):
    """Asserts email share button's href is right."""
    assert (
            test_data.EMAIL_SHARER_URL + recall_article_page.url
            == recall_article_page.get_email_share_href()
    )


def test_find_my_match(browser, recall_article_page, test_data):
    """Asserts find my match redirects correctly"""
    recall_article_page.fill_zip_code(test_data.ZIP_CODE)
    with recall_article_page.click_find_my_match() as newtab:
        assert (
                newtab.current_url
                == test_data.FIND_MY_MATCH_URL + test_data.ZIP_CODE
        )


def test_related_news(browser, recall_article_page, test_data):
    """Asserts the first and last links on the related news modal redirect to a working article"""
    for news in recall_article_page.get_related_news():
        recall_article_page.load(news)
        test_disclaimer(recall_article_page, test_data)
        test_footer_text(recall_article_page, test_data)
        test_facebook_share(recall_article_page, test_data)
        test_email_share(recall_article_page, test_data)
        test_twitter_share(recall_article_page, test_data)
    else:
        pytest.skip("This article has no related news")
