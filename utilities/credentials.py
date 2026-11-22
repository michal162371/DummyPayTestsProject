import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")
BASE_URL = os.getenv("DUMMYPAY_BASE_URL")