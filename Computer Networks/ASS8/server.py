import socket
import os

def transfer_file(conn, filename):
    with open(filename, 'rb') as f:
        data = f.read()
        conn.send(str(len(data)).encode())
        conn.send(data)

def main():
    with socket.socket() as s:
        s.bind(('127.0.0.1', 65432))
        s.listen()
        print('Server running...')
        
        while True:
            conn, addr = s.accept()
            print(f'Client connected: {addr}')
            
            while True:
                cmd = conn.recv(1024).decode()
                if cmd == 'quit':
                    break
                    
                fname = conn.recv(1024).decode()
                if cmd == 'send':
                    size = int(conn.recv(1024).decode())
                    data = conn.recv(size)
                    with open(fname, 'wb') as f:
                        f.write(data)
                    print(f'Received: {fname}')
                elif cmd == 'get':
                    if os.path.exists(fname):
                        transfer_file(conn, fname)
                        print(f'Sent: {fname}')
                    
            conn.close()

if __name__ == '__main__':
    main()