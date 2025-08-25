import os

os.system("cls") 

"""
Este es un comentario multilinea

"""
#Este es un comentario multilinea

print('hola mundo')

if 5 > 3:
  if 5 > 4:
    print('5 es mayor que 4')
#Variables
# Contenedor para almacenar datos

x = 5
txt = 'Esto es un texto'
_variable = "My variable"

print(x)
print(txt)


camelCase = ""
PascalCase = ""
snake_case = ""

a,b,c = 1,5,6
print(a)
print(b)
print(c)

frutas = ["naranja","banana","mandarina"]
m,n,o = frutas


nombre = "cristian"
edad = 45
print(f"Hola que tal {nombre} y tienes " + str(edad) + " años.")

#variables globales vs variables locales

def funcion():
  variable_scope = "variable de scope"
  global variable_global
  variable_global = "variable global"
  print(variable_scope)
  # print(variable_global)
  
funcion()
print(variable_global)


"""
=======================================================
Tipos de datos
=======================================================
"""

#str => string o cadena de texto

string_python = ""
string_python2 = ''
string_python3 = '''Este es un texto'''

#int => integer número entero
numero_entero = 10

#float => flotante número decimal
numero_decimal = 5.6
print(float(5))
print(numero_decimal)

#complex => numero complejo
numero_complejo = 5 + 2j

#lista => colección, ordenada y mutable => tienen index
list_obj = [0,1,2,3,4,5,6,7,8,9]

#tupla => colección, ordeanda e inmutable => tienen index
tupla = (0,1,2,3,4,5,6,7,8,9)

#range => rango => secuencia de números de un rango
rango = range(1,10)
print(rango)

#dict => colección de key-value desordenada y mutable
diccionario = { "a" : 1, "b" : 2, "c" : 3 }

#set => colección desordana únicos desordenados y mutables
conjunto = {1,1,2,2,3,3}
print(conjunto)

#frozenSet([]):colección desordenada únicos e inmutables
conjunto_inmutable = frozenset([1,2,3,4,5,6,6,3])
print(conjunto_inmutable)

#bool (booleanos) : valores verdaderos o falso
boolf = False
boolT = True