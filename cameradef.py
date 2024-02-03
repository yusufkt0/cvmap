import cv2

vid = cv2.VideoCapture()
tvid = cv2.VideoCapture()

frame = cv2.imread

xlen = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
ylen = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

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

       tvid = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY_INV, 11, 2)