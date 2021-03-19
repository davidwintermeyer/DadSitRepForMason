# Get the record of that report_date
# https://zetcode.com/python/openpyxl/
from constants import sitrep_column_constants
from constants.sitrep_column_constants import column_title_to_letter_dicts

def get_row_number_of_report_date(sheet, report_date):
    # Skip header
    row_number = 2
    # currently, row 160 is 3/14/2021
    while row_number < 500:
        cell_str = column_title_to_letter_dicts[sitrep_column_constants.DATE_COLUMN] + str(row_number)
        cell = sheet[cell_str]
        # cell.value is a datetime object, call date() in it
        if cell.value.date() == report_date:
            return row_number
        row_number += 1
    raise RuntimeError('Could not find row for reportdate: ' + report_date.__str__())


# Virginia/DC/Maryland
# Virginia (case and death data from VDH.  Hospitalization data from Virginia Health and Hospital Association website/dashboard).
# Total cases: 590,625  (up 1,250 since previous day)
# 5.5% positive test rate (7 day PCR positive rate; down 0.2% since previous day)
# Deaths: 9,902 (up 53 since previous day)
# Hospitalizations:  Present 1,129 (down 7 since previous day) Discharges: Cumulative 48,804 (up 98 since previous day)


def get_virginia_text(sheet, row_number):


    text = 'Virginia/DC/Maryland\n'
    text += 'Virginia (case and death data from VDH. Hospitalization data from Virginia Health and Hospital Association website/dashboard).\n'

    total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_CASES_TOTAL_COLUMN] + str(row_number)
    total_cases_cell = sheet[total_cases_cell_str]
    total_cases_cell_formatted = format_integer(total_cases_cell.value)
    total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_CASES_CHANGE_PREVIOUS_DAY_COLUMN] + str(row_number)
    total_cases_change_since_previous_day_cell = sheet[total_cases_change_since_previous_day_cell_str]
    total_cases_change_since_previous_day_cell_formatted = format_integer(total_cases_change_since_previous_day_cell.value)

    text += 'Total cases: {} (up {} since previous day)\n'.format(total_cases_cell_formatted, total_cases_change_since_previous_day_cell_formatted)

    va_positive_test_rate_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_POSITIVE_TEST_RATE_COLUMN] + str(row_number)
    va_positive_test_rate_cell = sheet[va_positive_test_rate_cell_str]
    va_positive_test_rate_str_value = get_percent_string_value(va_positive_test_rate_cell.value)
    va_positive_test_rate_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_POSITIVE_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    va_positive_test_rate_change_since_previous_day_cell = sheet[va_positive_test_rate_change_since_previous_day_cell_str]
    va_positive_test_rate_change_since_previous_day_str_value = get_percent_string_value(va_positive_test_rate_change_since_previous_day_cell.value)
    va_positive_test_rate_change_since_previous_day_str_value = format_up_down(va_positive_test_rate_change_since_previous_day_str_value)
    text += '{} positive test rate (7 day PCR positive rate; {} since previous day)\n'.format(va_positive_test_rate_str_value, va_positive_test_rate_change_since_previous_day_str_value)

    # # Deaths: 9,902 (up 53 since previous day)
    va_deaths_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_DEATHS_TOTAL_COLUMN] + str(row_number)
    va_deaths_cell = sheet[va_deaths_cell_str]
    va_deaths_cell_formatted = format_integer(va_deaths_cell.value)
    va_death_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_DEATHS_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    va_death_change_since_previous_day_cell = sheet[va_death_change_since_previous_day_cell_str]
    text += 'Deaths: {} (up {} since previous day)\n'.format(va_deaths_cell_formatted, va_death_change_since_previous_day_cell.value)

    # # Hospitalizations:  Present 1,129 (down 7 since previous day) Discharges: Cumulative 48,804 (up 98 since previous day)

    va_hospitalizations_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CURRENT_COLUMN] + str(row_number)
    va_hospitalizations_cell = sheet[va_hospitalizations_cell_str]
    va_hospitalizations_cell_formatted = format_integer(va_hospitalizations_cell.value)
    va_hospitalizations_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    va_hospitalizations_change_since_previous_day_cell = sheet[va_hospitalizations_change_since_previous_day_cell_str]
    va_hospitalizations_change_since_previous_day_formatted = format_integer(va_hospitalizations_change_since_previous_day_cell.value)
    va_hospitalizations_change_since_previous_day_formatted = format_up_down(va_hospitalizations_change_since_previous_day_formatted)
    text += 'Hospitalizations: Present: {} ({} since previous day)\n '.format(va_hospitalizations_cell_formatted, va_hospitalizations_change_since_previous_day_formatted)

    # Excluding discharges
    # text += 'Discharges: Cumulative: {} (up {} since previous day).\n'.format(va_deaths_cell_formatted, va_death_change_since_previous_day_cell.value)
    return text

# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
def format_integer(value):
    return f'{value:,}'  # For Python ≥3.6


def format_up_down(str):
    if '-' in str:
        str = str.replace('-', '')
        return 'down ' + str
    else:
        return 'up ' + str

def get_percent_string_value(float_value):
    float_value = round(float_value, 3)
    float_value = float_value * 100
    return str(float_value) + '%'


def get_email_text_paragraphs_in_list(sheet, report_date):
    row_number = get_row_number_of_report_date(sheet, report_date)

    virginia_text = get_virginia_text(sheet, row_number)

    return [virginia_text]