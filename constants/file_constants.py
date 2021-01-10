# Local filepath
# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
from datetime import date

from openpyxl.styles import NamedStyle

from constants import sitrep_column_constants

S3_BUCKET_NAME = 'dadsitrepformason'

# Using the same format as the csse github i.e.
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv
# key looks like Covid-19_SitRep_Data-01-01-2021.csv
BASE_FILE_PATH = 'Covid-19_SitRep_Data-'
EXCEL_EXTENSION = '.xlsx'

def get_s3_key(report_date: date):
    date_str = report_date.strftime('%m-%d-%Y')
    return BASE_FILE_PATH + date_str + EXCEL_EXTENSION

SIT_REP_FILE_PATH = 'Covid-19_SitRep_Data.xlsx'
SHEET_NAME = 'Sheet1'

# Formatting
# https://stackoverflow.com/questions/24370385/how-to-format-cell-with-datetime-object-of-the-form-yyyy-mm-dd-hhmmss-in-exc
# https://support.microsoft.com/en-us/office/format-a-date-the-way-you-want-8e10019e-d5d8-47a1-ba95-db95123d273e
# the names must be unique


def get_style_dict(report_date: date) -> dict:
    date_string = report_date.strftime('%m-%d-%Y')
    date_style = NamedStyle(name='date_style' + date_string, number_format='d-mmm')
    time_style = NamedStyle(name='time_style' + date_string, number_format='HH:MM')
    number_style = NamedStyle(name='number_style' + date_string, number_format='#,###')
    percent_style = NamedStyle(name='percent_style'+ date_string, number_format='#.#%')

    style_dict = {
        sitrep_column_constants.DATE_COLUMN: date_style,
        sitrep_column_constants.TIME_COLUMN: time_style,
        sitrep_column_constants.GLOBAL_CASES_COLUMN: number_style,
        sitrep_column_constants.GLOBAL_DEATHS_COLUMN: number_style,
        sitrep_column_constants.US_CASES_COLUMN: number_style,
        sitrep_column_constants.US_DEATHS_COLUMN: number_style,
        sitrep_column_constants.VA_CASES_TOTAL_COLUMN: number_style,
        sitrep_column_constants.VA_POSITIVE_TEST_RATE_COLUMN: percent_style,
        sitrep_column_constants.VA_DEATHS_TOTAL_COLUMN: number_style,
        sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CURRENT_COLUMN: number_style,
        sitrep_column_constants.FAIRFAX_CASES_COLUMN: number_style,
        sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_COLUMN: percent_style,
        sitrep_column_constants.FAIRFAX_HOSPITALIZATIONS_COLUMN: number_style,
        sitrep_column_constants.FAIRFAX_DEATHS_COLUMN: number_style,
        sitrep_column_constants.ARLINGTON_CASES_COLUMN: number_style,
        sitrep_column_constants.ARLINGTON_POSITIVE_TEST_RATE_COLUMN: percent_style,
        sitrep_column_constants.ARLINGTON_HOSPITALIZATIONS_COLUMN: number_style,
        sitrep_column_constants.ARLINGTON_DEATHS_COLUMN: number_style,
        sitrep_column_constants.PW_CASES_COLUMN: number_style,
        sitrep_column_constants.PW_POSITIVE_TEST_RATE_COLUMN: percent_style,
        sitrep_column_constants.PW_HOSPITALIZATIONS_COLUMN: number_style,
        sitrep_column_constants.PW_DEATHS_COLUMN: number_style
    }

    return style_dict