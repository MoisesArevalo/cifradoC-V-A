#
# El algoritmo para crear el chat, fue replicado de la siguiente pagina
#https://www.tutorialspoint.com/simple-chat-room-using-python
import socket, time , sys
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
print('COnfiguracion de Servidor')
time.sleep(1)
so= socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 4321
so.bind((host,port))
print(host,'({})'.format(ip))
name = input('Ingrese su alias:')
so.listen(1)
print('Esperando conexiones')
connection, addr = so.accept()
print('Se conecto de ',addr[0],'(',addr[1],')')
print('Se establecio la conexion, Conectado desde: {}, ({})'.format(addr[0], addr[0]))
client = connection.recv(1024)
client = client.decode()
print(client, ' se conecto')
print('Escriba adios para desconectarse.')
connection.send(name.encode())
opcion = int(input('Encriptar por:\n1.Cesar\n2.Vigenere\n3.Afin\nDefault [1]'))
while 1:
    message = input('> ')
    if message == 'adios':
        message = 'Me tengo que desconectar'
        message = cifrar(message.upper(),opcion)
        connection.send(message.encode())
        print('*******************')
        so.close()
        break
    message = cifrar(message.upper(),opcion)
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client,' cifrado >',message)
    message = decifrar(message.upper(),opcion)
    print(client,'decifrado >',message)