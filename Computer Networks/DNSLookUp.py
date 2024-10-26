import socket

choice = int(input("1. Enter Host Name\n2. Enter IP address\nChoice = "))
host = input("\nEnter host name or IP address: ")

try:
    if choice == 1:
        addr = socket.gethostbyname(host)
        print(f"IP address: {addr}")
    else:
        addr = socket.gethostbyaddr(host)
        print(f"Host name: {addr[0]}")
        print(f"IP address: {addr[2][0]}")
except socket.gaierror:
    print(f"Could not find {host}")


 ################################################################

 import socket

choice = int(input("1.Enter host name \2. Enter IP Address"))
host = input("Enter host name or ip address")

try:
    if choice==1:
        addr = socket.gethostbyname(host)
        print(f"IP Address {addr}")

    else:
        addr = socket.gethostbyaddr(host)
        print(f"Host name {addr[0]}")
        print(f"IP address{addr[2][0]}")
except socket.gaierror:
    print(f"Could not find {host}")


