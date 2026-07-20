# Login do emailu

This project contains an automated BDD test for Outlook.com.

## Tested scenario

Block level 1:

- Login to an Outlook email account
- Verify that the inbox is displayed
- Logout from the email account
- Verify that the user is logged out

### Block level 2

- Login to an Outlook email account
- Create an email for a recipient saved in Outlook contacts
- Send the email
- Verify that the email is present in Sent Items
- Logout from the email account

### Block level 3

- Login to an Outlook email account
- Create an email for a recipient saved in Outlook contacts
- Attach a test file
- Send the email
- Verify that the email is present in Sent Items
- Logout from the email account

## Technologies

- Python
- Playwright
- pytest
- pytest-bdd
- Gherkin

## Installation

Create and activate a virtual environment:

py -m venv .venv
.\.venv\Scripts\Activate.ps1

## Example
Screen record from testing: https://drive.google.com/file/d/1yZqB3pmEOP-QH2LhuAxwEYh0H2YMPwzE/view?usp=sharing

<img width="1452" height="275" alt="image" src="https://github.com/user-attachments/assets/2c1acf9d-ab24-49bb-8899-3803d1e4a188" />
