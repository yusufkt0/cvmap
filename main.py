from math import e
import cv2
import mapdef as map

vid = cv2.VideoCapture()
gray = cv2.imread
frame = cv2.imread

xlen = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
ylen = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
th = cv2.imread()
#resize int istiyor
xlen = int (xlen)
ylen = int (ylen)

def getcam(index):
    vid = cv2.VideoCapture(index)

def thresh():
    while(vid.isOpened()):

       ret, frame = vid.read()
       frame = cv2.resize(frame, (xlen, ylen), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
       
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY_INV, 11, 2)

cv2.imshow("",th)

cv2.waitKey(0)
cam.vid.release()
cv2.destroyAllWindows()
