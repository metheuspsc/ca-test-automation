import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.browser import Browser
from types import SimpleNamespace


@pytest.fixture(scope="session")
def test_data():
    return SimpleNamespace(
        RECALL_ARTICLE_URL="https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html",
        RECALL_ARTICLE_DISC_TEXT="ConsumerAffairs is not a government agency and may be compensated by companies displayed. How it works.",
        FAQ_URL="https://www.consumeraffairs.com/about/faq/",
        FOOTER_TEXT="ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers.",
        FIND_MY_MATCH_WARRANTY_URL="https://my.consumeraffairs.com/home-warranty/?element_label=in_content_mt_cta&zip=",
        FIND_MY_MATCH_ALARM_URL="https://my.consumeraffairs.com/home-alarm/get-matched/?element_label=in_content_mt_cta&zip=",
        ZIP_CODE="98001",
    )


@pytest.fixture(scope="session")
def browser():
    options = Options()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return Browser(driver)
