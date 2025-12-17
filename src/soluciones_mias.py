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

    res = texto
    cont_alterna = 0
    
    if usa_dieresis:
        for c in res:
            if c == 'a':
                res.replace(c, 'ä')
            elif c == 'e':
                res.replace(c, 'ë')
            elif c == 'i':
                res.replace(c, 'ï')
            elif c == 'o':
                res.replace(c, 'ö')
            elif c == 'u':
                res.replace(c, 'ü')

    if alterna_may_min:
        for c in res:
            if c.isaplha() and not cont_alterna % 2 == 0:
                res.replace(c, c.upper())
            elif c.isaplha() and cont_alterna % 2 == 0:
                res.replace(c, c.lower())        

    if sustituye_espacios != " " and sustituye_espacios:
        res.replace(" ", sustituye_espacios )
    
    return res



