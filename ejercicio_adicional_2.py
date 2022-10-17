# ingresar la mensajeria y calcular el volumen

class Mensajeria:
    def __init__(self, destino: str, alto: int, ancho: int, largo: int):
        self.destino = destino
        self.alto = alto
        self.ancho = ancho
        self.largo = largo


print("Ingrese destino: ")
destino = input()
print("Ingrese alto")
alto = int(input())
print("Ingrese ancho")
ancho = int(input())
print("Ingrese largo")
largo = int(input())

msg = Mensajeria(destino, alto, ancho, largo)

volumen = msg.alto * msg.ancho * msg.largo

print(f"El volumen es :{volumen}")

# usando diccionario
msg_dic = {"destino": destino, "alto": alto, "ancho": ancho, "largo": largo}

volumen = msg_dic['alto'] * msg_dic['ancho'] * msg_dic['largo']

print(f"El volumen es :{volumen}")
