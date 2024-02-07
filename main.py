from math import e
import cv2
import cameradef as cam
import mapdef as map

frame = cv2.imread

cam.getcam(0)
cam.thresh()
cv2.imshow("",cam.gray)

cv2.waitKey(0)
cam.vid.release()
cv2.destroyAllWindows()
