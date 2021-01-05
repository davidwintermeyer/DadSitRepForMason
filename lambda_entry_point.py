import json
from datetime import datetime
from pytz import timezone

from constants import file_constants
from constants.email_constants import EMAIL_RECIPIENTS
from constants.file_constants import S3_BUCKET_NAME, get_s3_key
from generate_sit_rep import generate_report_for_day_s3
from util.ses_util import send_report_as_attachment


def lambda_handler(event, context):
    # Set Current date and time
    from util.date_util import get_days_ago

    print("lambda_handler invoked with event: " + json.dumps(event))

    tz = timezone('EST')
    report_date = datetime.now(tz).date()
    previous_report_date = get_days_ago(report_date, 1)
    report_time = datetime.now(tz).time()

    # Executes the generate_report_for_day
    previous_report_s3_key = get_s3_key(previous_report_date)
    new_report_s3_key = get_s3_key(report_date)

    report_local_path = generate_report_for_day_s3(s3bucket=S3_BUCKET_NAME, previous_report_s3_key=previous_report_s3_key, new_report_s3_key=new_report_s3_key, report_date=report_date, report_time=report_time)

    send_report_as_attachment(report_date=report_date, report_local_path=report_local_path, email_recipients=EMAIL_RECIPIENTS)

