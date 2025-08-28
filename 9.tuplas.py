#Colección ordenada e inmutable de elementos

tupla = ("a" , "b" , "c" )
vehiculos =("bicicleta","moto","auto","camioneta","avion","barco")

longitud = len(vehiculos)
print(type(longitud))

lista_vehiculos = list(vehiculos)
print(lista_vehiculos)

(a,b,c,d,e,f) = vehiculos
(bici,moto,*cuatroruedad,avion,barco,crucero) = vehiculos


print(a)
print(b)
print(c)
print(cuatroruedad)

#join tuplas
citricos = ("naranja","limon","pomelo")
tropical1 = ("papaya","coco")

frutas = citricos + tropical1
dobleCitrico = citricos * 2

print(dobleCitrico)