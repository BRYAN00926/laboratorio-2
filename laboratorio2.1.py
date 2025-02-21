# 1. Programación Estructurada - Factorial de un número

def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {calcular_factorial(numero)}")


# 2. Programación Orientada a Objetos - Clase Círculo
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

radio = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio)
print(f"El área del círculo es: {circulo.calcular_area():.2f}")
print(f"La circunferencia del círculo es: {circulo.calcular_circunferencia():.2f}")


# 3. Programación Funcional - Filtrar pares y calcular cuadrados
numeros = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
pares_cuadrados = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))
print(f"Los cuadrados de los números pares son: {pares_cuadrados}")