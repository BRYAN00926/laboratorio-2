# Algoritmo con paradigma imperativo
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def exponenciacion(a, b):
    return a ** b

# Prueba de los métodos
a, b = 5, 3
print("Suma:", suma(a, b))
print("Resta:", resta(a, b))
print("Multiplicación:", multiplicacion(a, b))
print("Exponenciación:", exponenciacion(a, b))

# Algoritmo con paradigma orientado a objetos
class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b
    
    def resta(self):
        return self.a - self.b
    
    def multiplicacion(self):
        return self.a * self.b
    
    def exponenciacion(self):
        return self.a ** self.b

# Prueba de la clase
operacion = Operaciones(5, 3)
print("\nUsando la clase:")
print("Suma:", operacion.suma())
print("Resta:", operacion.resta())
print("Multiplicación:", operacion.multiplicacion())
print("Exponenciación:", operacion.exponenciacion())
