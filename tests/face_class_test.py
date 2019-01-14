import unittest
import numpy as np

from src import FaceDetector

CAMERA_PORT = 0
face_detector = FaceDetector(CAMERA_PORT)

class FaceClassTest(unittest.TestCase):
    # 0行列(顔なし)から顔検出をして
    def test_detecting_from_zeros_ndarray(self):
        image_frame = np.zeros([255, 255], dtype='uint8')
        detected_face = face_detector.detecting(image_frame)
        self.assertEqual(detected_face, None)
