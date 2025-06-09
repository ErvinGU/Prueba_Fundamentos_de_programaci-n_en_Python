from preguntas import pool_preguntas

def print_pregunta(enunciado, alternativas):
 
    print(f"\n{enunciado}\n")  

    letras = ["A", "B", "C", "D"]  
    for idx, alternativa in enumerate(alternativas):
        print(f"{letras[idx]}. {alternativa[0]}") 


if __name__ == "__main__":
    nivel = "basicas" 
    pregunta_n = 1  

    enunciado = pool_preguntas[nivel][pregunta_n]["enunciado"]
    alternativas = pool_preguntas[nivel][pregunta_n]["alternativas"]

    print_pregunta(enunciado, alternativas)

