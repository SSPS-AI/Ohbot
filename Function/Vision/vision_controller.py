import base64
import cv2
import matplotlib.image as mpimg
import eel

from Function.Vision.face_detection import FaceDetection
from Function.Vision.face_recognition import FaceRecognition

CAMERA_DIMS = (1920, 1080)
CAMERA_PORT = 1


class VisionController:
    def __init__(self):
        print("Initializing vision controller...")
        self.camera = cv2.VideoCapture(CAMERA_PORT)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_DIMS[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_DIMS[1])

        self.face_detection_pipeline = FaceDetection()
        self.face_recognition_pipeline = FaceRecognition()

        self.show_camera = False
        print("Vision controller initialized!")

    def get_frame(self, face_detections: bool = False, face_recognition: bool = False) -> tuple:
        success, image = self.camera.read()
        visualized_predictions = image.copy()
        faces, visualized_predictions = self.face_detection_pipeline.predict(image, visualized_predictions)
        faces, visualized_predictions = self.face_recognition_pipeline.predict_faces(faces, visualized_predictions)

        ret, jpeg = cv2.imencode('.jpg', visualized_predictions)
        return jpeg.tobytes()

    def gen(self):
        while self.show_camera:
            frame = self.get_frame()
            yield frame

    def show_camera_feed(self):
        self.show_camera = True
        y = self.gen()
        for each in y:
            blob = base64.b64encode(each)
            blob = blob.decode("utf-8")
            eel.showCameraFeed(blob)()
