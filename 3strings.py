##### string

cadena = "cadena"
cadena2 = "c,a,d,e,n,a"
print(type(cadena))

caracter = cadena[2]
print(caracter)

#len() => longitd
print(len(cadena))

#in => incluir
print('Ca'.lower() in  cadena.lower())

#not in => no incluido
print('Ca'.lower() not in  cadena.lower())

#Slice-cortar una parte del texto
print(cadena[1:5])
print(cadena[:5])

#mayusculas
print(cadena.upper())

#minusculas
print(cadena.lower())

#remover espacios comienzo y final
print(cadena.strip())

#remplazo
print(cadena.replace("ca","ko"))

#separar por caracteres
print(type(cadena2.split(",")))

#concatenar
print(cadena + cadena2)

#f-strings
print(f"{cadena} y {cadena2}")
num = 2
print(f"{num:.2f}")

resultado = f"El resultado de 69 - 75 es => {69 * 75}"
print(resultado)

escape = "Mi pais favorito es \"Lituania\""
salto_linea = "Saldo de linea \n otra linea"
print(salto_linea)