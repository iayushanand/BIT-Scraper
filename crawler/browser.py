from playwright.sync_api import sync_playwright

from config import HEADLESS, TIMEOUT


class Browser:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=HEADLESS
        )

        self.page = self.browser.new_page()

    def download(self, url: str) -> str:
        self.page.goto(
            url,
            wait_until="load",
            timeout=TIMEOUT
        )

        self.page.wait_for_timeout(1000)

        return self.page.content()

    def close(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()