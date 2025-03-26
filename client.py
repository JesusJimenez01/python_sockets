import socket
import ctypes


class TemperatureData(ctypes.Structure):
    _fields_ = [("temp1", ctypes.c_int),
                ("temp2", ctypes.c_int),
                ("temp3", ctypes.c_short),
                ("temp4", ctypes.c_short),
                ("temp5", ctypes.c_long),
                ("temp6", ctypes.c_long)]

    def __setattr__(self, name, value):

        ranges = {
            "temp1": (-2147483648, 2147483647),
            "temp2": (-2147483648, 2147483647),
            "temp3": (-32768, 32767),
            "temp4": (-32768, 32767),
            "temp5": (-2147483648, 2147483647),
            "temp6": (-2147483648, 2147483647),
        }

        if name in ranges:
            min_value, max_value = ranges[name]
            if not (min_value <= value <= max_value):
                raise ValueError(
                    f"❌ Error: {name} ({value}) está fuera del rango permitido ({min_value} a {max_value})")

        super().__setattr__(name, value)



def run_client():
    server_address = ('localhost', 8000)

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(server_address)
        data = TemperatureData(25, 30, 1800000, 22, 150000, 160000)

        client.send(bytes(data))

        response = client.recv(1024).decode()
        print(f"Server response: {response}")

    except ConnectionRefusedError:
        print('Connection refused.')
    except KeyboardInterrupt:
        print('Client interrupted')
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()


run_client()
