import cv2
import numpy as np

class GestureRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def capture_frame(self):
        ret, frame = self.cap.read()
        return frame

    def detect_hand(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 20, 70])
        upper_skin = np.array([20, 255, 255])
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        return mask

    def recognize_gesture(self, mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w)/h
                if aspect_ratio > 2:
                    return "V Gesture"
                elif aspect_ratio < 0.5:
                    return "Fist Gesture"
                else:
                    return "Unknown Gesture"
        return "No Gesture"
