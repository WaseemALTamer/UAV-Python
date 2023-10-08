import socket


server_ip = '192.168.1.173'
server_port = 3003

MessageContent = []

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)







def ProcessData(input_string, delimiter="@"):
    parts = input_string.split(delimiter)
    parts = [part for part in parts if part.strip() != '']
    return parts


def main():
    global server_ip, server_port, MessageContent, udp_socket
    udp_socket.bind((server_ip,server_port))
    while True:
        try:
            data, server_address = udp_socket.recvfrom(1024)
            received_message = data.decode()
            print(f"Received from server: {received_message}")
            MessageContent = ProcessData(received_message)
            print(MessageContent)
        except:
            udp_socket.close()
