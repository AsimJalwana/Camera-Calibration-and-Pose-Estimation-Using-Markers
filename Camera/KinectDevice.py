from __future__ import print_function
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import CameraParams
import ctypes
import _ctypes
import sys
import numpy as np
import cv2 as openCV
import os
import Device
class Kinect(Device.Device):
    # _runTime = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Depth| PyKinectV2.FrameSourceTypes_Infrared)
    __runTime = None

    def __init__(self):
        super(Kinect, self).__init__()
        self.__class__.__runTime = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Depth)
        self._rgbFrame = None
        self._depthFrame = None
        self._rawDepthFrame = None

    def getColorFrame(self):
        while True:
            if self.__runTime.has_new_color_frame():
                frame = self.__runTime.get_last_color_frame()
                print("Got the Color Frame")
                self._rgbFrame = frame.reshape((self.__runTime.color_frame_desc.Height, self.__runTime.color_frame_desc.width, 4), order='C')

                # r = 1000.0 / self._rgbFrame.shape[1]
                # dim = (1000, int(self._rgbFrame.shape[0] * r))
                # self._rgbFrame = cv2.resize(self._rgbFrame, dim, interpolation=cv2.INTER_AREA)
                break
        return self._rgbFrame

    def getDepthFrame(self):
        while True:
            if self.__runTime.has_new_depth_frame():
                self._rawDepthFrame = self.__runTime.get_last_depth_frame()
                print("Got the depth Frame :)")
                frame = np.uint8(self._rawDepthFrame.clip(1, 4000) / 16.)
                frame8bit = np.dstack((frame, frame, frame))
                self._depthFrame = np.array(frame8bit)
                self._depthFrame = self._depthFrame.reshape((self.__runTime.depth_frame_desc.Height, self.__runTime.depth_frame_desc.Width, 3), order='C')
                break
        return self._depthFrame

    def colorSpaceToCameraSpace(self):
        self.getDepthFrame()
        depthframe = self._rawDepthFrame
        L = depthframe.size
        ptr_depth = np.ctypeslib.as_ctypes(depthframe.flatten())
        S = 1080 * 1920
        TYPE_CameraSpacePointArray = PyKinectV2._CameraSpacePoint * S
        csps1 = TYPE_CameraSpacePointArray()
        print(csps1[1].x, csps1[1].y, csps1[1].z, ptr_depth[1])
        error_state = self.__runTime._mapper.MapColorFrameToCameraSpace(L, ptr_depth, S, csps1)
        print("Error state", error_state)
        print(csps1)
        print(csps1[1].x, csps1[1].y, csps1[1].z, ptr_depth[1])
        csps1[1].x = 2

        for i in range(0, len(csps1)):
            cameraSpacePoint = csps1[i]
            colorSpacePoint = self.__runTime._mapper.MapCameraPointToColorSpace(cameraSpacePoint)
            print(colorSpacePoint.x, colorSpacePoint.y)



        print("end")