import json


def report_generating_lambda_handler(event, context):
    print("report_generating_lambda_handler invoked with event: " + json.dumps(event))

