
def verificar(alternativas, eleccion):
    letras = ["A", "B", "C", "D"]
    indice = letras.index(eleccion.upper()) if eleccion.upper() in letras else -1

    if indice == -1 or indice >= len(alternativas):
        print("Opción inválida.")
        return False

    if alternativas[indice][1] == 1:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False







