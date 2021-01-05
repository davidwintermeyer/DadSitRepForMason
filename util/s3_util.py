# https://stackoverflow.com/questions/58179449/how-to-load-a-template-file-from-amazon-s3-and-load-it-into-openpyxl-workbook
from openpyxl import load_workbook
from tempfile import NamedTemporaryFile
import boto3
import botocore

s3 = boto3.resource('s3')

def download_file(bucket, key):
    try:
        file = NamedTemporaryFile(suffix = '.xlsx', delete=False)
        s3.Bucket(bucket).download_file(key, file.name)
        return file.name
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return None
        else:
            raise

def upload_workbook(workbook, bucket, key):
    with NamedTemporaryFile() as tmp:
        workbook.save(tmp.name)
        tmp.seek(0)
        s3.meta.client.upload_file(tmp.name, bucket, key)