#Funciones lambdas => Funciones anónimas y cortas

example =  lambda x : x + 2
example1 =  lambda x : x - 2
example2 =  lambda x : x * 2
example3 =  lambda x : x // 2

print(example(5))
print(example1(5))
print(example2(5))
print(example3(5))

def multiplicador(n):
  return lambda x : x * n 

funcion2 = multiplicador(5)
print(funcion2(5))

numeros = [0,1,2,3,4,5,6,7,8,9]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)