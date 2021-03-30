import os
# coding=utf-8
from datetime import date, datetime
from pytz import timezone
import json

from email_template_generator.email_template_generator_entry_point import email_template_generator_handler

os.environ["DEBUSSY"] = "1"
os.environ["DEBUSSY"] = "1"

# generate_test_event_json
def generate_test_event_json(report_date: date):
    data = """
    {
        "Records": [
            {
                "eventVersion": "2.1",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "2021-03-29T22:18:04.645Z",
                "eventName": "ObjectCreated:Copy",
                "userIdentity": {
                    "principalId": "A3GDKR019UAWM"
                },
                "requestParameters": {
                    "sourceIPAddress": "72.21.198.66"
                },
                "responseElements": {
                    "x-amz-request-id": "VP76A4QJ3Y9FRP4S",
                    "x-amz-id-2": "8mXfy3yhAbS4hogKLt0k2Btm0MINxJqcSgiNm7wg0PWFX3IzkKltv0wS2/V0kwGcTwmS47RTCDnJVlnrgoayROrnF6eWPTkP"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "8531f1ac-1fa5-4b42-a91c-54efa2762122",
                    "bucket": {
                        "name": "dadsitrepformason-public.com",
                        "ownerIdentity": {
                            "principalId": "A3GDKR019UAWM"
                        },
                        "arn": "arn:aws:s3:::dadsitrepformason-public.com"
                    },
                    "object": {
                        "key": "uploadedSitReps/Complete_Covid-19_SitRep_Data-V3-03-29-2021.xlsx",
                        "size": 104399,
                        "eTag": "c0b951a89055a8e8e395b2c273829995",
                        "versionId": "AhXsR1VSomOvbbjjTO7GmVDKHRN39D3I",
                        "sequencer": "006052AA5180D8291F"
                    }
                }
            }
        ]
    }
    """
    return json.loads(data)

# Set date and time for Report, if you want to test for a report in the past
# use the get_days_ago function

from util.date_util import get_days_ago

tz = timezone('EST')
report_date = datetime.now(tz).date()
# report_date = get_days_ago(report_date, 7)

s3_event_json = generate_test_event_json(report_date)
email_template_generator_handler(s3_event_json, None)
