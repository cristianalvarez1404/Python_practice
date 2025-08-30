#dict => Colección de pares clave-valor - key:value desordenada y mutable
diccionario = {
  "nombre" : "Code",
  "apellido":"amazing",
  "edad":1000
}

new_dict = dict(nombre = "cristian", lenguage = "Python")
# print(diccionario)
# print(len(diccionario))
# print(type(diccionario))
# print(new_dict)
# print(diccionario["apellido"])
# print(diccionario["nombre"])
# print(diccionario.get("nombre"))
# print(diccionario.values())
# print(list(diccionario.keys())[2])

items = diccionario.items()
# print(items)
# print(type(items))

# if "nombre" in diccionario:
#   print("Si")
# else:
#   print("no")

diccionario["nombre"] = ["cristian CODE"]
diccionario["apellido"] = "CODING"
diccionario.update({"direccion":"CR 5","nombre":"andres"})
diccionario["profesion"] = "Software developer"

# diccionario.pop("profesion")
# diccionario.popitem()
del diccionario["profesion"]

curso_python = {
  "nombre":"Python lo mejor",
  "duracion":10,
  "dificultad":"pro"
}

# for key,value in curso_python.items():
#   print(value)
  
# for key in curso_python:
#   print(curso_python[key])
  
# for key in curso_python.values():
#   print(key)
  
copia = curso_python.copy()
copia2 = dict(curso_python)
print(copia)

hijo1 = {
  "nombre":"Pedro",
  "edad":5
}

hijo2 = {
  "nombre":"Alan",
  "edad":7
}

hijo3 = {
  "nombre":"Enzo",
  "edad":9
}

familia = {
  "hijo1":hijo1,
  "hijo2":hijo2,
  "hijo3":hijo3,
}

print(familia["hijo1"]["nombre"])

for x,y in familia.items():
  for z,hijo in y.items():
    print(hijo) 