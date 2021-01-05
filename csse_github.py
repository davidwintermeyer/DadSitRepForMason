from datetime import date
import pandas as pd
import io
import requests

from constants import csse_data_constants, sitrep_column_constants
from util.date_util import get_days_ago


def get_csse_data_url(report_date: date) -> str:
    date_str = report_date.strftime('%m-%d-%Y')
    return csse_data_constants.CSSE_GIT_HUB_BASE_URL + date_str + csse_data_constants.CSV_EXTENSION


# Global Cases,
# Global Deaths,
# US Cases, US Deaths
def get_csse_data(report_date: date) -> dict:
    # Because csse data is published at midnight est and we run this at 5pm est, we have to use previous day
    csse_report_date = get_days_ago(report_date, 1)

    url = get_csse_data_url(csse_report_date)
    csse_content = requests.get(url).content
    csse_df = pd.read_csv(io.StringIO(csse_content.decode('utf-8')))

    csse_data_dict = {}

    csse_data_dict[sitrep_column_constants.GLOBAL_CASES_COLUMN] = csse_df[csse_data_constants.CONFIRMED_DATA_COLUMN].sum()
    csse_data_dict[sitrep_column_constants.GLOBAL_DEATHS_COLUMN] = csse_df[csse_data_constants.DEATHS_DATA_COLUMN].sum()

    us_csse_data_df = csse_df[csse_df[csse_data_constants.COUNTRY_REGION_DATA_COLUMN] == csse_data_constants.US_COUNTRY_REGION]
    csse_data_dict[sitrep_column_constants.US_CASES_COLUMN] = us_csse_data_df[csse_data_constants.CONFIRMED_DATA_COLUMN].sum()
    csse_data_dict[sitrep_column_constants.US_DEATHS_COLUMN] = us_csse_data_df[csse_data_constants.DEATHS_DATA_COLUMN].sum()

    return csse_data_dict