import pandas as pd

from datetime import datetime, date, timedelta
from sodapy import Socrata

import constants.vdh_constants
from constants import constant, sitrep_column_constants, vdh_constants


# Method signature that returns a dict
def get_vdh_data(today_date: date) -> dict:
    client = Socrata(vdh_constants.VDH_DATA_URL, vdh_constants.VDH_APP_TOKEN)

    result = {}

    ########## Cases data ###########
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

    result[sitrep_column_constants.VA_CASES_TOTAL_COLUMN] = cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[sitrep_column_constants.VA_DEATHS_TOTAL_COLUMN] = cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    # fairfax
    fairfax_cases_df = cases_df[cases_df[
                                    vdh_constants.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.FAIRFAX]
    result[sitrep_column_constants.FAIRFAX_CASES_COLUMN] = fairfax_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[sitrep_column_constants.FAIRFAX_HOSPITALIZATIONS_COLUMN] = fairfax_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
    result[sitrep_column_constants.FAIRFAX_DEATHS_COLUMN] = fairfax_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    # arlington
    arlington_cases_df = cases_df[cases_df[vdh_constants.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.ARLINGTON]
    result[sitrep_column_constants.ARLINGTON_CASES_COLUMN] = arlington_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[sitrep_column_constants.ARLINGTON_HOSPITALIZATIONS_COLUMN] = arlington_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
    result[sitrep_column_constants.ARLINGTON_DEATHS_COLUMN] = arlington_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    pw_cases_df = cases_df[cases_df[vdh_constants.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == vdh_constants.PW]
    result[sitrep_column_constants.PW_CASES_COLUMN] = pw_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[sitrep_column_constants.PW_HOSPITALIZATIONS_COLUMN] = pw_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
    result[sitrep_column_constants.PW_DEATHS_COLUMN] = pw_cases_df[
        vdh_constants.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()


    ########## Positive Test Rate Data ###########
    # Looking at the metadata for the data
    #     metadata = client.get_metadata(vdh_constants.VDH_TESTING_BY_LAB_REPORT_DATA_ENDPOINT)
    # labe_report_date datatype is text
    # with format 1/26/2020

    lab_report_query_string = "lab_report_date = '" + str(today_date) + "'"
    lab_report_data = client.get(vdh_constants.VDH_TESTING_BY_LAB_REPORT_DATA_ENDPOINT, where=lab_report_query_string)
    lab_report_df = pd.DataFrame.from_records(lab_report_data)

    return result
