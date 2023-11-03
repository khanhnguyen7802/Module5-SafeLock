import socket

TCP_IP = '145.126.67.97'  # Replace with the IP of your Java server
TCP_PORT = 12345  # Make sure this port matches the one in the Java server
BUFFER_SIZE = 1024
MESSAGE = "Hello, Java!"

def send_data(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(data.encode())
    s.close()
