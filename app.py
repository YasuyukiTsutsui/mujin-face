import cv2
import tempfile

from src import FaceDetector, FaceRecognizer
from flask import Flask


CAMERA_PORT = 0
S3_BUCKET_NAME = 'pakuty-mujin-backet'
COLLECTION_ID = 'sample'
CASCADE_PATH = './src/haarcascades/haarcascade_frontalface_alt2.xml'

app = Flask(__name__)
face_detector = FaceDetector(CAMERA_PORT, CASCADE_PATH)
face_recognizer = FaceRecognizer(S3_BUCKET_NAME, COLLECTION_ID)

@app.route('/recognize')
def main():
    # 顔の検出と切り取り
    face_img = face_detector.detecting()

    # 一時ファイルとして保存
    named_temporary_file = tempfile.NamedTemporaryFile()
    extension = '.png'
    named_temporary_file_name = named_temporary_file.name + extension
    cv2.imwrite(named_temporary_file_name, face_img)

    # 顔を識別する
    recognize_response = face_recognizer.recognizing(named_temporary_file_name)

    # レスポンス作成
    print(recognize_response)

    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
