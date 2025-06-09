def choose_level(n_pregunta, preguntas_por_nivel):
    niveles = ["basicas", "intermedias", "avanzadas"]
    
    if preguntas_por_nivel == 1:
        return niveles[0]
    elif preguntas_por_nivel == 2:
        if n_pregunta in [1, 2]: return niveles[0]
        elif n_pregunta in [3, 4]: return niveles[1]
        elif n_pregunta in [5, 6]: return niveles[2]
    elif preguntas_por_nivel == 3:
        if n_pregunta in [1, 2, 3]: return niveles[0]
        elif n_pregunta in [4, 5, 6]: return niveles[1]
        elif n_pregunta in [7, 8, 9]: return niveles[2]

    return "Nivel desconocido"
