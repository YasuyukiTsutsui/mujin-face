import unittest
import numpy as np
import cv2
import boto3

from src import FaceDetector
from src import FaceRecognizer
from src import Storage

CAMERA_PORT = 0
fd = FaceDetector(CAMERA_PORT)

class FaceClassTest(unittest.TestCase):
    # 0行列(顔なし)から顔検出をして
    def test_detecting_from_zeros_ndarray(self):
        image_frame = np.zeros([255, 255], dtype='uint8')
        detected_face = fd.detecting(image_frame)
        self.assertEqual(detected_face, None)

    def test_detecting_capture_face(self):
        detected_face = fd.detecting(cv2.imread('./tests/Nakata.jpg'))
        self.assertTrue((detected_face == cv2.imread('./tests/detect.jpg')).all)
