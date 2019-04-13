#-------------------------------------------------------------------------------
#-                      Kuphaneler 
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
#-                     Nothing Fonksiyonu Mutlaka Olmali  
#------------------------------------------------------------------------------
def nothing(x):
    pass
#-------------------------------------------------------------------------------
#-                      TrackBar Tanimlmalari  
#------------------------------------------------------------------------------
def CreateTrackBar_Init():
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("Lower - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("Lower - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Lower - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Upper - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("Upper - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("Upper - V", "Trackbars", 255, 255, nothing)
    
CreateTrackBar_Init()
cap =cv2.VideoCapture('Video.MKV')
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (720, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    Lower_H_Value = cv2.getTrackbarPos("Lower - H", "Trackbars")
    Lower_S_Value = cv2.getTrackbarPos("Lower - S", "Trackbars")
    Lower_V_Value = cv2.getTrackbarPos("Lower - V", "Trackbars")
    Upper_H_Value = cv2.getTrackbarPos("Upper - H", "Trackbars")
    Upper_S_Value = cv2.getTrackbarPos("Upper - S", "Trackbars")
    Upper_V_Value = cv2.getTrackbarPos("Upper - V", "Trackbars")
#-------------------------------------------------------------------------------
#-                      Standart Maskeleme Islemleri  
#-------------------------------------------------------------------------------
    lower_blue = np.array([Lower_H_Value,Lower_S_Value,Lower_V_Value])
    upper_blue = np.array([Upper_H_Value,Upper_S_Value,Upper_V_Value])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
