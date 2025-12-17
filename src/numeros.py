def invierte_numero(n):
    invertido = 0
    while n != 0:
        nueva_primera = n % 10
        n //= 10
        invertido =  invertido*10 + nueva_primera
    return invertido
    
def convierte_binario(n:int):
    resultado = "" 
    while n > 0:
        bit = n % 2
        resultado = str(bit) + resultado
        n = n // 2
    if n == 0 and resultado == "":
        resultado = "0" 
    return resultado

def sumar_divisores_propios(n:int):
    suma = 0
    for i in range(1,n):
        if n % i == 0: #si es un divisor
            suma += i
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

def busca_perfecto(n):
    numero = 0
    contador = 0
    while True:
        if clasifica_numero(numero) == "Perfecto":
            if contador == n:
                return numero
            else:
                contador +=1
        numero += 1
                
