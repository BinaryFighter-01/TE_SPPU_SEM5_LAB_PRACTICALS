# tcp_client.py
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 6789))
    
    message = "Hello, server!"
    client.send(message.encode())
    
    response = client.recv(1024).decode()
    print(f"Server response: {response}")
    
    client.close()

if __name__ == '__main__':
    main()