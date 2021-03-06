import os
from datetime import date

import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from typing import List

from constants.email_constants import AWS_REGION, SENDER, RECIPIENT, CHARSET

def send_report_as_attachment(report_local_path: str, email_recipients: List[str], subject: str, body_text, body_html):
    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Create a multipart/mixed parent container.
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(body_text.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(body_html.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    # Define the attachment part and encode it using MIMEApplication.
    att = MIMEApplication(open(report_local_path, 'rb').read())

    # Add a header to tell the email client to treat this part as an attachment,
    # and to give the attachment a name.
    att.add_header('Content-Disposition','attachment',filename=os.path.basename(report_local_path))

    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)

    # Add the attachment to the parent container.
    msg.attach(att)
    try:
        print("sending email message with sender: " + SENDER)
        print("sending email message with Destinations: " + ' '.join(map(str, email_recipients)))
        #Provide the contents of the email.
        response = client.send_raw_email(
            Source=SENDER,
            Destinations=email_recipients,
            RawMessage={
                'Data':msg.as_string(),
            }
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
        raise e
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])