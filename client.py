import socket
import threading
import time


def recv_msg(client):
    try:
        while True:
            try:
                response = client.recv(1024).decode()

                if response.lower() == "waiting":
                    print("\n[Server]: Waiting for response...")
                    print("Enter message: ", end=" ", flush=True)

                elif response.lower() == 'closed':
                    print('Connection closed')
                    break

            except:
                break
    finally:
        client.close()


def run_client():
    server_address = ('localhost', 8000)
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(server_address)

            thread = threading.Thread(target=recv_msg, args=(client,))
            thread.daemon = True
            thread.start()
            msg = input('Enter message: ')
            client.send(msg.encode())


            if msg.lower() == 'close':
                client.close()
                print('Connection closed')
                return

        except ConnectionRefusedError:
            print('Connection refused. Reconnecting in 5 seconds...')
            time.sleep(5)
            print('Reconnecting...')
        except KeyboardInterrupt:
            print('Client interrupted')
            break
        except OSError:
            print('Server error. Reconnecting in 5 seconds...')
            time.sleep(5)
            print('Reconnecting...')
        except Exception as e:
            print(f"Error: {e}")
            break
        finally:
            client.close()


run_client()