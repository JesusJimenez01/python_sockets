import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen()

conn, addr = server.accept()

data = conn.recv(1024)

first, last, age, gender, weight = struct.unpack('10s10sisf', data)
print(first.decode())
print(last.decode())
print(age)
print(gender.decode())
print(weight)