"""Reusable POM for inspected links; do not claim a route exists until observed."""

from playwright.sync_api import Locator, Page, Response

from pages.base_page import BasePage


class DiscoveredPage(BasePage):
    def __init__(self, page: Page, path: str):
        super().__init__(page)
        self.path = path

    def open(self) -> Response | None:
        return self.open_path(self.path)

    def inputs(self) -> Locator:
        return self.page.locator("input:visible, textarea:visible, select:visible")