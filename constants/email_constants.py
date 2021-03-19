from datetime import date

EMAIL_RECIPIENTS = [
    'dwint94@gmail.com',
    'stevewintermeyer1@gmail.com',
    'swinterm@gmu.edu'
]

RECIPIENT = 'dwint94@gmail.com'

# https://docs.aws.amazon.com/ses/latest/DeveloperGuide/examples-send-raw-using-sdk.html
# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "David Wintermeyer <dwint94@gmail.com>"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-east-1"

# The character encoding for the email.
CHARSET = "utf-8"