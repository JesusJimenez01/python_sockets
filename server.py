import socket
import threading
import ctypes


class TemperatureData(ctypes.Structure):
    _fields_ = [("temp1", ctypes.c_int),
                ("temp2", ctypes.c_int),
                ("temp3", ctypes.c_short),
                ("temp4", ctypes.c_short),
                ("temp5", ctypes.c_long),
                ("temp6", ctypes.c_long)]

def handle_client(client_socket, addr):
    try:

        data = client_socket.recv(ctypes.sizeof(TemperatureData))

        if data:

            received_data = TemperatureData.from_buffer_copy(data)

            print(f"Received Temperatures from {addr}:")
            print(f"Temp1: {received_data.temp1}, Temp2: {received_data.temp2},")
            print(f"Temp3: {received_data.temp3}, Temp4: {received_data.temp4},")
            print(f"Temp5: {received_data.temp5}, Temp6: {received_data.temp6}")

            response = "accepted"
            client_socket.send(response.encode())

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        print(f"Closing connection with {addr}")
        client_socket.close()

def run_server():
    server_address = ('localhost', 8000)

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(server_address)
        server.listen()

        print(f"Listening on {server_address}")

        while True:
            client_socket, client_address = server.accept()
            print(f"Accepted connection from {client_address}")

            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()

    except KeyboardInterrupt:
        print("Closing server...")
    finally:
        server.close()
        print("Server closed")

run_server()
