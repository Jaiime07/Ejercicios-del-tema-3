def invierte_cadena(texto) -> str:
    
    invertido = ""
    for i in range(len(texto)-1, -1, -1):
        invertido = invertido + texto[i]
    return invertido
   

def es_palindromo(texto, ignora_espacios = False, ignora_mayusculas =False ):
    inverso = invierte_cadena(texto)
    if ignora_espacios:
        texto = str(c for c in texto if c != " ")
        inverso = str(c for c in inverso if c != " ")
    if ignora_mayusculas:
        texto = texto.lower()
        inverso = inverso.lower()
    if texto == inverso:
        return True
    else:
        return False

                
def estiliza_mensaje(texto, alterna_may_min = True, usa_dieresis = False, sustituye_espacios = " ") -> str | bool | bool | str:
    