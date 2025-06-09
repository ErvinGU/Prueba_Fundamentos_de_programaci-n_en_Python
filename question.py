
import random
from shuffle import shuffle_alt
from preguntas import pool_preguntas

def choose_q(dificultad):
    if dificultad not in pool_preguntas:
        raise ValueError("Nivel de dificultad inválido")

    preguntas_disponibles = pool_preguntas[dificultad]
    if not preguntas_disponibles:
        raise ValueError("No quedan preguntas disponibles en este nivel")

    pregunta_n = random.choice(list(preguntas_disponibles.keys()))
    pregunta_seleccionada = preguntas_disponibles.pop(pregunta_n)

    enunciado = pregunta_seleccionada["enunciado"]
    alternativas_mezcladas = shuffle_alt(pregunta_seleccionada)

    return enunciado, alternativas_mezcladas
