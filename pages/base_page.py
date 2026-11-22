"""A minimal POM foundation, without assumptions about site screens."""

from playwright.sync_api import Page, Response


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_path(self, path: str) -> Response | None:
        """Open a path relative to base_url (set on the browser context)."""
        return self.page.goto(path, wait_until="domcontentloaded")

    def open_root(self) -> Response | None:
        """Open the only URL verified in the assignment."""
        return self.open_path("/")