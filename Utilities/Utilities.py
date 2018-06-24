import cv2 as openCV
import numpy as np
import os
import thread
import time
import datetime

class Utils:
    __randomCounter = 1;

    @classmethod
    def imshowNonBlocking(cls, image, name = "Image" + str(__randomCounter), waitKey = 0):
        cls.__randomCounter = cls.__randomCounter + 1
        try:
            thread.start_new_thread(cls.__imshow, (image, name, waitKey))
        except:
            print("Unable to start the thread for displaying image!")

    @classmethod
    def imshow(cls, image, name = "Image" + str(__randomCounter), waitKey=0):
        openCV.namedWindow(name, openCV.WND_PROP_FULLSCREEN)
        openCV.setWindowProperty(name, openCV.WND_PROP_FULLSCREEN, openCV.WINDOW_FULLSCREEN)
        openCV.imshow(name, image)
        openCV.waitKey(waitKey)
        openCV.destroyAllWindows()

    @classmethod
    def getTimestampAsString(cls):
        # return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        return datetime.datetime.now().strftime("%d-%m-%Y--%H%M%S")
    