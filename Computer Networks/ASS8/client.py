import socket

def transfer_file(s, filename, mode='rb'):
    with open(filename, mode) as f:
        data = f.read() if 'b' in mode else f.read().encode()
        s.send(str(len(data)).encode())
        s.send(data)

def main():
    with socket.socket() as s:
        s.connect(('127.0.0.1', 65432))
        while True:
            cmd = input('Command (send/get/quit): ').lower()
            if cmd == 'quit':
                s.send(b'quit')
                break
            
            s.send(cmd.encode())
            fname = input('Filename: ')
            s.send(fname.encode())
            
            if cmd == 'send':
                transfer_file(s, fname)
                print(f'Sent: {fname}')
            elif cmd == 'get':
                size = int(s.recv(1024).decode())
                data = s.recv(size)
                with open(fname, 'wb') as f:
                    f.write(data)
                print(f'Received: {fname}')

if __name__ == '__main__':
    main()