from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"  # להתאים לאתר שלך

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.open_path(self.PATH)

    @property
    def email_input(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email")

    @property
    def password_input(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in")

    def login(self, username: str, password: str) -> None:
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()