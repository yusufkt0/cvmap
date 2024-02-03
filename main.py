import cv2
import cameradef as cam
import mapdef as map

frame = cv2.imread

cam.getcam(0)

cv2.waitKey(0)
cam.vid.release()
cv2.destroyAllWindows()
