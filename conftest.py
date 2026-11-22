import os
from pages.login_page import LoginPage
import pytest
from dotenv import load_dotenv

from pages.discovered_page import DiscoveredPage
from pages.home_page import HomePage
from utilities.consts import DEFAULT_BASE_URL

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Site address. pytest-playwright applies it to every browser context."""
    return os.getenv("DUMMYPAY_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def discovered_page(page):
    """Factory: discovered_page("/some-path").open()"""

    def _make(path: str) -> DiscoveredPage:
        return DiscoveredPage(page, path)

    return _make


@pytest.fixture
def login_page(page):
    return LoginPage(page)