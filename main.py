
from validador import validate
from level import choose_level
from question import choose_q
from shuffle import shuffle_alt
from print_preguntas import print_pregunta
from verify import verificar
from preguntas import pool_preguntas

def main():
    print("Bienvenido a la trivia interactiva")
    
    inicio = validate(["1", "0"], input("Presione 1 para comenzar o 0 para salir: ").strip())
    if inicio == "0":
        print("Nos vemos pronto!")
        return

    preguntas_por_nivel = int(validate(["1", "2", "3"], input("Ingrese la cantidad de preguntas por nivel (1, 2 o 3): ").strip()))
    puntaje = 0

    for n_pregunta in range(1, preguntas_por_nivel * 3 + 1):
        nivel = choose_level(n_pregunta, preguntas_por_nivel)

        if not pool_preguntas[nivel]:
            print(f"No quedan más preguntas en el nivel {nivel}.")
            continue

        enunciado, alternativas = choose_q(nivel)

        alternativas_mezcladas = shuffle_alt({"alternativas": alternativas})
        print_pregunta(enunciado, alternativas_mezcladas)

        eleccion_usuario = validate(["A", "B", "C", "D"], input("Seleccione una opción (A, B, C, D): ").strip().upper())

        if verificar(alternativas_mezcladas, eleccion_usuario):
            puntaje += 1

    print(f"\nTrivia finalizada. Puntaje: {puntaje}/{preguntas_por_nivel * 3}")

    continuar = validate(["1", "0"], input("\n¿Quieres jugar otra vez? (1: Sí, 0: No): ").strip())
    if continuar == "1":
        main()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()


            
