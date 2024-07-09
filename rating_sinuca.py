import os

# Nome do arquivo de ratings
arquivo_ratings = 'Rating_Jogadores.txt'

# Função para ler os ratings dos jogadores do arquivo
def ler_ratings():
    ratings = {}
    if os.path.exists(arquivo_ratings):
        with open(arquivo_ratings, 'r') as f:
            for linha in f:
                dados = linha.strip().split()
                jogador = ' '.join(dados[:-1])
                rating = int(dados[-1])
                ratings[jogador] = rating
    return ratings

# Função para escrever os ratings atualizados no arquivo
def escrever_ratings(ratings):
    with open(arquivo_ratings, 'w') as f:
        for jogador in sorted(ratings):
            f.write(f"{jogador} {ratings[jogador]}\n")

# Função para calcular o novo rating após um jogo
def calcular_novo_rating(rating1, rating2, resultado, tipo_jogo, K=8):
    # Probabilidade esperada de vitória do jogador 1
    esperada1 = 1 / (1 + 10 ** ((rating2 - rating1) / 200))
    # Probabilidade esperada de vitória do jogador 2
    esperada2 = 1 - esperada1

    # Ajuste do K baseado na diferença de partidas
    if tipo_jogo == 3:
        if resultado == 2:  # Vitória por 2-0
            K_factor = 5.0
        else:  # Vitória por 2-1
            K_factor = 3.0
    elif tipo_jogo == 5:
        if resultado == 3:  # Vitória por 3-0
            K_factor = 8.0
        elif resultado == 2:  # Vitória por 3-1
            K_factor = 6.0
        else:  # Vitória por 3-2
            K_factor = 5.0
    elif tipo_jogo == 7:
        if resultado == 4:  # Vitória por 4-0
            K_factor = 18.0
        elif resultado == 3:  # Vitória por 4-1
            K_factor = 14.0
        elif resultado == 2:  # Vitória por 4-2
            K_factor = 12.0
        else:  # Vitória por 4-3
            K_factor = 10.0
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

# Função para atualizar os ratings com base nos resultados dos jogos
def atualizar_ratings(resultados):
    if not resultados:
        return  # Se a lista de resultados estiver vazia, não faz nada

    ratings = ler_ratings()
    for jogador1, jogador2, resultado, tipo_jogo in resultados:
        if jogador1 not in ratings:
            ratings[jogador1] = 950
        if jogador2 not in ratings:
            ratings[jogador2] = 950
        rating1 = ratings[jogador1]
        rating2 = ratings[jogador2]
        novo_rating1, novo_rating2 = calcular_novo_rating(rating1, rating2, resultado, tipo_jogo)
        ratings[jogador1] = novo_rating1
        ratings[jogador2] = novo_rating2
    escrever_ratings(ratings)

# Função para exibir os ratings em ordem alfabética e por pontuação
def exibir_ratings(ratings):
    print("Ordem Alfabética:")
    for jogador in sorted(ratings):
        print(f"{jogador}: {ratings[jogador]}")
    
    print("\n" + "-"*30 + "\n")
    
    print("Ordem de Pontuação:")
    for jogador, rating in sorted(ratings.items(), key=lambda item: item[1], reverse=True):
        print(f"{jogador}: {rating}")

# Exemplo de resultados: [(jogador1, jogador2, resultado, tipo_jogo), ...]
# resultado é a diferença de partidas ganhas (ex: 2 para 2-0 em melhor de 3, 1 para 3-2 em melhor de 5)
resultados_exemplo = [
    ('White', 'Dornellas', 1, 1),
    ('PT', 'White', 1, 1),
    ('PT', 'Dornellas', 1, 1),
    ('White', 'Lulu', 1, 1),
    ('Lulu', 'White', 1, 1),
    ('Vanderley', 'Lulu', 1, 1),
    ('Moises', 'Vanderley', 1, 1),
    ('Moises', 'MT', 1, 1),
    ('Moises', 'Iam', 1, 1),
    ('Moises', 'Iam', 1, 1),
    ('Vanderley', 'Iam', 1, 1)
]

# Executar as funções
atualizar_ratings(resultados_exemplo)

# Exibir os ratings atualizados
ratings_atualizados = ler_ratings()
exibir_ratings(ratings_atualizados)