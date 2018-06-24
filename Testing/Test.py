import numpy as np
import cv2
import glob
import os
from CalibrationPattern import ChessBoard

_COLOR_IMAGES_STORE_PATH = "C:\\Users\\jalwana\\PycharmProjects\\CameraCalibration\\CapturedImages"
_PERFECT_CHECKER_BOARD = "C:\\Users\\jalwana\\PycharmProjects\\CameraCalibration\\Perfect CheckerBoard"

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

path = _COLOR_IMAGES_STORE_PATH
path = os.path.join(path, "*.jpg")
images = glob.glob(path)

rows = 7
cols = 9

numberOfUsefulImages = 1
for fname in images:
    print(fname)
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (rows,cols),flags=cv2.CALIB_CB_ADAPTIVE_THRESH)
    print(ret,corners)

    # If found, add object points, image points (after refining them)
    if ret:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        numberOfUsefulImages = numberOfUsefulImages + 1
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (rows,cols), corners2,ret)
        cv2.namedWindow(fname, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(fname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(fname, img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

print("numberOfUsefulImages:", numberOfUsefulImages)