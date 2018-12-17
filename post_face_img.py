import sys
import json
import boto3

args = sys.argv

bucket_name = "pakuty-mujin-backet"
s3 = boto3.resource('s3')
originl_img = args[1]
upload_img = args[2]

s3.Bucket(bucket_name).upload_file(originl_img, upload_img)
