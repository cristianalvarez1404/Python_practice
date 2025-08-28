### CONDICIONALES => if, elif, else

#Estructura que nos permite tomar el flujo u otro según una condición

a = 5
b = 8
c = 7

if a > b:
  print(f"{a} es mayor que {b}")
elif c > b:
  print(f"{c} es mayor que {b}")
else:
  print(f"{a} es menor que {b} y {c} es menor que {b}")  
  
"""
  Ejemplo
"""

edad = 17

if edad > 18 and edad < 60:
  print("Puedes entrar al boliche")
else:
  print("No puedes entrar al boliche")
  
#SHORTCUTS

if edad > 17: print("mayor de edad")
print("Hola") if edad else print("Hola mundo") 

