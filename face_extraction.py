# coding: utf-8

import cv2
import numpy as np
from subprocess import check_call

if __name__ == "__main__":

    # 内蔵カメラを起動
    cap = cv2.VideoCapture(0)

    # OpenCVに用意されている顔認識するためのxmlファイルのパス
    cascade_path = "/anaconda3/pkgs/opencv3-3.1.0-py35_0/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    # カスケード分類器の特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)

    # 顔に表示される枠の色を指定（白色）
    color = (255,255,255)

    while(True):

        # 内蔵カメラから読み込んだキャプチャデータを取得
        ret, frame = cap.read()
        height, width, channels = frame.shape[:3]
        frame_crop = np.zeros((height, width, channels), np.uint8)

        # モノクロで表示する
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 顔認識の実行
        facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10,10))
        # 顔が見つかったら顔を抽出して表示する
        if len(facerect) > 0:
            for rect in facerect:
                #顔部分を出力
                face_img = frame[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
                cv2.imshow("capture",face_img)
        else:
            print("no face")

        # qキーを押すとループ終了 実行画面がカレントウィンドウの時のみ
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or len(facerect) > 0 :
            break

    #PCに保存した後にS3に保存
    cv2.imwrite('./face_img/face.png', face_img)
    check_call(["python", "post_face_img.py", "./face_img/face.png", "face.png"])

    # 内蔵カメラを終了
    cap.release()
    cv2.destroyAllWindows()
