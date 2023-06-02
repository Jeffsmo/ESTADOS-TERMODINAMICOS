class GuardarDatos:
    def __init__(self, presion, temperatura):
        self.presion = presion
        self.temperatura = temperatura

    def guardarDatos(self):
        try:
            # Abrir el archivo en modo escritura ('w')
            with open('datos.txt', 'w') as archivo:
                # Escribir los datos de presión y temperatura en el archivo
                archivo.write(f'Presión: {self.presion}\n')
                archivo.write(f'Temperatura: {self.temperatura}\n')
            print('Datos guardados correctamente.')
        except IOError:
            print('Error al guardar los datos en el archivo.')