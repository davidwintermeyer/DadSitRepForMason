# Get the record of that report_date
# https://zetcode.com/python/openpyxl/
from constants import sitrep_column_constants
from constants.sitrep_column_constants import column_title_to_letter_dicts

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
def get_george_mason_text(sheet, row_number):

    text = '<b>George Mason</b>\n'
    text += '<p style="background-color: #75fa4b">'
    text += 'New cases since 1/25/2021.\n'

    total_student_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_TOTAL_STUDENT_CASES_COLUMN] + str(row_number)
    total_student_cases_cell = sheet[total_student_cases_cell_str]
    total_student_cases_cell_formatted = format_integer(total_student_cases_cell.value)
    total_student_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_TOTAL_STUDENT_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    total_student_cases_change_since_previous_day_cell = sheet[total_student_cases_change_since_previous_day_cell_str]
    total_student_cases_change_since_previous_day_cell_formatted = format_integer(total_student_cases_change_since_previous_day_cell.value)
    total_student_cases_change_since_previous_day_cell_formatted = format_up_down(total_student_cases_change_since_previous_day_cell_formatted)
    text += '{} student cases ({} since previous day)\n'.format(total_student_cases_cell_formatted, total_student_cases_change_since_previous_day_cell_formatted)

    res_student_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_RES_STUDENT_CASES_COLUMN] + str(row_number)
    res_student_cases_cell = sheet[res_student_cases_cell_str]
    res_student_cases_cell_formatted = format_integer(res_student_cases_cell.value)
    res_student_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_RES_STUDENT_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    res_student_cases_change_since_previous_day_cell = sheet[res_student_cases_change_since_previous_day_cell_str]
    res_student_cases_change_since_previous_day_cell_formatted = format_integer(res_student_cases_change_since_previous_day_cell.value)
    res_student_cases_change_since_previous_day_cell_formatted = format_up_down(res_student_cases_change_since_previous_day_cell_formatted)
    text += '{} residential student cases ({} since previous day)\n'.format(res_student_cases_cell_formatted, res_student_cases_change_since_previous_day_cell_formatted)

    non_res_student_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_NON_RES_STUDENT_CASES_COLUMN] + str(row_number)
    non_res_student_cases_cell = sheet[non_res_student_cases_cell_str]
    non_res_student_cases_cell_formatted = format_integer(non_res_student_cases_cell.value)
    non_res_student_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_NON_RES_STUDENT_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    non_res_student_cases_change_since_previous_day_cell = sheet[non_res_student_cases_change_since_previous_day_cell_str]
    non_res_student_cases_change_since_previous_day_cell_formatted = format_integer(non_res_student_cases_change_since_previous_day_cell.value)
    non_res_student_cases_change_since_previous_day_cell_formatted = format_up_down(non_res_student_cases_change_since_previous_day_cell_formatted)
    text += '{} non-residential student cases ({} since previous day)\n'.format(non_res_student_cases_cell_formatted, non_res_student_cases_change_since_previous_day_cell_formatted)

    employee_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_EMPLOYEE_CASES_COLUMN] + str(row_number)
    employee_cases_cell = sheet[employee_cases_cell_str]
    employee_cases_cell_formatted = format_integer(employee_cases_cell.value)
    employee_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_EMPLOYEE_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    employee_cases_change_since_previous_day_cell = sheet[employee_cases_change_since_previous_day_cell_str]
    employee_cases_change_since_previous_day_cell_formatted = format_integer(employee_cases_change_since_previous_day_cell.value)
    employee_cases_change_since_previous_day_cell_formatted = format_up_down(employee_cases_change_since_previous_day_cell_formatted)
    text += '{} employee cases ({} since previous day)\n'.format(employee_cases_cell_formatted, employee_cases_change_since_previous_day_cell_formatted)

    contractor_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_CONTRACTOR_CASES_COLUMN] + str(row_number)
    contractor_cases_cell = sheet[contractor_cases_cell_str]
    contractor_cases_cell_formatted = format_integer(contractor_cases_cell.value)
    contractor_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GMU_CONTRACTOR_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    contractor_cases_change_since_previous_day_cell = sheet[contractor_cases_change_since_previous_day_cell_str]
    contractor_cases_change_since_previous_day_cell_formatted = format_integer(contractor_cases_change_since_previous_day_cell.value)
    contractor_cases_change_since_previous_day_cell_formatted = format_up_down(contractor_cases_change_since_previous_day_cell_formatted)
    text += '{} contractor cases ({} since previous day)\n'.format(contractor_cases_cell_formatted, contractor_cases_change_since_previous_day_cell_formatted)
    text += '</p>'

    text += '\n'

    ### Active cases, I'm not updating the variable names, only the columns
    text += '<p style="background-color: #75fa4b">'
    active_total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ACTIVE_TOTAL_CASES_COLUMN] + str(row_number)
    active_total_cases_cell = sheet[active_total_cases_cell_str]
    active_total_cases_cell_formatted = format_integer(active_total_cases_cell.value)
    active_total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ACTIVE_TOTAL_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    active_total_cases_change_since_previous_day_cell = sheet[active_total_cases_change_since_previous_day_cell_str]
    active_total_cases_change_since_previous_day_cell_formatted = format_integer(active_total_cases_change_since_previous_day_cell.value)
    active_total_cases_change_since_previous_day_cell_formatted = format_up_down(active_total_cases_change_since_previous_day_cell_formatted)
    text += '{} active total cases ({} since previous day)\n'.format(active_total_cases_cell_formatted, active_total_cases_change_since_previous_day_cell_formatted)

    res_student_cases_cell_str = column_title_to_letter_dicts[
                                     sitrep_column_constants.ACTIVE_RES_STUDENT_CASES_COLUMN] + str(row_number)
    res_student_cases_cell = sheet[res_student_cases_cell_str]
    res_student_cases_cell_formatted = format_integer(res_student_cases_cell.value)
    res_student_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[
                                                               sitrep_column_constants.ACTIVE_RES_STUDENT_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(
        row_number)
    res_student_cases_change_since_previous_day_cell = sheet[res_student_cases_change_since_previous_day_cell_str]
    res_student_cases_change_since_previous_day_cell_formatted = format_integer(
        res_student_cases_change_since_previous_day_cell.value)
    res_student_cases_change_since_previous_day_cell_formatted = format_up_down(
        res_student_cases_change_since_previous_day_cell_formatted)
    text += '{} active residential student cases ({} since previous day)\n'.format(res_student_cases_cell_formatted,
                                                                            res_student_cases_change_since_previous_day_cell_formatted)

    non_res_student_cases_cell_str = column_title_to_letter_dicts[
                                         sitrep_column_constants.ACTIVE_NON_RES_STUDENT_CASES_COLUMN] + str(row_number)
    non_res_student_cases_cell = sheet[non_res_student_cases_cell_str]
    non_res_student_cases_cell_formatted = format_integer(non_res_student_cases_cell.value)
    non_res_student_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[
                                                                   sitrep_column_constants.ACTIVE_NON_RES_STUDENT_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(
        row_number)
    non_res_student_cases_change_since_previous_day_cell = sheet[
        non_res_student_cases_change_since_previous_day_cell_str]
    non_res_student_cases_change_since_previous_day_cell_formatted = format_integer(
        non_res_student_cases_change_since_previous_day_cell.value)
    non_res_student_cases_change_since_previous_day_cell_formatted = format_up_down(
        non_res_student_cases_change_since_previous_day_cell_formatted)
    text += '{} active non-residential student cases ({} since previous day)\n'.format(non_res_student_cases_cell_formatted,
                                                                                non_res_student_cases_change_since_previous_day_cell_formatted)

    employee_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ACTIVE_EMPLOYEE_CASES_COLUMN] + str(
        row_number)
    employee_cases_cell = sheet[employee_cases_cell_str]
    employee_cases_cell_formatted = format_integer(employee_cases_cell.value)
    employee_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[
                                                            sitrep_column_constants.ACTIVE_EMPLOYEE_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(
        row_number)
    employee_cases_change_since_previous_day_cell = sheet[employee_cases_change_since_previous_day_cell_str]
    employee_cases_change_since_previous_day_cell_formatted = format_integer(
        employee_cases_change_since_previous_day_cell.value)
    employee_cases_change_since_previous_day_cell_formatted = format_up_down(
        employee_cases_change_since_previous_day_cell_formatted)
    text += '{} active employee cases ({} since previous day)\n'.format(employee_cases_cell_formatted,
                                                                 employee_cases_change_since_previous_day_cell_formatted)

    contractor_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ACTIVE_CONTRACTOR_CASES_COLUMN] + str(
        row_number)
    contractor_cases_cell = sheet[contractor_cases_cell_str]
    contractor_cases_cell_formatted = format_integer(contractor_cases_cell.value)
    contractor_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[
                                                              sitrep_column_constants.ACTIVE_CONTRACTOR_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(
        row_number)
    contractor_cases_change_since_previous_day_cell = sheet[contractor_cases_change_since_previous_day_cell_str]
    contractor_cases_change_since_previous_day_cell_formatted = format_integer(
        contractor_cases_change_since_previous_day_cell.value)
    contractor_cases_change_since_previous_day_cell_formatted = format_up_down(
        contractor_cases_change_since_previous_day_cell_formatted)
    text += '{} active contractor cases ({} since previous day)\n'.format(contractor_cases_cell_formatted,
                                                                   contractor_cases_change_since_previous_day_cell_formatted)
    text += '</p>'

    ### Being lazy and not changing the variable names, just the column names
    text += '\n'
    text += '<p style="background-color: #75fa4b">'
    text += 'Residential students presently in Isolation or Quarantine on and off campus):\n'
    active_total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_ISOLATION_ON_CAMPUS] + str(row_number)
    active_total_cases_cell = sheet[active_total_cases_cell_str]
    active_total_cases_cell_formatted = format_integer(active_total_cases_cell.value)
    active_total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_ISOLATION_ON_CAMPUS_DELTA] + str(row_number)
    active_total_cases_change_since_previous_day_cell = sheet[active_total_cases_change_since_previous_day_cell_str]
    active_total_cases_change_since_previous_day_cell_formatted = format_integer(active_total_cases_change_since_previous_day_cell.value)
    active_total_cases_change_since_previous_day_cell_formatted = format_up_down(active_total_cases_change_since_previous_day_cell_formatted)
    text += '{} in isolation on campus ({} since previous day)\n'.format(active_total_cases_cell_formatted, active_total_cases_change_since_previous_day_cell_formatted)

    active_total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_ISOLATION_OFF_CAMPUS] + str(row_number)
    active_total_cases_cell = sheet[active_total_cases_cell_str]
    active_total_cases_cell_formatted = format_integer(active_total_cases_cell.value)
    active_total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_ISOLATION_OFF_CAMPUS_DELTA] + str(row_number)
    active_total_cases_change_since_previous_day_cell = sheet[active_total_cases_change_since_previous_day_cell_str]
    active_total_cases_change_since_previous_day_cell_formatted = format_integer(active_total_cases_change_since_previous_day_cell.value)
    active_total_cases_change_since_previous_day_cell_formatted = format_up_down(active_total_cases_change_since_previous_day_cell_formatted)
    text += '{} in isolation off campus ({} since previous day)\n'.format(active_total_cases_cell_formatted, active_total_cases_change_since_previous_day_cell_formatted)

    active_total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_QUARARNTINE_ON_CAMPUS] + str(row_number)
    active_total_cases_cell = sheet[active_total_cases_cell_str]
    active_total_cases_cell_formatted = format_integer(active_total_cases_cell.value)
    active_total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_QUARARNTINE_ON_CAMPUS_DELTA] + str(row_number)
    active_total_cases_change_since_previous_day_cell = sheet[active_total_cases_change_since_previous_day_cell_str]
    active_total_cases_change_since_previous_day_cell_formatted = format_integer(active_total_cases_change_since_previous_day_cell.value)
    active_total_cases_change_since_previous_day_cell_formatted = format_up_down(active_total_cases_change_since_previous_day_cell_formatted)
    text += '{} in quarantine on campus ({} since previous day)\n'.format(active_total_cases_cell_formatted, active_total_cases_change_since_previous_day_cell_formatted)

    active_total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_QUARARNTINE_OFF_CAMPUS] + str(row_number)
    active_total_cases_cell = sheet[active_total_cases_cell_str]
    active_total_cases_cell_formatted = format_integer(active_total_cases_cell.value)
    active_total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.RESIDENTIAL_QUARARNTINE_OFF_CAMPUS_DELTA] + str(row_number)
    active_total_cases_change_since_previous_day_cell = sheet[active_total_cases_change_since_previous_day_cell_str]
    active_total_cases_change_since_previous_day_cell_formatted = format_integer(active_total_cases_change_since_previous_day_cell.value)
    active_total_cases_change_since_previous_day_cell_formatted = format_up_down(active_total_cases_change_since_previous_day_cell_formatted)
    text += '{} in quarantine off campus ({} since previous day)\n'.format(active_total_cases_cell_formatted, active_total_cases_change_since_previous_day_cell_formatted)

    text += '</p>'
    return text

# Global:  118,031,918 cases/2,619,866 deaths
def get_global_text(sheet, row_number):
    cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GLOBAL_CASES_COLUMN] + str(row_number)
    cases_cell = sheet[cases_cell_str]
    cases_cell_formatted = format_integer(cases_cell.value)
    deaths_cell_str = column_title_to_letter_dicts[sitrep_column_constants.GLOBAL_DEATHS_COLUMN] + str(row_number)
    deaths_cell = sheet[deaths_cell_str]
    deaths_cell_formatted = format_integer(deaths_cell.value)
    text = 'Global: {} cases/{} deaths'.format(cases_cell_formatted, deaths_cell_formatted)
    return text

# US:   29,154,659 cases/529,263 deaths
def get_us_text(sheet, row_number):
    cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.US_CASES_COLUMN] + str(row_number)
    cases_cell = sheet[cases_cell_str]
    cases_cell_formatted = format_integer(cases_cell.value)
    deaths_cell_str = column_title_to_letter_dicts[sitrep_column_constants.US_DEATHS_COLUMN] + str(row_number)
    deaths_cell = sheet[deaths_cell_str]
    deaths_cell_formatted = format_integer(deaths_cell.value)
    text = 'US: {} cases/{} deaths'.format(cases_cell_formatted, deaths_cell_formatted)
    return text

def get_prince_william_county_text(sheet, row_number):
    text = '<b>Prince William County</b>\n'
    cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.PW_CASES_COLUMN] + str(row_number)
    cases_cell = sheet[cases_cell_str]
    cases_cell_formatted = format_integer(cases_cell.value)
    cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.PW_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    cases_change_since_previous_day_cell = sheet[cases_change_since_previous_day_cell_str]
    cases_change_since_previous_day_cell_formatted = format_integer(cases_change_since_previous_day_cell.value)
    cases_change_since_previous_day_cell_formatted = format_up_down(cases_change_since_previous_day_cell_formatted)

    text += '{} cases ({} since previous day)\n'.format(cases_cell_formatted, cases_change_since_previous_day_cell_formatted)

    positive_test_rate_cell_str = column_title_to_letter_dicts[sitrep_column_constants.PW_POSITIVE_TEST_RATE_COLUMN] + str(row_number)
    positive_test_rate_cell = sheet[positive_test_rate_cell_str]
    positive_test_rate_str_value = get_percent_string_value(positive_test_rate_cell.value)
    positive_test_rate_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.PW_POSITIVE_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    positive_test_rate_change_since_previous_day_cell = sheet[positive_test_rate_change_since_previous_day_cell_str]
    positive_test_rate_change_since_previous_day_str_value = get_percent_string_value(positive_test_rate_change_since_previous_day_cell.value)
    positive_test_rate_change_since_previous_day_str_value = format_up_down(positive_test_rate_change_since_previous_day_str_value)
    text += '{} positive test rate (7 day PCR positive rate; {} since previous day)\n'.format(positive_test_rate_str_value, positive_test_rate_change_since_previous_day_str_value)

    return text
# Arlington County
# 69,070 cases (up 138 since previous day)
# 5.5% positive test rate (7 day PCR positive test rate; down 0.1% since previous day)
def get_arlington_county_text(sheet, row_number):
    text = '<b>Arlington County</b>\n'
    cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ARLINGTON_CASES_COLUMN] + str(row_number)
    cases_cell = sheet[cases_cell_str]
    cases_cell_formatted = format_integer(cases_cell.value)
    cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ARLINGTON_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    cases_change_since_previous_day_cell = sheet[cases_change_since_previous_day_cell_str]
    cases_change_since_previous_day_cell_formatted = format_integer(cases_change_since_previous_day_cell.value)
    cases_change_since_previous_day_cell_formatted = format_up_down(cases_change_since_previous_day_cell_formatted)

    text += '{} cases ({} since previous day)\n'.format(cases_cell_formatted, cases_change_since_previous_day_cell_formatted)

    positive_test_rate_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ARLINGTON_POSITIVE_TEST_RATE_COLUMN] + str(row_number)
    positive_test_rate_cell = sheet[positive_test_rate_cell_str]
    positive_test_rate_str_value = get_percent_string_value(positive_test_rate_cell.value)
    positive_test_rate_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.ARLINGTON_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    positive_test_rate_change_since_previous_day_cell = sheet[positive_test_rate_change_since_previous_day_cell_str]
    positive_test_rate_change_since_previous_day_str_value = get_percent_string_value(positive_test_rate_change_since_previous_day_cell.value)
    positive_test_rate_change_since_previous_day_str_value = format_up_down(positive_test_rate_change_since_previous_day_str_value)
    text += '{} positive test rate (7 day PCR positive rate; {} since previous day)\n'.format(positive_test_rate_str_value, positive_test_rate_change_since_previous_day_str_value)

    return text

# Fairfax County
# 69,070 cases (up 138 since previous day)
# 5.5% positive test rate (7 day PCR positive test rate; down 0.1% since previous day)
def get_fairfax_county_text(sheet, row_number):
    text = '<b>Fairfax County</b>\n'
    cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.FAIRFAX_CASES_COLUMN] + str(row_number)
    cases_cell = sheet[cases_cell_str]
    cases_cell_formatted = format_integer(cases_cell.value)
    cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.FAIRFAX_CASES_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    cases_change_since_previous_day_cell = sheet[cases_change_since_previous_day_cell_str]
    cases_change_since_previous_day_cell_formatted = format_integer(cases_change_since_previous_day_cell.value)
    cases_change_since_previous_day_cell_formatted = format_up_down(cases_change_since_previous_day_cell_formatted)

    text += '{} cases ({} since previous day)\n'.format(cases_cell_formatted, cases_change_since_previous_day_cell_formatted)

    positive_test_rate_cell_str = column_title_to_letter_dicts[sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_COLUMN] + str(row_number)
    positive_test_rate_cell = sheet[positive_test_rate_cell_str]
    positive_test_rate_str_value = get_percent_string_value(positive_test_rate_cell.value)
    positive_test_rate_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_CHANGE_SINCE_PREVIOUS_DAY_COLUMN] + str(row_number)
    positive_test_rate_change_since_previous_day_cell = sheet[positive_test_rate_change_since_previous_day_cell_str]
    positive_test_rate_change_since_previous_day_str_value = get_percent_string_value(positive_test_rate_change_since_previous_day_cell.value)
    positive_test_rate_change_since_previous_day_str_value = format_up_down(positive_test_rate_change_since_previous_day_str_value)
    text += '{} positive test rate (7 day PCR positive rate; {} since previous day)\n'.format(positive_test_rate_str_value, positive_test_rate_change_since_previous_day_str_value)

    return text

# Virginia/DC/Maryland
# Virginia (case and death data from VDH.  Hospitalization data from Virginia Health and Hospital Association website/dashboard).
# Total cases: 590,625  (up 1,250 since previous day)
# 5.5% positive test rate (7 day PCR positive rate; down 0.2% since previous day)
# Deaths: 9,902 (up 53 since previous day)
# Hospitalizations:  Present 1,129 (down 7 since previous day) Discharges: Cumulative 48,804 (up 98 since previous day)

def get_virginia_text(sheet, row_number):

    text = '<b>Virginia/DC/Maryland</b>\n'
    text += 'Virginia (case and death data from VDH. Hospitalization data from Virginia Health and Hospital Association website/dashboard).\n'

    total_cases_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_CASES_TOTAL_COLUMN] + str(row_number)
    total_cases_cell = sheet[total_cases_cell_str]
    total_cases_cell_formatted = format_integer(total_cases_cell.value)
    total_cases_change_since_previous_day_cell_str = column_title_to_letter_dicts[sitrep_column_constants.VA_CASES_CHANGE_PREVIOUS_DAY_COLUMN] + str(row_number)
    total_cases_change_since_previous_day_cell = sheet[total_cases_change_since_previous_day_cell_str]
    total_cases_change_since_previous_day_cell_formatted = format_integer(total_cases_change_since_previous_day_cell.value)
    total_cases_change_since_previous_day_cell_formatted = format_up_down(total_cases_change_since_previous_day_cell_formatted)

    text += 'Total cases: {} ({} since previous day)\n'.format(total_cases_cell_formatted, total_cases_change_since_previous_day_cell_formatted)

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
    va_deaths_change_since_previous_day_formatted = format_integer(va_death_change_since_previous_day_cell.value)
    va_deaths_change_since_previous_day_formatted = format_up_down(va_deaths_change_since_previous_day_formatted)
    text += 'Deaths: {} ({} since previous day)\n'.format(va_deaths_cell_formatted, va_deaths_change_since_previous_day_formatted)

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
    try:
        int(str)
        if int(str) == 0:
            return 'no change '
    except ValueError:
        'ignoring this'

    if '-' in str:
        str = str.replace('-', '')
        return 'down ' + str
    else:
        return 'up ' + str

def get_percent_string_value(float_value):
    float_value = float_value * 100
    float_value = round(float_value, 1)
    return str(float_value) + '%'


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


def get_source_data_text():
    text = 'Virginia and health district data are pulled from the VDH website.  Virginia hospitalization data are from the VHHA website.  Mason data are from OMMT Metrics.  Global and US data are pulled from the Johns Hopkins statistical database.'
    text += "\n"
    text += 'Notable changes are highlighted in green.  Please note that not all pages under each CDC link that may be referenced have been updated.  Be sure to check when each particular page you are reading has been updated.'
    return text


def get_intro_text(report_date):
    text = 'COVID-19 Situation Report'
    text += "\n"
    text += 'Date:'
    text += "\n"
    text += 'Time:'

    return text

# appends all the paragraphs together
def append_sections(text_paragraphs_in_list):
    text = ''
    for paragraph in text_paragraphs_in_list:
        text += paragraph
    return text


def get_email_html(sheet, report_date):
    row_number = get_row_number_of_report_date(sheet, report_date)

    intro_text = get_intro_text(report_date)
    source_data_text = get_source_data_text()
    selected_references_text = '<p>Selected References:</p>'
    virginia_text = get_virginia_text(sheet, row_number)
    fairfax_county_text = get_fairfax_county_text(sheet, row_number)
    arlington_county_text = get_arlington_county_text(sheet, row_number)
    prince_william_county_text = get_prince_william_county_text(sheet, row_number)
    george_mason_text = get_george_mason_text(sheet, row_number)
    global_text = get_global_text(sheet, row_number)
    us_text = get_us_text(sheet, row_number)

    return append_sections([intro_text, source_data_text, selected_references_text, virginia_text, fairfax_county_text, arlington_county_text, prince_william_county_text, george_mason_text, global_text, us_text])

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
