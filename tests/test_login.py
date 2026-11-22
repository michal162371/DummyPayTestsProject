import pytest
from utilities.credentials import VALID_USERNAME, VALID_PASSWORD

# def test_login_with_valid_credentials(login_page):
    
#     login_page.open()
#     login_page.get_by_role("textbox", name='Email').fill(VALID_USERNAME)
#     login_page.get_by_role("textbox", name='Password').fill(VALID_PASSWORD)
#     login_page.get_by_role("button", name='Sign in')
#     assert login_page.url.endswith("/dashboard")

import re
from playwright.sync_api import expect
from pages import login_page
from utilities.credentials import BASE_URL

@pytest.mark.regression
def test_login_with_valid_credentials(login_page):
    print(repr(VALID_USERNAME), repr(VALID_PASSWORD))
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    expect(login_page.page).to_have_url(BASE_URL)