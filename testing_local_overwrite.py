# coding=utf-8
from datetime import datetime
from pytz import timezone

from generate_sit_rep import generate_report_for_day_write_file_locally

SIT_REP_FILE_PATH = 'Covid-19_SitRep_Data-01-19-2021.xlsx'

# Set Current date and time
from util.date_util import get_days_ago

tz = timezone('EST')
report_date = datetime.now(tz).date()
# report_date = get_days_ago(report_date, 7)
report_time = datetime.now(tz).time()

# Currently, reads file from SIT_REP_FILE_PATH and then overwrites it
input_file_path = SIT_REP_FILE_PATH
output_file_path = SIT_REP_FILE_PATH

# Executes the generate_report_for_day
generate_report_for_day_write_file_locally(input_file_path, output_file_path, report_date, report_time)