import ServoAngleConverter
import RPi.GPIO as GPIO
import threading
import time
import pigpio


frequency = 50

servo_pin_1 = 17
PulseDuration_1 = 1

servo_pin_2 = 15
PulseDuration_2 = 1

BMotor_pin_2 = 4
PulseDuration_3 = 1100

def Servo_1():
        global servo_pin_1, PulseDuration_1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin_1,GPIO.OUT)
        while True:
                GPIO.output(servo_pin_1, GPIO.HIGH)
                time.sleep(PulseDuration_1 * 0.001)
                GPIO.output(servo_pin_1, GPIO.LOW)
                time.sleep(1/frequency - (PulseDuration_1 * 0.001))
def Servo_2():
        global servo_pin_2, PulseDuration_2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin_2,GPIO.OUT)
        while True:
                GPIO.output(servo_pin_2, GPIO.HIGH)
                time.sleep(PulseDuration_2 * 0.001)
                GPIO.output(servo_pin_2, GPIO.LOW)
                time.sleep(1/frequency - (PulseDuration_2 * 0.001))

def BMotor():
        global BMotor_pin_2, PulseDuration_3
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(BMotor_pin_2, 0)
        print(PulseDuration_3)
        while True:
                pi.set_servo_pulsewidth(BMotor_pin_2, PulseDuration_3)