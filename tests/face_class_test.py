import cv2
import unittest
import numpy as np
import cv2
import boto3

from contextlib import contextmanager
from src import FaceDetector
from src import FaceRecognizer
from src import Storage

CAMERA_PORT = 0
<<<<<<< HEAD
fd = FaceDetector(CAMERA_PORT)
=======
CASCADE = "./src/haarcascades/haarcascade_frontalface_alt2.xml"

face_detector = FaceDetector(CAMERA_PORT, cascade_path=CASCADE)
>>>>>>> db6c8116d6ceca1707105ec2fd530741b7c92ac3

class FaceClassTest(unittest.TestCase):
    # 0行列(顔なし)から顔検出をして
    def test_detecting_from_zeros_ndarray(self):
        image_frame = np.zeros([255, 255], dtype='uint8')
        detected_face = fd.detecting(image_frame)
        self.assertEqual(detected_face, None)

    def test_detecting_capture_face(self):
        detected_face = fd.detecting(cv2.imread('./tests/Nakata.jpg'))
        self.assertTrue((detected_face == cv2.imread('./tests/detect.jpg')).all)

    def test_capturing(self):
        with self.assertNotRaises(cv2.error):
            detected_face = face_detector.detecting()

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))
