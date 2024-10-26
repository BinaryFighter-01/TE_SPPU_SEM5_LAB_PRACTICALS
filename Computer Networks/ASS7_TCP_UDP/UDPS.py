# udp_server.py
import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 9876))
    print("UDP Server listening on port 9876")
    
    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode()
        print(f"Received: {message}")
        
        # Send response in uppercase
        response = message.upper()
        server.sendto(response.encode(), addr)

if __name__ == '__main__':
    main()