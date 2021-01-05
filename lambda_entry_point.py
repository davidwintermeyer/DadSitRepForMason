import json
from datetime import datetime
from pytz import timezone

from constants import file_constants
from constants.file_constants import S3_BUCKET_NAME, get_s3_key
from generate_sit_rep import generate_report_for_day_s3


def lambda_handler(event, context):
    # Set Current date and time
    from util.date_util import get_days_ago

    print("lambda_handler invoked with event: " + json.dumps(event))

    tz = timezone('EST')
    report_date = datetime.now(tz).date()
    previous_report_date = get_days_ago(report_date, 1)
    report_time = datetime.now(tz).time()

    # Executes the generate_report_for_day
    previous_report_file_path = get_s3_key(previous_report_date)
    new_report_file_path = get_s3_key(report_date)

    generate_report_for_day_s3(S3_BUCKET_NAME, previous_report_file_path, new_report_file_path, report_date, report_time)

