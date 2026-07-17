from pytest_bdd import given, scenarios, then, when
from pathlib import Path
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.send_mail_page import SendMailPage

scenarios("authentication.feature")

@given("the Outlook login page is open")
def open_login_page(login_page: LoginPage) -> None:
    login_page.open()

@when("I login with valid credentials")
def login(login_page: LoginPage, email_credentials: dict[str, str]) -> None:
    login_page.login(
        email = email_credentials["email"],
        password = email_credentials["password"]
    )

@then("the inbox should be displayed")
def verify_inbox(login_page: LoginPage) -> None:
    ##assert page.get_by_text("Inbox", exact=True).is_visible()
    login_page.expect_inbox_to_be_visible()

@when("I log out")
def logout(login_page: LoginPage, account_button_name: str) -> None:
    login_page.logout(account_button_name)

@then("I should be logged out")
def verify_logout(login_page: LoginPage) -> None:
    login_page.expect_user_to_be_logged_out()



@when("I compose an email for a saved contact")
def compose_email(mail_page: SendMailPage, contact_data: dict[str, str], email_message_data: dict[str, str]) -> None:
    mail_page.compose_email(
        contact_name=contact_data["name"],
        contact_email=contact_data["email"],
        subject=email_message_data["subject"],
        body=email_message_data["body"]
    )

@when("I attach a test file")
def attach_test_file(mail_page: SendMailPage, attachment_path: Path) -> None:
    mail_page.attach_file(attachment_path)

@when("I send the email")
def send_email(mail_page: SendMailPage) -> None:
    mail_page.send_email()

@then("the email should be present in Sent Items")
def verify_email_was_sent(mail_page: SendMailPage, email_message_data: dict[str, str]) -> None:
    mail_page.expect_email_in_sent_items(
        email_message_data["subject"]
    )