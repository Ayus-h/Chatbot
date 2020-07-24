import cv2
import numpy as np


web_cam = cv2.VideoCapture(0)

while True:
    ret,frame = web_cam.read()

    cv2.imshow("frame", frame)

