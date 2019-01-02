import boto3
import sys
import json

args = sys.argv

if __name__ == "__main__":
    bucket = 'pakuty-mujin-backet'
    collectionId = 'sample'
    face_img = args[1]

    f = open(face_img, "rb")
    face_img_byte = bytearray(f.read())
    collectionId = 'sample'

    client=boto3.client('rekognition','us-east-2')

    response = client.search_faces_by_image(CollectionId = collectionId,
                                            FaceMatchThreshold = 80,
                                            Image = {'Bytes':face_img_byte},
                                            MaxFaces = 1)
    print(response)
