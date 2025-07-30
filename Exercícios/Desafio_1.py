herois = {
    'Capitão América': 100,
    'Viúva Negra': 98,
    'Homem de Ferro': 99,
    'Thor': 120,
    'Feiticeira Escarlate' : 145
}

armas = {
    'Escudo do Capitão América': 320,
    'Mordida': 140,
    'Armadura do Homem de Ferro': 300,
    'Mjolnir': 580,
    'Magia' : 890
}

viloes = {
    'Caveira Vermelha ': 80,
    'Treinador (Taskmaster)': 78,
    'Thanos': 79,
    'Gorr': 100,
    'Magneto ' : 125
}

print("Heróis disponíveis:")
for nome in herois:
    print(f"O(a) {nome} (Poder: {herois[nome]})")

print("\nArmas disponíveis:")
for nome in armas:
    print(f"A {nome} (Poder: {armas[nome]})")

print("\nVilões disponíveis:")
for nome in viloes:
    print(f"O {nome} (Poder: {viloes[nome]})")

# Entradas do usuário
heroi_escolhido = input("\nEscolha um herói: ")
arma_escolhida = input("Escolha uma arma: ")
vilao_escolhido = input("Escolha um vilão: ")

# Validação
if heroi_escolhido not in herois:
    print("Herói inválido.")
elif arma_escolhida not in armas:
    print("Arma inválida.")
elif vilao_escolhido not in viloes:
    print("Vilão inválido.")
else:
    poder_heroi = herois[heroi_escolhido] + armas[arma_escolhida]
    poder_vilao = viloes[vilao_escolhido]

    print(f"\n{heroi_escolhido} (com {arma_escolhida}) tem poder total de {poder_heroi}")
    print(f"{vilao_escolhido} tem poder de {poder_vilao}")

    if poder_heroi > poder_vilao:
        print(f"\nO(a) {heroi_escolhido} a batalha venceu usando a arma {arma_escolhida}!")
    elif poder_heroi < poder_vilao:
        print(f"\nO {vilao_escolhido} venceu a batalha!")
    else:
        print("\nA batalha terminou em empate!")
