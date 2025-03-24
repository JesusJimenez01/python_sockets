import socket
import threading


def handle_client(client_socket, addr):
    try:
        while True:
            client_socket.settimeout(30) # Si pasan 30 segundos sin respuesta del cliente lanza un error
            try:

                data = client_socket.recv(1024).decode()
                if data.lower() == "close":
                    client_socket.send("closed".encode())
                    client_socket.close()
                    break

                print(f"Received: {data}")
                response = "accepted"
                client_socket.send(response.encode())

            except socket.timeout:
                print("No message received")
                break


    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print(f"Client ({addr[0]}:{addr[1]}) disconnected")


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
        return

    except Exception as error:
        print(f"Error: {error}")

    finally:
        server.close()
        print("Server closed")

run_server()