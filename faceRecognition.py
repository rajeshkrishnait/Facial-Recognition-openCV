import cv2
import numpy as np
import face_recognition
#load on image first
import cv2
from random import randrange
#press q to quit webcam
imgRajesh=face_recognition.load_image_file('images/reg3.jpg')

imgRajesh=cv2.cvtColor(imgRajesh,cv2.COLOR_BGR2RGB)
# faceloc=face_recognition.face_locations(imgRajesh)[0]
# print(faceloc)
encodeRajes=face_recognition.face_encodings(imgRajesh)[0]
# print(encodeRajes)
# cv2.rectangle(imgRajesh,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),4)
webcam=cv2.VideoCapture(0)
while True:
    successful_frame_read, frame=webcam.read()
    cv2.imshow("f",frame)
    cv2.waitKey(10)

    # faceloc=face_recognition.face_locations(frame)
    # print(faceloc)
    # cv2.rectangle(frame,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),4)
    # cv2.imshow("f",frame)
    encodeFrame=face_recognition.face_encodings(frame)
    if len(encodeFrame)==0:
        print("get to better lighting dumbass")
    else:
        results=face_recognition.compare_faces([encodeRajes],encodeFrame[0])
    # cv2.imshow("f",frame)
        print(results)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()
print("Code Completed")