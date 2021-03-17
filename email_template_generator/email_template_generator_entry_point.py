import json

## email_template_generator_handler invoked with event:
from openpyxl import load_workbook

from constants.file_constants import get_s3_key, PRIVATE_S3_BUCKET_NAME
from util.s3_util import download_file, upload_workbook


def get_bucket_and_key_from_event(event: dict) -> []:
    individual_record = event["Records"][0]
    s3_record = individual_record["s3"]
    bucket = s3_record["bucket"]["name"]
    key = s3_record["object"]["key"]
    return [bucket, key]


def email_template_generator_handler(event, context):
    print("email_template_generator_handler invoked with event: " + json.dumps(event))

    bucket_and_key = get_bucket_and_key_from_event(event)
    source_bucket = bucket_and_key[0]
    source_key = bucket_and_key[1]

    # Load the workbook
    print("downloading file from bucket: " + source_bucket + " with key: " + source_key)
    # https://stackoverflow.com/questions/17195569/using-a-variable-in-a-try-catch-finally-statement-without-declaring-it-outside
    try:
        file = download_file(bucket=source_bucket, key=source_key)
    except Exception as exc:
        raise RuntimeError('Failed to file from bucket: ' + source_bucket + ' with key: ' + source_key) from exc
    wb = load_workbook(file)

    # generate the email format and share it with dad as an
    individual_record = event["Records"][0]["eventTime"]
    report_date_time = get_report_date_time(individual_record)
    report_date = report_date_time.date()

    # Write the report to the non-public bucket
    new_report_s3_key = get_s3_key(report_date)
    upload_workbook(workbook=wb, bucket=PRIVATE_S3_BUCKET_NAME, key= new_report_s3_key)
c

# Virginia/DC/Maryland
# Virginia (case and death data from VDH.  Hospitalization data from Virginia Health and Hospital Association website/dashboard).
# Total cases: 590,625  (up 1,250 since previous day)
# 5.5% positive test rate (7 day PCR positive rate; down 0.2% since previous day)
# Deaths: 9,902 (up 53 since previous day)
# Hospitalizations:  Present 1,129 (down 7 since previous day) Discharges: Cumulative 48,804 (up 98 since previous day)
#
# Fairfax County
# 69,070 cases (up 138 since previous day)
# 5.5% positive test rate (7 day PCR positive test rate; down 0.1% since previous day)
# 3,630 cumulative number of hospitalizations (up 2 since previous day)
# 1,052 deaths (no change since previous day)
#
# Arlington
# 13,526 cases (up 25 since previous day)
# 4.2% positive test rate (7 day PCR positive test rate; down 0.1% since previous day)
# 781 cumulative number of hospitalizations (up 3  since previous day)
# 241 deaths (up 1 since previous day)
#
# Prince William
# 45,363 cases (up 54 since previous day)
# 6.5% positive test rate (7 day PCR positive test rate; down 0.3% since previous day)
# 1,687 cumulative number of hospitalizations (up 16 since previous day)
# 513 deaths (no change since previous day)
#
# George Mason
# New cases since 1/25/2021.
# 169 student cases (up 1 since previous day)
# 91 residential student cases (no change since previous day)
# 78 non-residential student cases (up 1 since previous day)
# 36 employee cases (up 1 since previous day)
# 2 contractor cases (no change since previous day)
#
# 33 active total cases (down 5 since previous day)
# 13 active residential student cases (down 1 since previous day)
# 15 active non-residential student cases (down 1 since previous day)
# 5 active employee case (down 3 since previous day)
# 0 active contractor cases (no change since previous day)
#
# Residential Case Data are from 3/7
# Residential students presently in Isolation or Quarantine on and off campus):
# 3 in isolation on campus (no change since previous day)
# 4 in isolation off campus (down 1 since previous day)
# 4 in quarantine on campus (up 1 since previous day)
# 5 in quarantine off campus (no change since previous day)
#
# Global:  118,031,918 cases/2,619,866 deaths
#
# US:   29,154,659 cases/529,263 deaths
