import socket
import time


def run_client():
    server_address = ('localhost', 8000)

    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(server_address)
            while True:

                msg = input('Enter message: ')
                client.send(msg.encode())

                try:
                    response = client.recv(1024).decode()
                    if not response:
                        break

                    if response.lower() == 'closed':
                        print('Connection closed')
                        return

                except Exception:
                    print('Error while connecting to server')
                    return

        except ConnectionRefusedError: # Si se desconecta espera 30s y vuelve a intentar conectarse
            print('Connection refused. Reconnecting in 30 seconds...')
            time.sleep(30)
            print('Reconnecting...')
        except KeyboardInterrupt:
            print('Client interrupted')
            break
        except Exception as e:
            print(f"Error: {e}")
            break
        finally:
            client.close()

run_client()