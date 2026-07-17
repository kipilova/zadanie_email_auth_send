import re

from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self) -> None:
        self.page.goto(self.base_url)
        ##self.page.pause()

    def login(self, email: str, password: str) -> None:
        self.page.get_by_role("link", name="Sign in", exact=True).click()
        ##self.page.pause()

        self.page.get_by_role("textbox", name="Enter your email, phone, or Skype").fill(email)
        self.page.get_by_role("button", name="Next").click()
        ##self.page.pause()

        self.page.get_by_role("button", name="Use your password").click()

        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Next").click()
        ##self.page.pause()


        self._decline_stay_signed_in()

        self.page.wait_for_url("**/mail/**", timeout=30_000)


    def _decline_stay_signed_in(self) -> None:
        stay_signed_in_box = self.page.get_by_text("Skip having to sign in every time.")

        try:
            stay_signed_in_box.wait_for(
                state="visible",
                timeout=5_000,
            )

            self.page.get_by_test_id("secondaryButton").click()

        except PlaywrightTimeoutError:
            pass
        
    def expect_inbox_to_be_visible(self) -> None:
        inbox = self.page.get_by_text("Inbox", exact=True).first

        expect(inbox).to_be_visible(timeout=30_000)
        ##self.page.pause()
        
    def logout(self, account_button_name: str) -> None:
        account_manager = self.page.get_by_role("button", name=account_button_name, exact=True)

        expect(account_manager).to_be_visible(timeout=30_000)
        account_manager.click()
        ##self.page.pause()

        sign_out = self.page.get_by_role("button", name="Sign out of this account")

        expect(sign_out).to_be_visible(timeout=30_000)
        sign_out.click()
        ##self.page.pause()

    def expect_user_to_be_logged_out(self) -> None:
        self.page.wait_for_url("**msn**", timeout=30_000)

        sign_in_button = self.page.get_by_role("button", name="Sign in to your account")

        expect(sign_in_button).to_be_visible(timeout=30_000)