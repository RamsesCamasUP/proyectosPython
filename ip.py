import socket


if __name__ == "__main__":
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    print(f'Mi hostname es: {hostname}')
    print(f'Mi dirección Ip es: {ip_adress}')