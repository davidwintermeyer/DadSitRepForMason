from datetime import date

from openpyxl import load_workbook

# Given an input file path to an existing sitrep excel file,
# adds a new record for the report_date input, and writes the file to output_file_path
# If you want to overwrite the same file, set input_file_path and output_file_path to be the same.
from constants import file_constants


def generate_report_for_day(input_file_path: str, output_file_path: str, report_date: date):

    # Load the workbook
    wb = load_workbook(filename=input_file_path)

    # Pull the sheet
    sheet = wb[file_constants.SHEET_NAME]