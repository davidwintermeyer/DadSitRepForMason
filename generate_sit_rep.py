from datetime import date, time

from openpyxl import load_workbook

from constants import file_constants, sitrep_column_constants
from constants.file_constants import STYLE_DICT
from constants.sitrep_column_constants import column_title_to_letter_dicts, NO_DATA_COLUMNS, NO_DATA
from dependencies.csse_github import get_csse_data
from util.excel_util import get_last_row, get_cell
# Given an input file path to an existing sitrep excel file,
# adds a new record for the report_date input, and writes the file to output_file_path
# TODO: Validations?
# If you want to overwrite the same file, set input_file_path and output_file_path to be the same.
from dependencies.vhd_soda import get_vdh_data

#
from util.s3_util import download_file, upload_workbook


def generate_report_for_day_s3(s3bucket: str, previous_report_file_path: str, new_report_file_path: str, report_date: date, report_time: time):

    column_title_to_value_dict = {}
    column_title_to_value_dict[sitrep_column_constants.DATE_COLUMN] = report_date
    column_title_to_value_dict[sitrep_column_constants.TIME_COLUMN] = report_time

    # csse data
    csse_data_dict = get_csse_data(report_date)
    column_title_to_value_dict.update(csse_data_dict)

    # vdh Data
    vdh_dict = get_vdh_data(report_date)
    column_title_to_value_dict.update(vdh_dict)

    # Write in No Data
    for column_title in NO_DATA_COLUMNS :
        column_title_to_value_dict[column_title] = NO_DATA

    # Load the workbook
    file = download_file(bucket=s3bucket, key=previous_report_file_path)
    wb = load_workbook(file)
    # Pull the sheet
    sheet = wb[file_constants.SHEET_NAME]

    # Add a row at the end
    last_row_number = get_last_row(sheet) + 1
    sheet.insert_rows(last_row_number)

    # Update the last row with values for report_date
    for column_title, column_letter in column_title_to_letter_dicts.items():
        cell = sheet[get_cell(column_letter, last_row_number)]
        cell.value = column_title_to_value_dict[column_title]
        if (column_title in STYLE_DICT):
            cell.style = STYLE_DICT[column_title]

    # Save the workbook
    wb.save(filename='tmp/' + new_report_file_path)
    upload_workbook(workbook=wb, bucket=s3bucket, key=new_report_file_path)


def generate_report_for_day_write_file_locally(input_file_path: str, output_file_path: str, report_date: date, report_time: time):

    column_title_to_value_dict = {}
    column_title_to_value_dict[sitrep_column_constants.DATE_COLUMN] = report_date
    column_title_to_value_dict[sitrep_column_constants.TIME_COLUMN] = report_time

    # csse data
    csse_data_dict = get_csse_data(report_date)
    column_title_to_value_dict.update(csse_data_dict)

    # vdh Data
    vdh_dict = get_vdh_data(report_date)
    column_title_to_value_dict.update(vdh_dict)

    # Write in No Data
    for column_title in NO_DATA_COLUMNS :
        column_title_to_value_dict[column_title] = NO_DATA

    # Load the workbook
    wb = load_workbook(filename=input_file_path, data_only=True)

    # Pull the sheet
    sheet = wb[file_constants.SHEET_NAME]

    # Add a row at the end
    last_row_number = get_last_row(sheet) + 1
    sheet.insert_rows(last_row_number)

    # Update the last row with values for report_date
    for column_title, column_letter in column_title_to_letter_dicts.items():
        cell = sheet[get_cell(column_letter, last_row_number)]
        cell.value = column_title_to_value_dict[column_title]
        if (column_title in STYLE_DICT):
            cell.style = STYLE_DICT[column_title]

    # Save the workbook
    wb.save(filename=output_file_path)