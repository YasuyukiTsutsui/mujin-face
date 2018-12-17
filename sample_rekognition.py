import sys, boto3

args = sys.argv

if __name__ == "__main__":
    fileName=args[1]
    bucket='pakuty-mujin-backet'

    client=boto3.client('rekognition','us-east-2')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

    print('Detected labels for ' + fileName)
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
