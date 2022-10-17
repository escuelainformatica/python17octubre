
# la clase es un plano, es una guia para seguir.
class Cliente:  # deberia partir en mayuscula
    # el self es la instancia
    def __init__(self,nom,apellido,direccion,saldo):
        self.nombre=nom  # self.nombre indica el nombre de la instancia, y nombre indicar el argumento de la funcion
        self.apellido=apellido
        self.direccion=direccion
        self.saldo=saldo

# john es una variable definida por la clase Cliente
# john es un objeto (una variable definida por una clase se llama objeto)
# john es una instancia de Cliente

john=Cliente("John","Doe","Avenida Pacificio 3555",100)
anna=Cliente("Anna","Smith","Calle nueva #200",200)
bob=Cliente("Bob","Williams","Pasaje 12",500)

clientes=[john,anna,bob] # listado de clientes
clientes_tuplas=(john,anna,bob)  # tuplas de clientes

print(f"El primer cliente de clientes: {clientes[0].nombre}")

print(f"Primer cliente:{john.nombre} {john.apellido}, Segundo: {anna.nombre}, Tercer:{bob.nombre}")

# ejemplo con diccionario:
# Nota: no necesito clase

johndic={"nombre":"John","apellido":"Doe","direccion":"Avenida Pacifico","saldo":100}

print(f"Nombre:{johndic['nombre']} {johndic['apellido']}")


#john2=Cliente()
#john2.nombre="John"

