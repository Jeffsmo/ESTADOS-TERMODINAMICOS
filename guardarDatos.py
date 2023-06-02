class GuardarDatos:
    def __init__(self, presion, temperatura):
        self.presion = presion
        self.temperatura = temperatura

    def guardarDatos(self, date, nombreFigura):
        try:

            contenido_previo = ''
            try:
                with open('Registro.txt', 'r') as archivo_previo:
                    contenido_previo = archivo_previo.read()
            except FileNotFoundError:
                pass

            with open('Registro.txt', 'w') as archivo:
                archivo.write(contenido_previo)
                archivo.write(f'Nombre de la Figura: {nombreFigura}\n')
                archivo.write(f'Fecha de Registro: {date}\n')
                archivo.write(f'Presión: {self.presion}\n')
                archivo.write(f'Temperatura: {self.temperatura}\n')
            print('Datos guardados correctamente.')
        except IOError:
            print('Error al guardar los datos en el archivo.')