#SET => Colección desordenada de elementos únicos y mutables

# conjunto = {1,1,2,2,3,True,"Hola"}
# conjunto[1] = 6 No puede modificarlo
# print(conjunto)
# longitud = len(conjunto)
# print(type(conjunto))
constructor = set(("Este","es","un","conjunto"))
# print(constructor)

# if "es" in constructor:
#   print("si esta")
  
# if "python" not in constructor:
#   print("python no esta")
  
telefonos = {"Xioami","Samsug","Motorola"}
telefonos2 = {"Huawai","Oneplus"}
telefonos.add("Apple")
telefonos.update(telefonos2)

autos = {"Ford","Paugeot","Fiat","Renault","Ferrari"}

autos.remove("Ferrari")
autos.discard("Fiat")

autos.pop()

# print(telefonos)
# print(autos)

#Join de conjunto

a = {1,2,3,4,5}
b = {1,3,5,7,9}

#union
u = a.union(b)
u2 = a | b

# print(d)

#Intersección: va a devolver elementos en común

i = a.intersection(b)
i2 = a & b
# a.intersection_update(b) #Modifica el conjunto original
# print(a)

#Diferencia => elementos diferentes
d = a.difference(b)
d2 = a - b
print(d)

#Diferencia simétrica: 
ds = a.symmetric_difference(b)
ds2 = a ^ b
print(ds)