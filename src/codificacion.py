def cifra_cesar(texto: str, clave: int): 
    
    def letra_a_posicion(letra):
        if not letra.isalpha():
            return
        alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
        return alfabeto.index(letra)
    
    def posicion_a_letra(posicion):
        alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
        if posicion > len(alfabeto):
            return
        return alfabeto[posicion]
    res = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    for caracter in texto:
        if caracter.isalpha():
            nueva_letra = posicion_a_letra(
                (letra_a_posicion(caracter) + clave) % len(alfabeto)
                                           )
            res += nueva_letra
        else:
            res += caracter
    return res
        
def rompe_cesar(msj_cifrado):
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    opciones = len(alfabeto) - 1
    for i in range(opciones):
        print(cifra_cesar(msj_cifrado, -i))

rompe_cesar("j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!") #a programar se aprende programando!
