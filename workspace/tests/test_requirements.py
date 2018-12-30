import cv2
import matplotlib
import jupyter

def test_opencv_version():
    assert cv2.__version__ == '3.4.5'

def test_matplotlib_version():
    assert matplotlib.__version__ == '3.0.2'

def test_jupyter_version():
    assert jupyter.__version__ == '1.0.0'