import json
from datetime import datetime
from pytz import timezone

from constants import file_constants
from generate_sit_rep import generate_report_for_day


def lambda_handler(event, context):
    # Set Current date and time
    from util.date_util import get_days_ago

    print("lambda_handler invoked with event: " + json.dumps(event))

    tz = timezone('EST')
    report_date = datetime.now(tz).date()
    # report_date = get_days_ago(report_date, 1)
    report_time = datetime.now(tz).time()

    # Currently, reads file from file_constants.SIT_REP_FILE_PATH and then overwrites it
    # file_constants.SIT_REP_FILE_PATH
    input_file_path = file_constants.SIT_REP_FILE_PATH
    output_file_path = file_constants.SIT_REP_FILE_PATH

    # Executes the generate_report_for_day
    generate_report_for_day(input_file_path, output_file_path, report_date, report_time)

