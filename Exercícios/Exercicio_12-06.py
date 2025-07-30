#itertools é um módulo do Python que oferece várias funções que geram iteradores eficientes
import itertools

flores = {
    "Rosas Vermelhas": 145,
    "Girassóis": 125,
    "Margaridas": 120,
    "Flores do Campo": 140
}

presentes = {
    "Urso de Pelúcia": 55,
    "Caixa de Bombom": 60,
    "Colar": 75,
    "Roupas": 40
}

lugares = {
    "Praia": 70,
    "Sair para Jantar": 150,
    "Parque de Diversões": 120,
    "Hotel": 180
}

#gerar todas as combinações possíveis
combinacoes = list(itertools.product(flores.items(), presentes.items(), lugares.items()))

#criar lista com a combinação e o preço total
valores_combinacoes = []

for flor, presente, lugar in combinacoes:
    total = flor[1] + presente[1] + lugar[1]
    valores_combinacoes.append(((flor[0], presente[0], lugar[0]), total))

#ordenar pela soma dos preços
valores_combinacoes.sort(key=lambda x: x[1])

#combinação mais barata, mais cara e média
combinacao_barata = valores_combinacoes[0]
combinacao_cara = valores_combinacoes[-1]
media_index = len(valores_combinacoes) // 2
media = valores_combinacoes[media_index]

#imprimir os resultados
print("A combinação mais barata é:")
print(f"{combinacao_barata[0]} - Valor Total: R${combinacao_barata[1]:.2f}\n")

print("A combinação mais cara é:")
print(f"{combinacao_cara[0]} - Valor Total: R${combinacao_cara[1]:.2f}\n")

print("A combinação média é:")
print(f"{media[0]} - Total: R${media[1]:.2f}")
