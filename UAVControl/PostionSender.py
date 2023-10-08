import socket
import Gyro
import time

target_port = 3003     
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = ""

ClientsIp = ["192.168.1.173","192.168.1.133"]


def main():
    global target_port, udp_socket, message, ClientsIp
    while True:
        message = f"{Gyro.main()}@{time.time()}"
        try:
            for Client in ClientsIp:
                udp_socket.sendto(message.encode(), (Client, target_port))
        except:
            pass
        time.sleep(1/60)