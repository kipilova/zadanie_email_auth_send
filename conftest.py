import os 

from datetime import datetime, timezone
from pathlib import Path

import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.send_mail_page import SendMailPage
from playwright.sync_api import Page

load_dotenv()

@pytest.fixture
def email_credentials() -> dict[str, str]:
    email = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")

    if not email or not password:
        raise ValueError("EMAIL_USERNAME and EMAIL_PASSWORD must be defined in the .env file.")
    
    return {
        "email": email,
        "password": password
    }

@pytest.fixture
def outlook_base_url() -> str:
    value = os.getenv("BASE_URL")

    if not value:
        raise ValueError("BASE_URL must be defined in the .env file.")

    return value

@pytest.fixture
def login_page(page, outlook_base_url: str) -> LoginPage:
    return LoginPage(page, outlook_base_url)

@pytest.fixture
def account_button_name() -> str:
    value = os.getenv("ACCOUNT_BUTTON_NAME")

    if not value:
        raise ValueError("ACCOUNT_BUTTON_NAME must be defined in the .env file.")

    return value



@pytest.fixture
def contact_data() -> dict[str, str]:
    contact_name = os.getenv("CONTACT_NAME")
    contact_email = os.getenv("CONTACT_EMAIL")

    if not contact_name or not contact_email:
        raise ValueError(
            "CONTACT_NAME and CONTACT_EMAIL must be defined in the .env file."
        )

    return {
        "name": contact_name,
        "email": contact_email,
    }

@pytest.fixture
def email_message_data() -> dict[str, str]:
    timestamp = datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S"     ############ kvoli kontrole
    )

    return {
        "subject": f"Playwright automated test {timestamp}",
        "body": (
            "This is an automated email sent by a Playwright and pytest-bdd test."
        ),
    }

@pytest.fixture
def attachment_path() -> Path:
    path = (
        Path(__file__).resolve().parent
        / "test_data"
        / "sample_attach.txt"
    )

    if not path.is_file():
        raise FileNotFoundError(
            f"Test attachment was not found: {path}"
        )

    return path

@pytest.fixture
def mail_page(page: Page) -> SendMailPage:
    return SendMailPage(page)