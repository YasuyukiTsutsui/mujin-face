import os
import cv2
import json
import tempfile

from src import FaceDetector, FaceRecognizer
from flask import Flask, Response, request, stream_with_context


CAMERA_PORT = 0
S3_BUCKET_NAME = 'pakuty-mujin-backet'
COLLECTION_ID = 'sample'
CASCADE_PATH = './src/haarcascades/haarcascade_frontalface_alt2.xml'
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

app = Flask(__name__)
face_detector = FaceDetector(CAMERA_PORT, CASCADE_PATH)
face_recognizer = FaceRecognizer(S3_BUCKET_NAME, COLLECTION_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

@app.route('/')
def main():
    # 顔の検出と切り取り
    def generate():
        # 顔が検出されるまで検出を続ける
        face_img = None
        while(True):
            face_img = face_detector.detecting()
            if face_img is not None:
                break

        # 一時ファイルとして保存
        named_temporary_file = tempfile.NamedTemporaryFile()
        extension = '.png'
        named_temporary_file_name = named_temporary_file.name + extension
        cv2.imwrite(named_temporary_file_name, face_img)

        # 顔を識別する
        recognize_response = face_recognizer.recognizing(named_temporary_file_name)

        # レスポンス作成
        yield json.dumps(recognize_response)
        yield '\n'

    return Response(stream_with_context(generate()), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
