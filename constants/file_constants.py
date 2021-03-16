# Local filepath
# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
from datetime import date

from openpyxl.styles import NamedStyle

from constants import sitrep_column_constants

S3_BUCKET_NAME = 'dadsitrepformason'

# Using the same format as the csse github i.e.
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv
# key looks like Covid-19_SitRep_Data-01-01-2021.csv
V3_STRING = 'V3'
FILE_NAME_PREFIX = 'Covid-19_SitRep_Data-V3-'
EXCEL_EXTENSION = '.xlsx'


def get_s3_key(report_date: date):
    return V3_STRING + '/' + get_file_name(report_date)


def get_file_name(report_date: date) -> str:
    date_str = report_date.strftime('%m-%d-%Y')
    return FILE_NAME_PREFIX + date_str + EXCEL_EXTENSION

SHEET_NAME = 'Sheet1'

# Formatting
# https://stackoverflow.com/questions/24370385/how-to-format-cell-with-datetime-object-of-the-form-yyyy-mm-dd-hhmmss-in-exc
# https://support.microsoft.com/en-us/office/format-a-date-the-way-you-want-8e10019e-d5d8-47a1-ba95-db95123d273e
# the names must be unique
# https://stackoverflow.com/questions/45055488/style-normal-exists-already-python-openpyxl
DATE_STYLE_NAME = 'date_style'
TIME_STYLE_NAME = 'time_style'
NUMBER_STYLE_NAME = 'number_style'
PERCENT_STYLE_NAME = 'percent_style'

DATE_STYLE = NamedStyle(name=DATE_STYLE_NAME, number_format='d-mmm')
TIME_STYLE = NamedStyle(name=TIME_STYLE_NAME, number_format='HH:MM')
NUMBER_STYLE = NamedStyle(name=NUMBER_STYLE_NAME, number_format='#,###')
PERCENT_STYLE = NamedStyle(name=PERCENT_STYLE_NAME, number_format='#.#%')

STYLE_NAME_TO_STYLE_DICT = {
    DATE_STYLE_NAME: DATE_STYLE,
    TIME_STYLE_NAME: TIME_STYLE,
    NUMBER_STYLE_NAME: NUMBER_STYLE,
    PERCENT_STYLE_NAME: PERCENT_STYLE
}

COLUMN_NAME_TO_STYLE_NAME_DICT = {
    sitrep_column_constants.DATE_COLUMN: DATE_STYLE_NAME,
    sitrep_column_constants.TIME_COLUMN: TIME_STYLE_NAME,
    sitrep_column_constants.GLOBAL_CASES_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.GLOBAL_DEATHS_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.US_CASES_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.US_DEATHS_COLUMN: NUMBER_STYLE_NAME,

    sitrep_column_constants.VA_CASES_TOTAL_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.VA_CASES_CHANGE_PREVIOUS_DAY_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.VA_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.VA_POSITIVE_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.VA_DEATHS_TOTAL_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.VA_DEATHS_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CURRENT_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: NUMBER_STYLE_NAME,

    sitrep_column_constants.FAIRFAX_CASES_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.FAIRFAX_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.FAIRFAX_HOSPITALIZATIONS_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.FAIRFAX_DEATHS_COLUMN: NUMBER_STYLE_NAME,

    sitrep_column_constants.ARLINGTON_CASES_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.ARLINGTON_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.ARLINGTON_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.ARLINGTON_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.ARLINGTON_HOSPITALIZATIONS_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.ARLINGTON_DEATHS_COLUMN: NUMBER_STYLE_NAME,

    sitrep_column_constants.PW_CASES_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.PW_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.PW_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.PW_POSITIVE_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN: PERCENT_STYLE_NAME,
    sitrep_column_constants.PW_HOSPITALIZATIONS_COLUMN: NUMBER_STYLE_NAME,
    sitrep_column_constants.PW_DEATHS_COLUMN: NUMBER_STYLE_NAME
}


# 1/5/2021 is hardcoded as row 92
def get_row_number(report_date: date) -> int:
    f_date = date(2021, 1, 5)
    delta = report_date - f_date
    return 92 + delta.days
