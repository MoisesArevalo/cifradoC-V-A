import time
import socket
import sys
import encriptar as ecp
def cifrar(message,opcion):
    if(opcion==2):
        return ecp.cifraVigenere(message)
    elif(opcion==3):
        return ecp.cifraAfin(message)
    else:
        return ecp.cifraCesar(message)
def decifrar(message,opcion):
    if(opcion==2):
        return ecp.decifrarVigenere(message)
    elif(opcion==3):
        return ecp.decifrarAfin(message)
    else:
        return ecp.decifrarCesar(message)
print('Usuario....')
time.sleep(1)
so = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
# conecta con el servidor
print(host, '({})'.format(ip))
server_host = input('Ingrese la IP del servidor: ')
name = input('Ingrese su alias:')
port = 4321
print('Conectando al servidor.')
time.sleep(1)
so.connect((server_host,port))
print('Conectando....')
so.send(name.encode())
server_name = so.recv(1024)
server_name = server_name.decode()
print('{} se unio..'.format(server_name))
print('Ingrese adios para salir.')
opcion = int(input('Encriptar por:\n1.Cesar\n2.Vigenere\n3.Afin\nDefault [1]'))
while 1:
    message = so.recv(1024)
    message = message.decode()
    print(server_name,' cifrado >',message)
    message = decifrar(message.upper(),opcion)
    print(server_name,' decifrado > ',message)
    message = input(str('> '))
    if message == 'adios':
        message = 'Me tengo que desconectar'
        message = cifrar(message.upper(),opcion)
        so.send(message.encode())
        print('*******************')
        break
    message = cifrar(message.upper(),opcion)
    so.send(message.encode())
