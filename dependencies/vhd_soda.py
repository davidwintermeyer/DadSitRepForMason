import datetime
import traceback

import pandas as pd
from sodapy import Socrata

from constants import sitrep_column_constants, vdh_constants
from constants.vdh_constants import VDH_KEY_MEASURES_HOSPITALS_TOTAL_COVID_PATIENTS_DATA_COLUMN
from util.date_util import get_date_string


########## Cases data ###########
# Passing Socrata client as a param
def get_vdh_cases_data(today_date: datetime.date, client: Socrata) -> dict:

    try:
        cases_data_dict = {}

        # constant.VA_CASES_TOTAL_COLUMN
        # constant.VA_DEATHS_TOTAL_COLUMN
        # {'report_date': '2021-01-01T00:00:00.000', 'fips': '51001', 'locality': 'Accomack', 'vdh_health_district': 'Eastern Shore', 'total_cases': '1709', 'hospitalizations': '124', 'deaths': '27'}
        cases_query_string = "report_date = '" + str(today_date) + "'"
        ## "report_date = '2021-01-01T00:00:00.000'"
        cases_data = client.get(vdh_constants.VDH_CASES_DATA_ENDPOINT, where=cases_query_string)

        # Sanity check that cases data size is 133
        # TODO: Make this not fail everything
        if vdh_constants.VDH_NUM_LOCALITIES != len(cases_data):
            cases_localities_error_message = 'Cases data should have ' + str(
                vdh_constants.VDH_NUM_LOCALITIES) + ' localities, found ' + str(len(cases_data)) + ' for date: ' + str(today_date)
            raise Exception(cases_localities_error_message)

        cases_df = pd.DataFrame.from_records(cases_data)

        # make total_cases and deaths numbers
        # https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
        cases_df[[vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN,
                  vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN,
                  vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN]] = \
            cases_df[[vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN,
                      vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN,
                      vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN]].apply(pd.to_numeric)

        cases_data_dict[sitrep_column_constants.VA_CASES_TOTAL_COLUMN] = cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.VA_DEATHS_TOTAL_COLUMN] = cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

        # fairfax
        fairfax_cases_df = cases_df[cases_df[
                                        vdh_constants.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.FAIRFAX]
        cases_data_dict[sitrep_column_constants.FAIRFAX_CASES_COLUMN] = fairfax_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.FAIRFAX_HOSPITALIZATIONS_COLUMN] = fairfax_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.FAIRFAX_DEATHS_COLUMN] = fairfax_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

        # arlington
        arlington_cases_df = cases_df[cases_df[vdh_constants.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.ARLINGTON]
        cases_data_dict[sitrep_column_constants.ARLINGTON_CASES_COLUMN] = arlington_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.ARLINGTON_HOSPITALIZATIONS_COLUMN] = arlington_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.ARLINGTON_DEATHS_COLUMN] = arlington_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

        # pw
        pw_cases_df = cases_df[cases_df[vdh_constants.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.PW]
        cases_data_dict[sitrep_column_constants.PW_CASES_COLUMN] = pw_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.PW_HOSPITALIZATIONS_COLUMN] = pw_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
        cases_data_dict[sitrep_column_constants.PW_DEATHS_COLUMN] = pw_cases_df[
            vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

        return cases_data_dict
    except Exception as exc:
        raise RuntimeError('Failed to get VDH Cases Data') from exc

########## Positive Test Rate Data ###########

# Looking at the metadata for the data
#     metadata = client.get_metadata(vdh_constants.VDH_TESTING_BY_LAB_REPORT_DATA_ENDPOINT)
# lab_report_date datatype is text
# with format 1/26/2020
# We want the last seven days worth of data
# single day: "lab_report_date = '1/3/2021'"
# No zero padding
# https://www.programiz.com/python-programming/datetime/strftime
# If windows, '%#m/%#d/%Y'
# lab_report_query_string = "lab_report_date = '" + today_date.strftime('%-m/%-d/%Y') + "'"
def get_lab_report_query_string(today_date):

    day_strings = []
    counter = 0
    while counter < vdh_constants.NUMBER_OF_DAYS_TO_INCLUDE_IN_TESTING_DATA:
        date = today_date - datetime.timedelta(days=counter)
        # For windows, needs the # rather than the -
        # day_strings.append("'" + date.strftime('%#m/%#d/%Y') + "'")
        date_formatting_str = get_date_string()
        day_strings.append("'" + date.strftime(date_formatting_str) + "'")

        counter = counter + 1

    return "lab_report_date IN (" + ",".join(day_strings) + ")"

def get_vdh_testing_data(today_date: datetime.date, client: Socrata) -> dict:

    try:
        testing_data_dict = {}

        lab_report_query_string = get_lab_report_query_string(today_date)
        lab_report_data = client.get(vdh_constants.VDH_TESTING_BY_LAB_REPORT_DATA_ENDPOINT, where=lab_report_query_string)
        lab_report_df = pd.DataFrame.from_records(lab_report_data)

        lab_report_df[[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_PCR_TESTING_DATA_COLUMN,
                  vdh_constants.VDH_LAB_REPORT_NUMBER_OF_POSITIVE_PCR_TESTING_DATA_COLUMN]] = \
            lab_report_df[[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_PCR_TESTING_DATA_COLUMN,
                      vdh_constants.VDH_LAB_REPORT_NUMBER_OF_POSITIVE_PCR_TESTING_DATA_COLUMN]].apply(pd.to_numeric)

        va_number_of_pcr_tests = lab_report_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_PCR_TESTING_DATA_COLUMN].sum()
        va_number_of_positive_pcs_tests = lab_report_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_POSITIVE_PCR_TESTING_DATA_COLUMN].sum()

        testing_data_dict[sitrep_column_constants.VA_POSITIVE_TEST_RATE_COLUMN] = va_number_of_positive_pcs_tests / va_number_of_pcr_tests

        # Fairfax
        fairfax_test_results_df = lab_report_df[lab_report_df[vdh_constants.VDH_LAB_REPORT_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.FAIRFAX]
        fairfax_number_of_pcr_tests = fairfax_test_results_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_PCR_TESTING_DATA_COLUMN].sum()
        fairfax_number_of_positive_pcs_tests = fairfax_test_results_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_POSITIVE_PCR_TESTING_DATA_COLUMN].sum()
        testing_data_dict[sitrep_column_constants.FAIRFAX_POSITIVE_TEST_RATE_COLUMN] = fairfax_number_of_positive_pcs_tests / fairfax_number_of_pcr_tests

        # Arlington
        arlington_test_results_df = lab_report_df[lab_report_df[vdh_constants.VDH_LAB_REPORT_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.ARLINGTON]
        arlington_number_of_pcr_tests = arlington_test_results_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_PCR_TESTING_DATA_COLUMN].sum()
        arlington_number_of_positive_pcs_tests = arlington_test_results_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_POSITIVE_PCR_TESTING_DATA_COLUMN].sum()
        testing_data_dict[sitrep_column_constants.ARLINGTON_POSITIVE_TEST_RATE_COLUMN] = arlington_number_of_positive_pcs_tests / arlington_number_of_pcr_tests

        # PW
        pw_test_results_df = lab_report_df[lab_report_df[vdh_constants.VDH_LAB_REPORT_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.PW]
        pw_number_of_pcr_tests = pw_test_results_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_PCR_TESTING_DATA_COLUMN].sum()
        pw_number_of_positive_pcs_tests = pw_test_results_df[vdh_constants.VDH_LAB_REPORT_NUMBER_OF_POSITIVE_PCR_TESTING_DATA_COLUMN].sum()
        testing_data_dict[sitrep_column_constants.PW_POSITIVE_TEST_RATE_COLUMN] = pw_number_of_positive_pcs_tests / pw_number_of_pcr_tests

        return testing_data_dict
    except Exception as exc:
        raise RuntimeError('Failed to get VDH Testing Data') from exc

def get_vdh_current_hospitalization_data(today_date: datetime.date, client: Socrata) -> dict:
    try:
        hospitalizations_data_dict = {}

        hospitalizations_query_string = "date = '" + str(today_date) + "'"

        hospitalizations_data = client.get(vdh_constants.VDH_KEY_MEASURES_HOSPITALS_DATA_ENDPOINT, where=hospitalizations_query_string)
        hospitalizations_data_dict[sitrep_column_constants.VA_PRESENT_HOSPITALIZATIONS_CURRENT_COLUMN] = int(hospitalizations_data[0][VDH_KEY_MEASURES_HOSPITALS_TOTAL_COVID_PATIENTS_DATA_COLUMN])

        return hospitalizations_data_dict
    except Exception as exc:
        raise RuntimeError('Failed to get VDH Current Hospitalization Data') from exc

def get_vdh_data(today_date: datetime.date) -> dict:

    print("running get_vdh_data")
    try:
        client = Socrata(vdh_constants.VDH_DATA_URL, vdh_constants.VDH_APP_TOKEN)

        result = {}

        vdh_cases_data = get_vdh_cases_data(today_date, client)
        result.update(vdh_cases_data)

        # Per Email Feb 2021, I won't populate the test values, but leave the columns in for dad to populate
        # vdh_testing_data = get_vdh_testing_data(today_date, client)
        # result.update(vdh_testing_data)

        vdh_hospitalization_data = get_vdh_current_hospitalization_data(today_date, client)
        result.update(vdh_hospitalization_data)

        return result
    except:
        traceback.print_exc()