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
CASCADE = "./src/haarcascades/haarcascade_frontalface_alt2.xml"

fd = FaceDetector(CAMERA_PORT, cascade_path=CASCADE)

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
            detected_face = fd.detecting()

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))

    def test_storage_update(self):
        self.s3_bucket = boto3.resource('s3').Bucket("pakuty-mujin-backet")
        self.s3_bucket.upload_file('./tests/test.txt', 'test.txt')
        self.s3_bucket.download_file('test.txt', './tests/test_a.txt')
        self.assertEqual(open('./tests/test.txt').read(),open('./tests/test_a.txt').read())
