# Código Python para verificar si un número es par o impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 7
if es_par(numero):
    print("El número es par")
else:
    print("El número es impar")
