from __future__ import print_function

import matlab.engine

from CalibrationPattern import ArucoMarker
from Camera import CameraParams
from Camera import KinectDevice
from Camera import DummyDevice
from CalibrationPattern import ChessBoard

device = DummyDevice.DummyDevice()
# device = KinectDevice.Kinect()

matlabEngine = matlab.engine.start_matlab()
matlabEngine.addpath(r'./DataForMatlab/',nargout=0)
counter = 0
dict = None

while(True):
    colorFrame = device.getColorFrame()
    counter = counter + 1
    if colorFrame is None or counter > 20:
        break

    # patternBoard = ArucoMarker.ArucoMarker(RGB=colorFrame)
    patternBoard = ChessBoard.ChessBoard(RGB=colorFrame)
    patternBoard.showGray()

    cParams = CameraParams.CameraParams.loadCameraParameters('CameraParams_27-06-2018--131943.pkl')
    rvec, tvec = patternBoard.findPoseOfPattern(cParams)

    if rvec is None or tvec is None or len(rvec) == 0 or len(tvec) == 0:
        counter = counter - 1
        continue

    dict = cParams.saveParamsAsMat("cameraParameterFromPython.mat",rotationalVector = rvec, translationVector = tvec, dict=dict)
    print(matlabEngine.displayCameranCheckerBoard(nargout=0))

matlabEngine.quit()

