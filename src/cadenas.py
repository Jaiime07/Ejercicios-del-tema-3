def invierte_cadena(texto) -> str:
    invertido = ""
    for i in range(len(texto)-1, -1, -1):
        invertido = invertido + texto[i]
    return invertido




#def es_palindromo(texto, ignora_espacios, ignora_mayusculas):
    
   
    
#def estiliza_mensaje(texto, alterna_may_min = True, usa_dieresis = False, sustituye_espacios = " ") -> str | bool | bool | str: