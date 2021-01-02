import pandas as pd
import io
import requests

from constants import constant


# Global Cases,
# Global Deaths,
# US Cases, US Deaths
def get_csse_data(date):
    return

def get_csse_data(url: str):
    s = requests.get(url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))
    print(df.head())
    return

get_csse_data(constant.CSSE_GIT_HUB_URL)