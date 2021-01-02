from datetime import date, datetime
from constants import file_constants, sitrep_column_constants
from constants.sitrep_column_constants import column_title_to_letter_dicts
from excel_util import get_last_row, get_cell
from openpyxl import load_workbook

# Given an input file path to an existing sitrep excel file,
# adds a new record for the report_date input, and writes the file to output_file_path
# TODO: Validations?
# If you want to overwrite the same file, set input_file_path and output_file_path to be the same.
from vhd_soda import get_vdh_data

def generate_report_for_day(input_file_path: str, output_file_path: str, report_date: date):

    column_title_to_value_dict = {}
    column_title_to_value_dict[sitrep_column_constants.DATE_COLUMN] = report_date
    column_title_to_value_dict[sitrep_column_constants.TIME_COLUMN] = datetime.utcnow().time()

    vdh_dict = get_vdh_data(report_date)

    column_title_to_value_dict.update(vdh_dict)

    # Load the workbook
    wb = load_workbook(filename=input_file_path)

    # Pull the sheet
    sheet = wb[file_constants.SHEET_NAME]

    # Add a row at the end
    last_row_number = get_last_row(sheet) + 1
    sheet.insert_rows(last_row_number)

    # Update the last row with values for report_date
    # TODO: Check if this is the correct format
    for column_title, column_letter in column_title_to_letter_dicts.items():
        sheet[get_cell(column_letter, last_row_number)] = column_title_to_value_dict[column_title]

    # Save the workbook
    wb.save(filename=output_file_path)