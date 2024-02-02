import cv2
import cameradef
import mapdef

vid = cv2.VideoCapture()
frame = cv2.imread

cameradef.getcam(0)

cv2.waitKey(0)
vid.release()
cv2.destroyAllWindows()
