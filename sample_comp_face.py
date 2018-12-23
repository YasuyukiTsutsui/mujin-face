import sys, boto3

args = sys.argv

if __name__ == "__main__":
    face_img1 = args[1]
    face_img2 = args[2]
    bucket='pakuty-mujin-backet'

    client=boto3.client('rekognition','us-east-2')

    response = client.compare_faces(
        SourceImage ={'S3Object':{'Bucket':bucket,'Name':face_img1}},
        TargetImage ={'S3Object':{'Bucket':bucket,'Name':face_img2}},
        SimilarityThreshold = 70)

    print(response)
