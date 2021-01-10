import datetime
import pytz

# Event looks like
# lambda_handler invoked with event:
# {
#     "version": "0",
#     "id": "c269fbe0-0982-4073-0f95-889603cee181",
#     "detail-type": "Scheduled Event",
#     "source": "aws.events",
#     "account": "343806292018",
#     "time": "2021-01-06T22:00:00Z",
#     "region": "us-east-1",
#     "resources": [
#         "arn:aws:events:us-east-1:343806292018:rule/DailyAt5pmEastern"
#     ],
#     "detail": {}
# }
def get_report_date_time(event: dict) -> datetime:
    date_time_str_utc = event['time']
    unaware_date_time_obj = datetime.datetime.strptime(date_time_str_utc, '%Y-%m-%dT%H:%M:%SZ')
    now_aware_date_time_obj = unaware_date_time_obj.replace(tzinfo=pytz.UTC)

    timezone = pytz.timezone('America/New_York')
    est_date_time_obj = now_aware_date_time_obj.astimezone(timezone)

    print(est_date_time_obj)
    return est_date_time_obj
