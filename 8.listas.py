"""
Colleccition ordenada y mutable
"""

frutas = ["Naranja","Manzana","Pera"]
# print(len(frutas))  

lista_desde_constructor = list(("Hola","que","tal"))
# print(lista_desde_constructor)

naranja = frutas[0]
otros = frutas[1:3]
otross = frutas[-2:-2]
# print(otross)

tecnologias = ["python","Django","Flask","Reactpy","Pandas"]
tecnologias[3] = "TensorFlow"
tecnologias.insert(2,"Scrapy")
tecnologias.append("Scrapy2")

frontend = ["Angular","React","Vue"]
diccionario =  {"nombre":"Joe Doe"}

tecnologias.extend(frontend)
tecnologias.extend(diccionario)

tecnologias.remove("Vue")
tecnologias.pop()
del tecnologias[7]
# tecnologias.clear()

# for tecnologia in tecnologias:
#   print(tecnologia)
  
# for i in range(len(tecnologias) - 1):
#   print(tecnologias[i])

#List comprenhention
# [print(tecnologia) for tecnologia in tecnologias]

listConY = []

for tecnologia in tecnologias:
  if "y" in tecnologia:
    listConY.append(tecnologia)
    
listConY2 = [tecnologia.upper() for tecnologia in tecnologias if "y" in tecnologia]

#ordenar lista
tecnologias.sort()
numeros = [9,7,8,4,2]
numeros.sort(reverse=True)
tecnologias.reverse()
# print(numeros)
# print(tecnologias)

#copiar una lista
meses = ["enero","febrero","marzo"]
copia_meses = meses.copy()
copia_meses2 = list(meses)

meses[0] = "January"
# print(copia_meses + copia_meses2)