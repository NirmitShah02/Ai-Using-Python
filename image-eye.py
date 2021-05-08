import cv2
import numpy as np

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('sharuk.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, 1.03, 5)
for (ex,ey,ew,eh) in eyes:
   img = cv2.rectangle(img,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)
cv2.imwrite('Eye_AB.jpg',img)
