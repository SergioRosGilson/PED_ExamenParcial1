import socket
 
class ClienteReina:

    def __init__(self):
        self.host = "127.0.0.1"
        self.puerto = 8809
        self.client_socket = None
    
    def iniciar_cliente(self):
        # Crear el socket del cliente
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.puerto))
            # Juego

            #Enviamos los datos al servidor
            data = 0
            self.client_socket.send(data.encode())
            
            # Recibir la respuesta del servidor
            respuesta = self.client_socket.recv(1024).decode()
            print("Respuesta del servidor:", respuesta)
        except Exception as e:
            print(f"Error en la conexión: {e}")
        finally:
            self.client_socket.close()