from __future__ import print_function
from CalibrationPattern import ChessBoard
from Camera import KinectDevice
import cv2

kinect = KinectDevice.Kinect()

print("Kinect device  = ", kinect)
while(True):
    colorFrame = kinect.getColorFrame()
    checkerBoard = ChessBoard.ChessBoard(RGB=colorFrame)
    checkerBoard.showGray()
    checkerBoard.getObjectnImagePoints()
    checkerBoard.save()

    # kinect.colorSpaceToCameraSpace()

    # ret, _ = checkerBoard.findCorners()
    # if ret:
    #     break
