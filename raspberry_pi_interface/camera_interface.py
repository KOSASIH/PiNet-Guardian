import cv2

class CameraInterface:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def capture_image(self):
        ret, frame = self.camera.read()
        return frame

    def release_camera(self):
        self.camera.release()
