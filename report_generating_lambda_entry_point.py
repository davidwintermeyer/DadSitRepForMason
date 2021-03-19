import json
import traceback
from datetime import date

from constants.email_constants import EMAIL_RECIPIENTS
from constants.file_constants import PRIVATE_S3_BUCKET_NAME, get_s3_key
from generate_sit_rep import generate_report_for_day_s3
from util.lambda_util import get_report_date_time
from util.ses_util import send_report_as_attachment
from util.date_util import get_days_ago


# The email body for recipients with non-HTML email clients.
BODY_TEXT = "Hello,\r\nPlease see the attached sit rep file"

# The HTML body of the email.
BODY_HTML = """\
<html>
<head></head>
<body>
<h1>Hello!</h1>
<p>Please see the attached sitrep file.</p>
</body>
</html>
"""

def get_subject(report_date: date) -> str:
    date_str = report_date.strftime('%m/%d/%Y')

    return "Mason Covid Sitrep Report Date: " + date_str

def report_generating_lambda_handler(event, context):
    print("lambda_handler invoked with event: " + json.dumps(event))
    date_time_str_utc = event['time']
    report_date_time = get_report_date_time(date_time_str_utc)
    report_date = report_date_time.date()
    previous_report_date = get_days_ago(report_date, 1)
    report_time = report_date_time.time()

    # Executes the generate_report_for_day
    previous_report_s3_key = get_s3_key(previous_report_date)
    new_report_s3_key = get_s3_key(report_date)
    try:
        report_local_path = generate_report_for_day_s3(s3bucket=PRIVATE_S3_BUCKET_NAME, previous_report_s3_key=previous_report_s3_key, new_report_s3_key=new_report_s3_key, report_date=report_date, report_time=report_time)
        send_report_as_attachment(report_local_path=report_local_path, subject=get_subject(report_date), email_recipients=EMAIL_RECIPIENTS, body_text=BODY_TEXT, body_html=BODY_HTML)
    except Exception as exc:
        traceback.print_exc()
        raise RuntimeError('Failed to process SitRep report for date: ' + new_report_s3_key) from exc
