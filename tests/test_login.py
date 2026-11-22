import pytest
from utilities.credentials import VALID_USERNAME, VALID_PASSWORD
import re
from playwright.sync_api import expect
from utilities.credentials import BASE_URL

@pytest.mark.regression
@pytest.mark.smoke
def test_login_with_valid_credentials(login_page):
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    expect(login_page.page).to_have_url(BASE_URL)