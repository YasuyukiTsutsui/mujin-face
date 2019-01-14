import cv2
import numpy as np

class FaceDetector():
    def __init__(self, camera_port, cascade_path="./haarcascades/haarcascade_frontalface_alt2.xml"):
        self.capture = cv2.VideoCapture(camera_port)
        self.cascade = cv2.CascadeClassifier(cascade_path)

    def detecting(self, frame=None):
        if frame is None:
            _, frame = self.capture.read()
            height, width, channels = frame.shape[:3]
            frame_crop = np.zeros((height, width, channels), np.uint8)

        # 顔検出
        faces = self.cascade.detectMultiScale(frame)

        # 顔がなかった場合
        if len(faces) ==  0:
            print('no face')
            return None

        # 大きく写っている顔のみを抽出

        # 顔の縦横のサイズの合計がもっとも大きい顔を
        # 大きく写っている顔とする
        max_face_size = -1
        max_size_face_id = -1
        for i, face in enumerate(faces):
            # 顔の縦横のサイズを算出
            face_size = face[2]+face[3]
            if max_face_size < face_size:
                max_face_size = face_size
                max_size_face_id = i

        # 大きく写っている顔を切り取る
        face = faces[max_size_face_id]
        face_img = frame[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
        return face_img
