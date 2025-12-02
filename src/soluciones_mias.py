def invierte_cadena(texto) -> str:
    inv = ''
    for c in texto:
        inv = c + inv
    return inv

def es_palindromo(texto, ignora_espacios, ignora_mayusculas):
    
    if ignora_espacios:
        texto = texto.replace(" ", "")

    if ignora_mayusculas:
        texto = texto.lower()

    palindromo = False
    if texto == invierte_cadena(texto):
        palindromo = True
    return palindromo
    
def estiliza_mensaje(texto, alterna_may_min = True, usa_dieresis = False, sustituye_espacios = " ") -> str | bool | bool | str:
    if alterna_may_min:
        contador = 0
        alternado = ""
        for c in texto:
            if c.isalpha():
                contador += 1
                if contador % 2 != 0:
                    alternado = alternado + c.upper() 
                elif contador % 2 == 0:
                    alternado = alternado + c.lower() 
            else:
                alternado = alternado + c
            
        return alternado
 
    if usa_dieresis:
        texto_dieresis = ""
        for c in texto:
        
            if c.lower() == "a":
                texto_dieresis = texto_dieresis+"ä"
            elif c.lower() == "e":
                texto_dieresis = texto_dieresis+"é"
            elif c.lower() == "i":
                texto_dieresis = texto_dieresis+"ï"
            elif c.lower() == "o":
                texto_dieresis = texto_dieresis+"ö"
            elif c.lower() == "u":
                texto_dieresis = texto_dieresis+"ü"
            else:
                texto_dieresis = texto_dieresis + c
        return texto_dieresis
    
    if sustituye_espacios != "":
        texto_espacios = ""
        for c in texto:
            if c == " ":
                h = texto.replace(c, sustituye_espacios)
                texto_espacios = texto_espacios + h
        return texto
    #está mal, no se puede usar un return en cada uno porque queremos poder aplicar las 3 funciones al mismo texto 
    
