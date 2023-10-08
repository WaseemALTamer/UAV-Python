import UAVSender
import threading



UAVSender.StartCam()
threading.Thread(target=UAVSender.main).start()
