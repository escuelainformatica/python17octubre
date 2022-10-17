class Mensajeria:
    def __init__(self, destino: str, alto: int, ancho: int, largo: int):
        self.destino = destino
        self.alto = alto
        self.ancho = ancho
        self.largo = largo


mensaje_10 = Mensajeria('Coquimbo', 3, 3, 3)
mensaje_11 = Mensajeria('Arica', 4, 4, 4)
volumen = mensaje_10.alto * mensaje_10.ancho * mensaje_10.largo

print(f"El volumen es :{volumen} del envio hacia {mensaje_10.destino}")

# el ejercicio con diccionario
mensaje_dic = {"destino": "Coquimbo", "alto": 3, "ancho": 3, "largo": 3}
mensaje_dic_2 = {"destino": "Arica", "alto": 4, "ancho": 4, "largo": 4}

volumen = mensaje_dic['alto'] * mensaje_dic['ancho'] * mensaje_dic['largo']

print(f"El volumen es :{volumen} del envio hacia {mensaje_dic['destino']}")

# el ejercicio sin diccionario o objeto
destino="Coquimbo"
alto=3
ancho=3
largo=3

destino2="Arica"
alto2=4
ancho2=4
largo2=4

volumen=alto*ancho*largo
print(f"El volumen es {volumen} del envio hacia {destino}")



