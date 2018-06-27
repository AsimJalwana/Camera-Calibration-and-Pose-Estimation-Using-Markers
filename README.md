# Camera Calibration and Pose Estimation Using Markers

## Getting Started
This is pycharm project that does the following tasks
*   Calibration of any RGB camera. 
*   Estimating pose (position and orientation) of any object of known dimensions. 

Currently Kinect v2 camera is supported by default. However any camera can be calibrated using this software. Please see section "Calibration of other Cameras" for details in wiki.
 
Many different pattern types can be used for calibration. The most commonly used patterns include checkerboard and the circle pattern. This software has the support for the Checkerboard. However, any pattern can be integrated seamlessly, Please see section "Adding other Calibration Patterns" for further details in wiki.

### Prerequisites
* Windows 10
* Kinect v2 SDK (https://www.microsoft.com/en-au/download/confirmation.aspx?id=44561)
* Python 2.7 32 bit.
* Matlab R2015b 32 bit, this is the last 32 bit released version.
* matlabengineforpython (R2015b) (https://au.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html#)
* opencv-python 3.4.1.15 (https://github.com/skvark/opencv-python)
* opencv-contrib-python 3.4.1.15 (https://github.com/skvark/opencv-python)
* pykinect2 (if your camera is kinect version 2) (https://github.com/Kinect/PyKinect2/)
* numpy 1.14.3 (http://www.numpy.org/)
* scipy 1.1.0 (https://www.scipy.org/)

### Why Python 2.7 and Why 32 bit?
I started with the 64 bits Python 3.6 and tried integrating with the Kinectv2.0 API. After many trials the 32bit Python 2.7 appeared to be the best choice. This decision affected the choice of Matlab version as well.  

### Why Matlab is being used?
Matlab is just only used for the plotting pose estimation results. Its nice routine would otherwise have to be translated to Python. Beside the same version is available at Woodside.

### Why Matlab is being used?
Matlab is just only used for the plotting pose estimation results. Its nice routine would otherwise have to be translated to Python. Beside the same version is available at Woodside.


* run the ScriptForCameraCalibration.py
* run the ScriptForOrientation.py

More details are shared on the Wiki page. Please refer to it.

