import display
import socket
import time
import threading
import PygameDisplay
import statistics


Ip = socket.gethostname() + " :Do Not Change"
Port = 5005


photo = b""
temp_Photo = b""

ImageWriteState = False
state = True

def window():
    global photo, temp_Photo
    while state:
        time.sleep(1/30)
        try:
            if ImageWriteState == False:
                PygameDisplay.run(photo)
                temp_Photo = photo
        except:
            pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), Port)
sock.bind(server_address)


threading.Thread(target=window).start()
#threading.Thread(target=window).start()


checker = []

while True:
    try:
        sock.listen()
        print('Waiting for a client connection...')
        client_sock, client_address = sock.accept()
        print('Accepted connection from', client_address)
        while True:
            try:
                ImageWriteState = True
                data = client_sock.recv(45000)
                ImageWriteState = False
                if not data:
                    break
                checker.append(data[-1])

                if len(checker) == 5:
                    checker = checker[1:]

                if data[-1] == statistics.mode(checker):
                    #pydisolay.run(data)
                    photo = data
                photo = data
                time.sleep(1/45)
            except:
                break
    except socket.error as e:
        print('Error occurred:', e)
