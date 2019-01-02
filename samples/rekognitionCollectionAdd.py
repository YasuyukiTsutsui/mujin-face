
import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    collectionId = 'sample'

    client=boto3.client('rekognition','us-east-2')

    response = client.index_faces(CollectionId = collectionId,
                                  Image = {'S3Object':{'Bucket':bucket, 'Name':key}},
                                  ExternalImageId = key.strip("RegistImage/"),
                                  DetectionAttributes = ['ALL'])
