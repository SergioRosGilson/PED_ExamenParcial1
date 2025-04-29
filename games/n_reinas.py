# games/n_reinas.py

class NReinas:
    def __init__(self, n):
        self.n = n
        self.tablero = [[0] * n for _ in range(n)]
        self.soluciones = []

    def es_seguro(self, fila, columna):
        # Comprobar filas y diagonales hacia arriba
        for i in range(fila):
            # Revisa columna
            if self.tablero[i][columna] == 1:
                return False
            # Revisa diagonal izquierda
            if columna - (fila - i) >= 0 and self.tablero[i][columna - (fila - i)] == 1:
                return False
            # Revisa diagonal derecha
            if columna + (fila - i) < self.n and self.tablero[i][columna + (fila - i)] == 1:
                return False
        return True

    def resolver(self, fila=0):
        if fila == self.n:
            # Almacenamos una copia profunda de la solución
            self.soluciones.append([fila[:] for fila in self.tablero])
            return
        for columna in range(self.n):
            if self.es_seguro(fila, columna):
                self.tablero[fila][columna] = 1
                self.resolver(fila + 1)
                self.tablero[fila][columna] = 0

    def get_solucion(self):
        if not self.soluciones:
            self.resolver()
        return self.soluciones[0] if self.soluciones else None

    def estado_a_json(self):
        import json
        # Convierte el tablero actual a una cadena JSON
        return json.dumps(self.tablero)
