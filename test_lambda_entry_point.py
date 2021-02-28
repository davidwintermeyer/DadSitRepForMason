import os
# coding=utf-8
from datetime import date, datetime
from pytz import timezone
import json

from lambda_entry_point import lambda_handler

os.environ["DEBUSSY"] = "1"
os.environ["DEBUSSY"] = "1"

# Given report_date (the time is always 22:00:00Z)
# generate_test_event_json
def generate_test_event_json(report_date: date):
    date_str = report_date.strftime('%Y-%m-%d')

    data = """
    {
        "version": "0",
        "id": "eca8a63a-0fae-7713-a836-7b9045067d2d",
        "detail-type": "Scheduled Event",
        "source": "aws.events",
        "account": "343806292018",
        "time": """
    data += '"'
    data += date_str
    data += """T22:00:00Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:events:us-east-1:343806292018:rule/DailyAt5pmEastern"
        ],
        "detail": {}
    }
    """
    return json.loads(data)

# Set date and time for Report, if you want to test for a report in the past
# use the get_days_ago function

from util.date_util import get_days_ago

tz = timezone('EST')
report_date = datetime.now(tz).date()
# report_date = get_days_ago(report_date, 7)

test_scheduled_event_json = generate_test_event_json(report_date)
lambda_handler(test_scheduled_event_json, None)
