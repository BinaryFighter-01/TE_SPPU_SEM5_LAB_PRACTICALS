# udp_client.py
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    message = input("Enter message: ")
    client.sendto(message.encode(), ('localhost', 9876))
    
    data, _ = client.recvfrom(1024)
    print(f"Server response: {data.decode()}")
    
    client.close()

if __name__ == '__main__':
    main()