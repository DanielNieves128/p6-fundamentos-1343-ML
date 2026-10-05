# Daniel Nieves NC=1343
# ==============================================================================
# EJERCICIOS DE PYTHON PARA VISUAL STUDIO CODE
# Basado en las guías de referencia de W3Schools (17 Secciones / 3 Ejemplos c/u)
# ==============================================================================

# ------------------------------------------------------------------------------
# 01. Python Variables
# Ref: https://www.w3schools.com/python/python_variables.asp
# ------------------------------------------------------------------------------
print("\n--- 01. PYTHON VARIABLES ---")

# Ejemplo 1: Creación básica de variables numéricas y de texto
edad = 25
nombre = "Carlos"
print("Ejemplo 1:", nombre, "tiene", edad, "años.")

# Ejemplo 2: Reasignación de variables (Tipado dinámico)
x = 10       # x es de tipo int
x = "Python" # x ahora es de tipo str
print("Ejemplo 2: Valor reasignado de x ->", x)

# Ejemplo 3: Especificación de tipo mediante casting y verificación de tipo
precio = float(100)
producto = str("Laptop")
print("Ejemplo 3:", producto, "precio:", precio, "| Tipo de precio:", type(precio))


# ------------------------------------------------------------------------------
# 02. Python Variable Names
# Ref: https://www.w3schools.com/python/python_variables_names.asp
# ------------------------------------------------------------------------------
print("\n--- 02. PYTHON VARIABLE NAMES ---")

# Ejemplo 1: Convenciones de nombres de variables (Camel, Pascal y Snake Case)
miNombreVariable = "Camel Case"   # Primera letra minúscula, siguientes mayúsculas
MiNombreVariable = "Pascal Case"  # Cada palabra inicia con mayúscula
mi_nombre_variable = "Snake Case" # Palabras separadas por guión bajo (Recomendado en Python)
print("Ejemplo 1:", miNombreVariable, "|", MiNombreVariable, "|", mi_nombre_variable)

# Ejemplo 2: Nombres de variables sensibles a mayúsculas/minúsculas (Case-Sensitive)
a = 4
A = "Cuatro"
print("Ejemplo 2: a =", a, "| A =", A)

# Ejemplo 3: Nombres permitidos con guión bajo inicial y números no iniciales
_usuario_id = 1001
usuario_2 = "Ana"
print("Ejemplo 3: ID ->", _usuario_id, "| Usuario ->", usuario_2)


# ------------------------------------------------------------------------------
# 03. Python Assign Multiple Values
# Ref: https://www.w3schools.com/python/python_variables_multiple.asp
# ------------------------------------------------------------------------------
print("\n--- 03. PYTHON ASSIGN MULTIPLE VALUES ---")

# Ejemplo 1: Asignar múltiples valores a múltiples variables en una línea
fruta1, fruta2, fruta3 = "Manzana", "Banana", "Cereza"
print("Ejemplo 1:", fruta1, fruta2, fruta3)

# Ejemplo 2: Asignar un mismo valor a múltiples variables
x = y = z = "Igual"
print("Ejemplo 2: x =", x, "| y =", y, "| z =", z)

# Ejemplo 3: Desempaquetado (Unpacking) de una lista en variables
colores = ["Rojo", "Verde", "Azul"]
c1, c2, c3 = colores
print("Ejemplo 3: Colores desempaquetados ->", c1, c2, c3)


# ------------------------------------------------------------------------------
# 04. Python Output Variables
# Ref: https://www.w3schools.com/python/python_variables_output.asp
# ------------------------------------------------------------------------------
print("\n--- 04. PYTHON OUTPUT VARIABLES ---")

# Ejemplo 1: Salida de múltiples variables separadas por comas
curso = "Python"
nivel = "Básico"
print("Ejemplo 1: Curso:", curso, "- Nivel:", nivel)

# Ejemplo 2: Concatenación de cadenas con el operador '+'
saludo = "Hola"
persona = "María"
print("Ejemplo 2: " + saludo + " " + persona)

# Ejemplo 3: Uso de f-strings para salida formateada
puntos = 95
print(f"Ejemplo 3: El estudiante {persona} obtuvo {puntos} puntos.")


# ------------------------------------------------------------------------------
# 05. Python Global Variables
# Ref: https://www.w3schools.com/python/python_variables_global.asp
# ------------------------------------------------------------------------------
print("\n--- 05. PYTHON GLOBAL VARIABLES ---")

# Ejemplo 1: Acceso a una variable global dentro de una función
mensaje_global = "Global"

def mostrar_global():
    print("Ejemplo 1: Variable leída dentro de la función ->", mensaje_global)

mostrar_global()

# Ejemplo 2: Variable local con el mismo nombre (Shadowing)
version = "v1.0"

def cambiar_local():
    version = "v2.0" # Variable local
    print("Ejemplo 2: Dentro de función ->", version)

cambiar_local()
print("Ejemplo 2: Fuera de función ->", version)

# Ejemplo 3: Modificación de variable global usando la palabra clave 'global'
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print("Ejemplo 3: Contador global modificado ->", contador)


# ------------------------------------------------------------------------------
# 06. Python Data Types
# Ref: https://www.w3schools.com/python/python_datatypes.asp
# ------------------------------------------------------------------------------
print("\n--- 06. PYTHON DATA TYPES ---")

# Ejemplo 1: Tipos numéricos y texto
texto = "Hola Mundo"          # str
entero = 20                   # int
decimal = 20.5                # float
print("Ejemplo 1:", type(texto), type(entero), type(decimal))

# Ejemplo 2: Tipos de secuencia (list, tuple, range)
lista = ["a", "b", "c"]       # list
tupla = ("a", "b", "c")       # tuple
rango = range(5)              # range
print("Ejemplo 2:", type(lista), type(tupla), type(rango))

# Ejemplo 3: Tipos de mapeo y conjuntos (dict, set, bool)
diccionario = {"nombre": "Ana", "edad": 30} # dict
conjunto = {"manzana", "banana"}             # set
booleano = True                             # bool
print("Ejemplo 3:", type(diccionario), type(conjunto), type(booleano))


# ------------------------------------------------------------------------------
# 07. Python Numbers
# Ref: https://www.w3schools.com/python/python_numbers.asp
# ------------------------------------------------------------------------------
print("\n--- 07. PYTHON NUMBERS ---")

# Ejemplo 1: Números enteros (int) positivos y negativos
num_int1 = 12345
num_int2 = -98765
print("Ejemplo 1: Enteros ->", num_int1, num_int2)

# Ejemplo 2: Números flotantes (float) con decimales y notación científica
num_float1 = 3.1416
num_float2 = 35e3 # 35000.0
print("Ejemplo 2: Flotantes ->", num_float1, num_float2)

# Ejemplo 3: Números complejos (complex)
num_complex = 3 + 5j
print("Ejemplo 3: Complejo ->", num_complex, "| Parte real:", num_complex.real)


# ------------------------------------------------------------------------------
# 08. Python Casting
# Ref: https://www.w3schools.com/python/python_casting.asp
# ------------------------------------------------------------------------------
print("\n--- 08. PYTHON CASTING ---")

# Ejemplo 1: Conversión a entero usando int()
c1 = int(2.8)     # Convierte float a int (trunca decimales)
c2 = int("10")    # Convierte str a int
print("Ejemplo 1: int(2.8) ->", c1, "| int('10') ->", c2)

# Ejemplo 2: Conversión a flotante usando float()
f1 = float(5)     # Convierte int a float
f2 = float("4.2") # Convierte str a float
print("Ejemplo 2: float(5) ->", f1, "| float('4.2') ->", f2)

# Ejemplo 3: Conversión a cadena usando str()
s1 = str(100)     # Convierte int a str
s2 = str(3.14)    # Convierte float a str
print("Ejemplo 3: str(100) ->", s1, "(Tipo:", type(s1), ")")


# ------------------------------------------------------------------------------
# 09. Python Strings
# Ref: https://www.w3schools.com/python/python_strings.asp
# ------------------------------------------------------------------------------
print("\n--- 09. PYTHON STRINGS ---")

# Ejemplo 1: Cadenas multilínea e indexación
cadena = "Python"
print("Ejemplo 1: Primer carácter ->", cadena[0], "| Último carácter ->", cadena[-1])

# Ejemplo 2: Slicing (Recorte de cadenas)
frase = "Programación en Python"
subcadena = frase[0:12] # Desde índice 0 hasta 11
print("Ejemplo 2: Subcadena extraída ->", subcadena)

# Ejemplo 3: Métodos comunes de cadenas (upper, lower, strip, replace)
texto_raw = "  hola mundo  "
print("Ejemplo 3: Mayúsculas ->", texto_raw.upper().strip())
print("Ejemplo 3: Reemplazo ->", texto_raw.replace("mundo", "Python").strip())


# ------------------------------------------------------------------------------
# 10. Python Booleans
# Ref: https://www.w3schools.com/python/python_booleans.asp
# ------------------------------------------------------------------------------
print("\n--- 10. PYTHON BOOLEANS ---")

# Ejemplo 1: Evaluaciones de comparación directa
print("Ejemplo 1: ¿10 > 5? ->", 10 > 5)
print("Ejemplo 1: ¿10 == 9? ->", 10 == 9)

# Ejemplo 2: Evaluación del valor de verdad usando bool()
print("Ejemplo 2: bool('Hola') ->", bool("Hola")) # Truthy
print("Ejemplo 2: bool('') ->", bool(""))         # Falsy (Cadena vacía)
print("Ejemplo 2: bool(0) ->", bool(0))           # Falsy (Cero)

# Ejemplo 3: Evaluaciones booleanas en estructuras condicionales
evaluacion = 15
if bool(evaluacion):
    print("Ejemplo 3: La variable contiene un valor considerado True.")


# ------------------------------------------------------------------------------
# 11. Python Arithmetic Operators
# Ref: https://www.w3schools.com/python/python_operators_arithmetic.asp
# ------------------------------------------------------------------------------
print("\n--- 11. PYTHON ARITHMETIC OPERATORS ---")

# Ejemplo 1: Suma, Resta, Multiplicación y División básica
a, b = 15, 4
print("Ejemplo 1: Suma ->", a + b, "| Resta ->", a - b)
print("Ejemplo 1: Multiplicación ->", a * b, "| División ->", a / b)

# Ejemplo 2: Módulo (resto) y División entera (floor division)
print("Ejemplo 2: Módulo (15 % 4) ->", a % b)
print("Ejemplo 2: División entera (15 // 4) ->", a // b)

# Ejemplo 3: Exponenciación (Potencia)
base, exponente = 2, 8
print("Ejemplo 3: 2 elevado a la 8 (2 ** 8) ->", base ** exponente)


# ------------------------------------------------------------------------------
# 12. Python Assignment Operators
# Ref: https://www.w3schools.com/python/python_operators_assignment.asp
# ------------------------------------------------------------------------------
print("\n--- 12. PYTHON ASSIGNMENT OPERATORS ---")

# Ejemplo 1: Asignación simple y asignación con suma/resta (+=, -=)
x_assign = 10
x_assign += 5  # Equivalente a: x_assign = x_assign + 5
print("Ejemplo 1: Después de += 5 ->", x_assign)

x_assign -= 3  # Equivalente a: x_assign = x_assign - 3
print("Ejemplo 1: Después de -= 3 ->", x_assign)

# Ejemplo 2: Asignación con multiplicación y división (*=, /=)
y_assign = 4
y_assign *= 3  # Equivalente a: y_assign = y_assign * 3
print("Ejemplo 2: Después de *= 3 ->", y_assign)

y_assign /= 2  # Equivalente a: y_assign = y_assign / 2
print("Ejemplo 2: Después de /= 2 ->", y_assign)

# Ejemplo 3: Asignación con módulo y exponenciación (%=, **=)
z_assign = 7
z_assign %= 3  # Equivalente a: z_assign = z_assign % 3
print("Ejemplo 3: Después de %= 3 ->", z_assign)

z_assign **= 4 # Equivalente a: z_assign = z_assign ** 4
print("Ejemplo 3: Después de **= 4 ->", z_assign)


# ------------------------------------------------------------------------------
# 13. Python Comparison Operators
# Ref: https://www.w3schools.com/python/python_operators_comparison.asp
# ------------------------------------------------------------------------------
print("\n--- 13. PYTHON COMPARISON OPERATORS ---")

n1, n2 = 20, 20
n3 = 30

# Ejemplo 1: Operadores de Igualdad (==) y Desigualdad (!=)
print("Ejemplo 1: ¿20 == 20? ->", n1 == n2)
print("Ejemplo 1: ¿20 != 30? ->", n1 != n3)

# Ejemplo 2: Mayor que (>) y Menor que (<)
print("Ejemplo 2: ¿30 > 20? ->", n3 > n1)
print("Ejemplo 2: ¿20 < 30? ->", n1 < n3)

# Ejemplo 3: Mayor o igual que (>=) y Menor o igual que (<=)
print("Ejemplo 3: ¿20 >= 20? ->", n1 >= n2)
print("Ejemplo 3: ¿20 <= 30? ->", n1 <= n3)


# ------------------------------------------------------------------------------
# 14. Python Logical Operators
# Ref: https://www.w3schools.com/python/python_operators_logical.asp
# ------------------------------------------------------------------------------
print("\n--- 14. PYTHON LOGICAL OPERATORS ---")

val1 = 10

# Ejemplo 1: Operador AND (Devuelve True si ambas afirmaciones son verdaderas)
res_and = (val1 > 5) and (val1 < 20)
print("Ejemplo 1: (10 > 5 y 10 < 20) ->", res_and)

# Ejemplo 2: Operador OR (Devuelve True si al menos una afirmación es verdadera)
res_or = (val1 > 15) or (val1 == 10)
print("Ejemplo 2: (10 > 15 o 10 == 10) ->", res_or)

# Ejemplo 3: Operador NOT (Invierte el resultado booleano)
res_not = not(val1 > 5)
print("Ejemplo 3: not(10 > 5) ->", res_not)


# ------------------------------------------------------------------------------
# 15. Python Identity Operators
# Ref: https://www.w3schools.com/python/python_operators_identity.asp
# ------------------------------------------------------------------------------
print("\n--- 15. PYTHON IDENTITY OPERATORS ---")

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

# Ejemplo 1: Operador 'is' (Comprueba si ambas variables apuntan al mismo objeto)
print("Ejemplo 1: list_a is list_c ->", list_a is list_c) # True (Misma memoria)
print("Ejemplo 1: list_a is list_b ->", list_a is list_b) # False (Mismo contenido, diferente memoria)

# Ejemplo 2: Operador 'is not' (Comprueba si no son el mismo objeto)
print("Ejemplo 2: list_a is not list_b ->", list_a is not list_b) # True

# Ejemplo 3: Comparación entre igualdad de valor (==) e identidad (is)
print("Ejemplo 3: Valor (list_a == list_b) ->", list_a == list_b) # True
print("Ejemplo 3: Identidad (list_a is list_b) ->", list_a is list_b) # False


# ------------------------------------------------------------------------------
# 16. Python Membership Operators
# Ref: https://www.w3schools.com/python/python_operators_membership.asp
# ------------------------------------------------------------------------------
print("\n--- 16. PYTHON MEMBERSHIP OPERATORS ---")

frutas = ["manzana", "platano", "cereza"]

# Ejemplo 1: Operador 'in' en listas y cadenas
print("Ejemplo 1: ¿'platano' in frutas? ->", "platano" in frutas)
print("Ejemplo 2: ¿'Py' in 'Python'? ->", "Py" in "Python")

# Ejemplo 2: Operador 'not in' en listas
print("Ejemplo 2: ¿'uva' not in frutas? ->", "uva" not in frutas)

# Ejemplo 3: Operador 'in' en diccionarios (Comprueba claves)
usuario_data = {"username": "admin", "role": "editor"}
print("Ejemplo 3: ¿'role' in usuario_data? ->", "role" in usuario_data)
print("Ejemplo 3: ¿'admin' in usuario_data? ->", "admin" in usuario_data) # False (Busca claves, no valores)


# ------------------------------------------------------------------------------
# 17. Python Bitwise Operators
# Ref: https://www.w3schools.com/python/python_operators_bitwise.asp
# ------------------------------------------------------------------------------
print("\n--- 17. PYTHON BITWISE OPERATORS ---")

# Números en binario: 6 = 0110, 3 = 0011
num_a, num_b = 6, 3

# Ejemplo 1: Operadores Bitwise AND (&) y OR (|)
print("Ejemplo 1: 6 & 3 (AND binario) ->", num_a & num_b) # Resulta 2 (0010)
print("Ejemplo 1: 6 | 3 (OR binario) ->", num_a | num_b)  # Resulta 7 (0111)

# Ejemplo 2: Operadores Bitwise XOR (^) y NOT (~)
print("Ejemplo 2: 6 ^ 3 (XOR binario) ->", num_a ^ num_b) # Resulta 5 (0101)
print("Ejemplo 2: ~6 (NOT / Complemento) ->", ~num_a)     # Resulta -7

# Ejemplo 3: Desplazamiento de bits a la izquierda (<<) y derecha (>>)
print("Ejemplo 3: 6 << 1 (Shift izquierda) ->", num_a << 1) # Resulta 12 (1100)
print("Ejemplo 3: 6 >> 1 (Shift derecha) ->", num_a >> 1)   # Resulta 3 (0011)

print("\n==============================================================================")
print("¡TODOS LOS EJERCICIOS SE EJECUTARON CORRECTAMENTE!")
print("==============================================================================")
print("Daniel Nieves NC=1343")