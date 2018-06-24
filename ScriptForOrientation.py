from __future__ import print_function
from CalibrationPattern import ChessBoard
from CalibrationPattern import ArucoMarker
from Camera import DummyDevice
from Camera import KinectDevice
from Camera import CameraParams
import matlab.engine

# device = DummyDevice.DummyDevice()
matlabEngine = matlab.engine.start_matlab()

device = KinectDevice.Kinect()
counter = 0
dict = None

while(True):
    colorFrame = device.getColorFrame()
    counter = counter + 1
    if colorFrame is None or counter > 20:
        break

    patternBoard = ArucoMarker.ArucoMarker(RGB=colorFrame)
    patternBoard.showGray()

    cParams = CameraParams.CameraParams.loadCameraParameters('CameraParams_31-05-2018--232958.pkl')
    rvec, tvec = patternBoard.findPoseOfPattern(cParams)

    if rvec is None or tvec is None or len(rvec) == 0 or len(tvec) == 0:
        counter = counter - 1
        continue

    dict = cParams.saveParamsAsMat("Test.mat",rotationalVector = rvec, translationVector = tvec, dict=dict)
    print(matlabEngine.displayCameranCheckerBoard(nargout=0))

matlabEngine.quit()

