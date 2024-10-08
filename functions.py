def calcular_novo_rating(rating1, rating2, resultado, tipo_jogo, K=8):
    # Probabilidade esperada de vitória do jogador 1
    esperada1 = 1 / (1 + 10 ** ((rating2 - rating1) / 200))
    # Probabilidade esperada de vitória do jogador 2
    esperada2 = 1 - esperada1

    # Ajuste do K baseado na diferença de partidas
    if tipo_jogo == 3:
        if resultado == 2:  # Vitória por 2-0
            K_factor = 6.0
        else:  # Vitória por 2-1
            K_factor = 3.0
    elif tipo_jogo == 5:
        if resultado == 3:  # Vitória por 3-0
            K_factor = 12.0
        elif resultado == 2:  # Vitória por 3-1
            K_factor = 7.0
        else:  # Vitória por 3-2
            K_factor = 5.0
    elif tipo_jogo == 7:
        if resultado == 4:  # Vitória por 4-0
            K_factor = 18.0
        elif resultado == 3:  # Vitória por 4-1
            K_factor = 14.0
        elif resultado == 2:  # Vitória por 4-2
            K_factor = 10.0
        else:  # Vitória por 4-3
            K_factor = 8.0
    else:
        K_factor = 1.0

    # Ajuste do resultado
    resultado1, resultado2 = 1, 0

    # Ajuste do K baseado nos ratings
    if rating1 > 2000:
        K1 = K * K_factor / 2
    elif rating1 < 800:
        K1 = K * K_factor * 2
    else:
        K1 = K * K_factor

    if rating2 > 2000:
        K2 = K * K_factor / 2
    elif rating2 < 800:
        K2 = K * K_factor * 2
    else:
        K2 = K * K_factor

    # Cálculo do novo rating
    if K1 * (resultado1 - esperada1) < 1 and rating1 > rating2:
        novo_rating1 = rating1 + 1
        novo_rating2 = rating2 - 1
    else:
        novo_rating1 = rating1 + K1 * (resultado1 - esperada1)
        novo_rating2 = rating2 + K2 * (resultado2 - esperada2)

    return round(novo_rating1), round(novo_rating2)

