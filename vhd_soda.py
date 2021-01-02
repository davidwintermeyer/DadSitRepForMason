import pandas as pd

from datetime import datetime, date, timedelta
from sodapy import Socrata

import constant

# Method signature that returns a dict
def get_vdh_data(today_date: date) -> dict:
    client = Socrata(constant.VDH_DATA_URL, constant.VDH_APP_TOKEN)

    result = {}

    # Cases data
    # constant.VA_CASES_TOTAL_COLUMN
    # constant.VA_DEATHS_TOTAL_COLUMN
    # {'report_date': '2021-01-01T00:00:00.000', 'fips': '51001', 'locality': 'Accomack', 'vdh_health_district': 'Eastern Shore', 'total_cases': '1709', 'hospitalizations': '124', 'deaths': '27'}
    query_string = "report_date = '" + str(today_date) + "'"
    ## "report_date = '2021-01-01T00:00:00.000'"
    cases_data = client.get(constant.VDH_CASES_DATA_ENDPOINT, where=query_string)

    # Sanity check that cases data size is 133
    # TODO: Make this not fail everything
    if constant.VDH_NUM_LOCALITIES != len(cases_data):
        cases_localities_error_message = 'Cases data should have ' + str(constant.VDH_NUM_LOCALITIES) + ' localities, found ' + str(len(cases_data)) + ' for date: ' + str(today_date)
        raise Exception(cases_localities_error_message)

    cases_df = pd.DataFrame.from_records(cases_data)

    # make total_cases and deaths numbers
    # https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
    cases_df[[constant.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN, constant.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN, constant.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN]] = \
        cases_df[[constant.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN, constant.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN, constant.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN]].apply(pd.to_numeric)

    result[constant.VA_CASES_TOTAL_COLUMN] = cases_df[constant.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[constant.VA_DEATHS_TOTAL_COLUMN] = cases_df[constant.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    # fairfax
    fairfax_cases_df = cases_df[cases_df[constant.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == constant.FAIRFAX]
    result[constant.FAIRFAX_CASES_COLUMN] = fairfax_cases_df[constant.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[constant.FAIRFAX_HOSPITALIZATIONS_COLUMN] = fairfax_cases_df[constant.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
    result[constant.FAIRFAX_DEATHS_COLUMN] = fairfax_cases_df[constant.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    # arlington
    arlington_cases_df = cases_df[cases_df[constant.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == constant.ARLINGTON]
    result[constant.ARLINGTON_CASES_COLUMN] = arlington_cases_df[constant.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[constant.ARLINGTON_HOSPITALIZATIONS_COLUMN] = arlington_cases_df[constant.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
    result[constant.ARLINGTON_DEATHS_COLUMN] = arlington_cases_df[constant.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    pw_cases_df = cases_df[cases_df[constant.VDH_CASES_HEALTH_DISTRICT_DATA_COLUMN] == constant.PW]
    result[constant.PW_CASES_COLUMN] = pw_cases_df[constant.VDH_CASES_DATA_FRAME_TOTAL_CASES_DATA_COLUMN].sum()
    result[constant.PW_HOSPITALIZATIONS_COLUMN] = pw_cases_df[constant.VDH_CASES_DATA_FRAME_HOSPITALIZATIONS_DATA_COLUMN].sum()
    result[constant.PW_DEATHS_COLUMN] = pw_cases_df[constant.VDH_CASES_DATA_FRAME_DEATHS_DATA_COLUMN].sum()

    return result

# 'Could not parse SoQL query "select * where report_date LIKE 2021-01-01T00:00:00.000" at line 1 character 43'
# 'Could not parse SoQL query "select * where report_date = 2021-01-01T00:00:00.000" at line 1 character 40'

today_date = datetime.utcnow().date()
get_vdh_data(today_date - timedelta(days=5))
