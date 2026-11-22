"""Home is verified only as the application's entry URL. No invented controls."""

from playwright.sync_api import Locator, Response

from pages.base_page import BasePage


class HomePage(BasePage):
    def open(self) -> Response | None:
        return self.open_root()

    def headings(self) -> Locator:
        return self.page.locator("h1, h2, h3")

    def visible_navigation_links(self) -> Locator:
        return self.page.locator("a[href]:visible")