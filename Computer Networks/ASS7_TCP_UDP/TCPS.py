# tcp_server.py
import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6789))
    server.listen()
    print("TCP Server listening on port 6789")
    
    while True:
        client, addr = server.accept()
        print(f"Connected to {addr}")
        
        data = client.recv(1024).decode()
        print(f"Received: {data}")
        
        response = f"Server received: {data}"
        client.send(response.encode())
        
        client.close()

if __name__ == '__main__':
    main()