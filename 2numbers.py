#int
numero_entero = 5
#float
numero_decimal = 5.2
#complex
numero_complejo = -5 + 2j

# print(type(numero_entero))
# print(type(numero_decimal))
# print(type(numero_complejo))

"""
===============================================
Casting
===============================================
"""
decimal_desde_entero = float(numero_entero)
# print(decimal_desde_entero)
entero_desde_decimal = int(numero_decimal)
# print(entero_desde_decimal)

import random
aleatorio = random.randrange(1,10)
aleatorio_par = random.randrange(1,10,2)
aleatorio_impar = random.randrange(2,10,2)
print(aleatorio_impar)