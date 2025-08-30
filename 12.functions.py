
def funcion(profesor,curso):
  print(f"El {profesor} esta dando un curso de {curso}")
  
funcion("Jaime","Matematicas")
funcion("Pedro","Física")
funcion("Sergio","Filosofia")

funcion(curso="Ed.Fisica",profesor="Ramoncito")

def llamar_alumno(**alumno):
  print(type(alumno))
  print(alumno)
  print(f"El apellido del alumno es {alumno["apellido"]} y su nombre es {alumno["nombre"]}")
  
llamar_alumno(apellido = "Suarez",nombre = "Fernan")

def llamar_alumno2(*alumno):
  print(type(alumno))
  print(alumno)
  print(f"El apellido del alumno es {alumno[0]} y su nombre es {alumno[1]}")
  
llamar_alumno2("Suarez","Fernan")

def suma(a,b):
  return a + b

print(suma(1,2))

"""
Recursión
"""

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
print(factorial(5))

