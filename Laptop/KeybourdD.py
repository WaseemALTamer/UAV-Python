from pynput import keyboard
import time

message = ""
power = 0
ServoAngle  = "0@0" 


def on_key_press(key):
    global message, power, ServoAngle
    if str(key) == "'w'":
        ServoAngle = "45@-45@"
    if str(key) == "'s'":
        ServoAngle = "-45@45@"
    if str(key) == "'a'":
        ServoAngle = "-45@-45@"
    if str(key) == "'d'":
        ServoAngle = "45@45@"
    if str(key) == "'t'":
        power += 10
    if str(key) == "'y'":
        power -= 10
    if str(key) == "'m'":
        ServoAngle = "0@0@"
    message = f"{ServoAngle}{power * 0.01}@{time.time()}"
        

def main():
    global message, ServoAngle, power
    with keyboard.Listener(on_press=on_key_press) as listener:listener.join()



