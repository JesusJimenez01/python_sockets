import socket
import struct

first_name = 'Jesus'
last_name = 'Jimenez'
age = 24
gender = 'm'
weight = 70.12

data = struct.pack("10s 10s i s f", first_name.encode(), last_name.encode(), age, gender.encode(), weight)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8000))
client.send(data)
client.close()