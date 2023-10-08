import socket
import image
import sys
import time

Ip  = '192.168.1.173'
Port = 5005




fps = 0
timer = time.time() + 1

def StartCam():
    image.run()


def main():
    global Ip, Port, fps, timer
    server_address = (Ip, Port)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(server_address)
            print('Connected to the server')
            while True:
                try:
                    message = image.convert(image.get())
                    sock.sendall(message)
                    fps += 1
                    #pygame.time.wait(5)
                except OSError as e:
                    print(f'An error occurred: {e}')
                    break
                except KeyboardInterrupt:
                    break
                except:
                    print('Unexpected error:', sys.exc_info()[0])
                    break

        except ConnectionRefusedError:
            print('Connection refused. Retrying in Now seconds...')
            continue

        except Exception as e:
            print(f'An error occurred: {e}')
            break