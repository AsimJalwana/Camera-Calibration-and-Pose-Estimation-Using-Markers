# from __future__ import print_function
# from CalibrationPattern import ArucoMarker
# from Camera import KinectDevice
# from Camera import CameraParams
# import matlab.engine
# import numpy as np
# import itertools
#
# # device = DummyDevice.DummyDevice()
# matlabEngine = matlab.engine.start_matlab()
#
# device = KinectDevice.Kinect();
# counter = 0
# dict = None
#
# while(True):
#     colorFrame = device.getColorFrame()
#     counter = counter + 1
#     if colorFrame is None or counter > 10:
#         break
#
#     arucoMarker = ArucoMarker.ArucoMarker(RGB=colorFrame)
#     arucoMarker.showGray()
#     cParams = CameraParams.CameraParams.loadCameraParameters('CameraParams_31-05-2018--232958.pkl')
#     rvec, tvec = arucoMarker.findPoseOfPattern(cParams)
#
#     rvec = list(itertools.chain(*rvec))
#     tvec = list(itertools.chain(*tvec))
#
#     print("RVec", rvec)
#     print("TVec", tvec)
#
#     if rvec is None or tvec is None:
#         counter = counter - 1
#         continue
#
#     dict = cParams.saveParamsAsMat("Test.mat",rotationalVector = np.transpose(rvec), translationVector = np.transpose(tvec), dict=dict)
#     print(matlabEngine.displayCameranCheckerBoard(nargout=0))
#
# matlabEngine.quit()
#







import os
import cv2
from cv2 import aruco
import numpy as np

aruco_dict = aruco.Dictionary_get( aruco.DICT_6X6_1000 )
img = aruco.drawMarker(aruco_dict, 2, 50)
cv2.imwrite("test_marker_50.jpg", img)

# img = cv2.imread('ArucoImageRGB1.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('frame',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# parameters = aruco.DetectorParameters_create()
# corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
# gray = aruco.drawDetectedMarkers(gray, corners, ids, (0,255,0))
# cv2.imshow('frame', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(corners)
#
#
# print("Hello")
# print(parameters)
# corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)