import socket
import logging

class Servidor:

    # Configuración del logging para registrar la actividad
    logging.basicConfig(filename='servidor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def __init__(self):
        self.host = "127.0.0.1"
        self.puerto = 8809
        self.server_socket = None
        self.acceso = False
    
    def iniciar_servidor(self):
        # Configurar el socket del servidor
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.puerto))
        self.server_socket.listen(5)
        print(f"Servidor escuchando en {self.host}:{self.puerto}...")
    
        while True:
            conexion, direccion = self.server_socket.accept()
            print(f"Conexión establecida con {direccion}")
            try:
                datos = conexion.recv(1024)
                if not datos:
                    continue
    
                # Intentar convertir los datos recibidos a entero
                try:
                    datosRecibidos = int(datos.decode().strip())
                except ValueError:
                    respuesta = "Error: Entrada no es un número entero."
                    conexion.send(respuesta.encode())
                    logging.error(f"Datos inválidos recibidos: {datos.decode().strip()}")
                    conexion.close()
                    continue

                # Verificar la password
                if self.PasswordVerification(password):
                    respuesta = f"La password {password} es correcta."
                    self.acceso = True
                else:
                    respuesta = f"La password {password} no es correcta."
                    self.acceso = False

                # Enviar la respuesta al cliente
                conexion.send(respuesta.encode())
                logging.info(f"Recibido: {password} - Respuesta: {respuesta}")
    
            except Exception as e:
                logging.error(f"Error en la conexión: {e}")
            finally:
                self.acceso = False
                conexion.close()