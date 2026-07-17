Feature: Email account authentication and send email
   
#    Scenario: User logs in and logs out successfully
#        Given the Outlook login page is open
#        When I login with valid credentials
#        Then the inbox should be displayed
#        When I log out
#        Then I should be logged out

#    Scenario: User sends an email to a saved contact
#        Given the Outlook login page is open
#        When I login with valid credentials
#        Then the inbox should be displayed
#        When I compose an email for a saved contact
#        And I send the email
#        Then the email should be present in Sent Items
#        When I log out
#        Then I should be logged out
   
    Scenario: User sends an email with an attachment to a saved contact
        Given the Outlook login page is open
        When I login with valid credentials
        Then the inbox should be displayed
        When I compose an email for a saved contact
        And I attach a test file
        And I send the email
        Then the email should be present in Sent Items
        When I log out
        Then I should be logged out