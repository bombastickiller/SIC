import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.16', 2345)
print('Conectando a {}  con puerto {}'.format(*server_address))

sock.connect(server_address)

try:
    mensaje = b'Mensaje muy largo.Mensaje muy largo'
    sock.sendall(mensaje)
    
    amount_recieved = 0
    amount_expected = len(mensaje)
    
    while amount_recieved < amount_expected:
        data = sock.recv(16)
        amount_recieved = len(data)
        print('Recibido {!r}'.format(data))
finally:
    sock.close()