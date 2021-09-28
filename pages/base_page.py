class BasePage:
    """Parent class for pages."""

    def __init__(self, browser, url, load=True):
        self.browser = browser
        if load:
            self.load(url)

    @property
    def url(self):
        return self.browser.current_url

    def load(self, url):
        self.browser.get(url)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.browser.close()
