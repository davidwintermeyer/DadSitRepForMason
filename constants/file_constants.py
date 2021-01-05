# Local filepath
# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
from openpyxl.styles import NamedStyle

from constants import sitrep_column_constants

SIT_REP_FILE_PATH = 'Covid-19_SitRep_Data.xlsx'
SHEET_NAME = 'Sheet1'

# Formatting
# https://stackoverflow.com/questions/24370385/how-to-format-cell-with-datetime-object-of-the-form-yyyy-mm-dd-hhmmss-in-exc
# https://support.microsoft.com/en-us/office/format-a-date-the-way-you-want-8e10019e-d5d8-47a1-ba95-db95123d273e
# the names must be unique
DATE_STYLE = NamedStyle(name='date_style', number_format='d-mmm')
TIME_STYLE = NamedStyle(name='time_style', number_format='HH:MM')
NUMBER_STYLE = NamedStyle(name='number_style', number_format='#,###')
PERCENT_STYLE = NamedStyle(name='percent_style', number_format='#.#%')

STYLE_DICT = {
    sitrep_column_constants.DATE_COLUMN: DATE_STYLE,
    sitrep_column_constants.TIME_COLUMN: TIME_STYLE,
    sitrep_column_constants.GLOBAL_CASES_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.GLOBAL_DEATHS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.US_CASES_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.US_DEATHS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.VA_CASES_TOTAL_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.VA_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE,
    sitrep_column_constants.VA_DEATHS_TOTAL_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CURRENT_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.FAIRFAX_CASES_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE,
    sitrep_column_constants.FAIRFAX_HOSPITALIZATIONS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.FAIRFAX_DEATHS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.ARLINGTON_CASES_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.ARLINGTON_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE,
    sitrep_column_constants.ARLINGTON_HOSPITALIZATIONS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.ARLINGTON_DEATHS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.PW_CASES_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.PW_POSITIVE_TEST_RATE_COLUMN: PERCENT_STYLE,
    sitrep_column_constants.PW_HOSPITALIZATIONS_COLUMN: NUMBER_STYLE,
    sitrep_column_constants.PW_DEATHS_COLUMN: NUMBER_STYLE
}