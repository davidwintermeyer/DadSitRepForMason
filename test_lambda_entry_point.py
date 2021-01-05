import os

from lambda_entry_point import lambda_handler

os.environ["DEBUSSY"] = "1"
os.environ["DEBUSSY"] = "1"

lambda_handler(None, None)
