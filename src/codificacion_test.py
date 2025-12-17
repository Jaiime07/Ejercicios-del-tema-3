from codificacion import cifra_cesar

def test_cifra_cesar():
    assert cifra_cesar("Hola Mundo", 1) == "Ipmb Nvñep"
    assert cifra_cesar("Hola Mundo", 13) == "Téxn YBzpé"
    assert cifra_cesar("Hola Mundo", 66) == "Hola Mundo"


print("Probando cifra_cesar...")
test_cifra_cesar()
print("Todo OK")