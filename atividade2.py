def perceptron_aspirador_inteligente(piso, sujeira, distancia):
    pisos = {"madeira": 0.5, "ceramica": 1.0, "carpete": 0.2}
    piso_valor = pisos.get(piso.lower(), 0.5)

    sujeira_nivel = sujeira / 10       
    distancia_nivel = distancia / 5    

    potencia = round(1 + 2 * sujeira_nivel)  

    velocidade = round(1 + 4 * ((piso_valor * 0.6) + (distancia_nivel * 0.4)))
    velocidade = max(1, min(5, velocidade))

    return potencia, velocidade

print(perceptron_aspirador_inteligente("madeira", 6, 4))  
print(perceptron_aspirador_inteligente("ceramica", 10, 2))
print(perceptron_aspirador_inteligente("carpete", 3, 1))
