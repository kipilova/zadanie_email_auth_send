import re
from pathlib import Path

from playwright.sync_api import Page, expect


class SendMailPage:
    def __init__(self, page: Page):
        self.page = page

    def compose_email(self, contact_name: str, contact_email: str, subject: str, body: str) -> None:
        new_email_button = self.page.get_by_role("button", name="New email")

        expect(new_email_button).to_be_visible(timeout=10_000)
        new_email_button.click()

        send_button = self.page.get_by_role("button", name="Send", description="Send (Ctrl+Enter)")

        expect(send_button).to_be_visible(timeout=10_000)

        recipient_input = self.page.get_by_label("To", exact=True)

        recipient_input.fill(contact_name)

        contact_suggestion = self.page.get_by_role("option", name=f"{contact_name} - {contact_email}", exact=True)

        expect(contact_suggestion).to_be_visible(timeout=10_000)
        contact_suggestion.click()

        subject_input = self.page.get_by_role("textbox", name="Subject")

        expect(subject_input).to_be_visible(timeout=10_000)
        subject_input.fill(subject)

        message_body = self.page.get_by_role("textbox", name="Message body")

        expect(message_body).to_be_visible(timeout=10_000)
        message_body.fill(body)

        

    def attach_file(self, file_path: Path) -> None:
        attach_button = self.page.get_by_role("button", name="Attach file")

        expect(attach_button).to_be_visible(timeout=10_000)
        attach_button.click()

        browse_option = self.page.get_by_role("menuitem", name="Browse this computer")

        expect(browse_option).to_be_visible(timeout=10_000)

        with self.page.expect_file_chooser() as file_chooser_info:
            browse_option.click()

        file_chooser = file_chooser_info.value
        file_chooser.set_files(str(file_path))

        attachment_name = self.page.get_by_text("sample_attach.txt")

        expect(attachment_name).to_be_visible(timeout=30_000)


    def send_email(self) -> None:
        send_button = self.page.get_by_role(
            "button",
            name=re.compile(r"^Send\b", re.IGNORECASE),
        ).first

        expect(send_button).to_be_enabled(timeout=10_000)
        send_button.click()

    def expect_email_in_sent_items(self, subject: str) -> None:
        sent_items = self.page.get_by_role(
            "treeitem",
            name=re.compile(r"^Sent Items", re.IGNORECASE),
        )

        expect(sent_items).to_be_visible(timeout=30_000)
        sent_items.click()

        sent_message = self.page.get_by_text(
            subject,
            exact=True,
        ).first

        expect(sent_message).to_be_visible(timeout=30_000)