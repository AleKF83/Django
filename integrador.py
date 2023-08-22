
#1. Escribir una función que calcule el máximo común divisor entre dos números.

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a
print("EJERCICIO 1:")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

mcd = calcular_mcd(num1, num2)
print(f"El Máximo Común Divisor de {num1} y {num2} es {mcd}")

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)
print("EJERCICIO 2:")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = lcm(numero1, numero2)
print(f"El mínimo común múltiplo entre {numero1} y {numero2} es: {resultado}")

#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario concada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabra(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia
print("EJERCICIO 3:")
cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabra(cadena)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
"""
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
"""
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

def palabras_mas_repetidas(diccionario):
    max_frecuencia = max(diccionario.values())
    palabras_rep = [palabra for palabra, frecuencia in diccionario.items() if frecuencia == max_frecuencia]
    return palabras_rep, max_frecuencia

cadena = input("Ingrese una cadena de caracteres: ")
frecuencia = contar_palabras(cadena)
palabras_rep, frecuencia_max = palabras_mas_repetidas(frecuencia)

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia.items():
    print(f"{palabra}: {frecuencia}")

print(f"Las palabras más repetidas son {', '.join(palabras_rep)} con una frecuencia de {frecuencia_max}.")


"""
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""
print("EJERCICIO 5:")

def get_int():

    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("¡Valor no válido! Intente nuevamente.")

entero = get_int()
print(f"Valor entero ingresado: {entero}")

"""
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
        
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("Edad inválida. No se ha actualizado la edad.")
        
    def get_edad(self):
        return self.edad
        
    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("DNI inválido. No se ha actualizado el DNI.")
        
    def get_dni(self):
        return self.dni
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
        
    def es_mayor_de_edad(self):
        return self.edad >= 18
print("EJERCICIO 6:")
# Crear una instancia de la clase Persona
persona1 = Persona()

# Establecer los atributos
persona1.set_nombre("Juan")
persona1.set_edad(5)
persona1.set_dni("123456789")

# Mostrar los datos de la persona
persona1.mostrar()

# Comprobar si es mayor de edad
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")


"""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa")

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print("Titular:", self.titular.get_nombre())
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad += cantidad
        else:
            print("No se puede ingresar una cantidad negativa")

    def retirar(self, cantidad):
        self.cantidad -= cantidad
print("EJERCICIO 7:")
# Crear una persona y una cuenta de ejemplo
persona2 = Persona("Ana", 30, "98765432B")
cuenta1 = Cuenta(persona2, 1000.0)

cuenta1.mostrar()
cuenta1.ingresar(500)
cuenta1.retirar(200)

cuenta1.mostrar()

"""
8.Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de lcuenta. 
"""
class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero de una cuenta joven con un titular inválido")

    def mostrar(self):
        print("Cuenta Joven")
        print("Bonificación:", self.bonificacion, "%")
        super().mostrar()
print("EJERCICIO 8:")
# Crear una persona y una cuenta joven de ejemplo
persona3 = Persona("Carlos", 2, "87654321C")
cuenta_joven1 = CuentaJoven(persona3, 800.0, 5.0)

cuenta_joven1.mostrar()
cuenta_joven1.ingresar(200)
cuenta_joven1.retirar(100)

cuenta_joven1.mostrar()



