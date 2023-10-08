from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import numpy as np
import pyautogui

def display(photo_data):
    if photo_data == "":
        return
    try:
        jpg_data = np.frombuffer(photo_data, dtype=np.uint8)
        img = cv2.imdecode(jpg_data, cv2.IMREAD_COLOR)
        cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
        #cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Window', img)
        cv2.waitKey(1)
    except:
        pass
def close():
    cv2.destroyAllWindows()
