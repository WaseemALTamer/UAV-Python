import socket
import time
import keyboard


target_port = 3003     
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = f"45@45@0@{time.time()}"

ClientsIp = ["192.168.1.173"]


def main():
    global target_port, udp_socket, message, ClientsIp
    while True:
        try:
            for Client in ClientsIp:
                udp_socket.sendto(message.encode(), (Client, target_port))
        except:
            udp_socket.close()
        time.sleep(1/60)