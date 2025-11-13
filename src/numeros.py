def invierte_numero(n):
    while n != 0:
        nueva_primera = n // 10
        n = n % 10
        invertida = n + nueva_primera
         

def convierte_binario(n:int):
    resultado = "" 
    while n > 0:
        bit = n % 2
        resultado = str(bit) + resultado
        n = n // 2
    if n == 0 and resultado == "":
        resultado = "0" + resultado
    return resultado

def sumar_divisores_propios(n:int):
    suma = 0
    for i in range(1,n):
        if n % i == 0: #es un divisor
            suma += 1
    return suma  

def clasifica_numero(n:int):
    suma = sumar_divisores_propios(n)
    if n == suma:
        return "Perfecto"
    elif n < suma:
        return "Abundante"
    else:
        return "Deficiente"

def clasifica_rango(n:int):
    for i in range(1, n+1):
        print(f"{i}: {clasifica_numero(i)}")

def busca_perfecto():
    numero = 0
    contador = 0
    if clasifica_numero(numero) == "Perfecto":
        contador +=1