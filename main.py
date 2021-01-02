# coding=utf-8
from datetime import datetime

from constants import file_constants
from generate_sit_rep import generate_report_for_day

# Set Current date
today_date = datetime.utcnow().date()

# Currently, reads file from file_constants.SIT_REP_FILE_PATH and then overwrites it
# file_constants.SIT_REP_FILE_PATH
input_file_path = file_constants.SIT_REP_FILE_PATH
output_file_path = file_constants.SIT_REP_FILE_PATH

# Executes the generate_report_for_day
generate_report_for_day(input_file_path, output_file_path, today_date)