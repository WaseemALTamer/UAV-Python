import ServoAngleConverter
import UAVController
import PostionReciver
import PostionSender
import threading
import time
import Gyro


threading.Thread(target=UAVController.Servo_1).start()
threading.Thread(target=UAVController.Servo_2).start()
threading.Thread(target=UAVController.BMotor)

threading.Thread(target=PostionReciver.main).start()
threading.Thread(target=PostionSender.main).start()





while True:
    time.sleep(1/70)
    if time.time() - float(PostionReciver.MessageContent[3]) > 0.2:
        continue
    if PostionReciver.MessageContent != []:
        UAVController.PulseDuration_1 = ServoAngleConverter.degree_to_ms(float(PostionReciver.MessageContent[0]))
        UAVController.PulseDuration_2 = ServoAngleConverter.degree_to_ms(float(PostionReciver.MessageContent[1]))
        if float(PostionReciver.MessageContent[2]) == 0:
            UAVController.PulseDuration_3 = 0
        else:
            UAVController.PulseDuration_3 = ((float(PostionReciver.MessageContent[2]))) + 1