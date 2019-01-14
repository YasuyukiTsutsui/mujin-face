import os
import cv2
import boto3
import tempfile


class Storage():
    def __init__(self, bucket_name):
        self.s3_bucket = boto3.resource('s3').Bucket(bucket_name)

    def uploading(self, img, extension='.png', upload_file_name=None):
        named_temporary_file = tempfile.NamedTemporaryFile()
        named_temporary_file_name = named_temporary_file.name + extension
        cv2.imwrite(named_temporary_file_name, img)
        if upload_file_name is None:
            upload_file_name = os.path.basename(named_temporary_file_name)
        self.s3_bucket.upload_file(named_temporary_file_name, upload_file_name)
