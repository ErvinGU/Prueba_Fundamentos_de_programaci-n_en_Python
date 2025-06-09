
def validate(opciones, eleccion):
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {', '.join(opciones)}")
        eleccion = input("Ingrese una opción válida: ").strip()
    return eleccion

if __name__ == "__main__":
    opciones_validas = ["1", "2", "3"]
    eleccion_usuario = input("Ingrese una opción (1, 2, 3): ").strip()
    resultado = validate(opciones_validas, eleccion_usuario)
    print(f"Opción seleccionada: {resultado}")

    
    
