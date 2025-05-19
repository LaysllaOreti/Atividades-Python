def contador_vogais(palavra):
    vogais = "aeiouAEIOU"
    contagem_vogais = 0
    for letra in palavra:
        if letra in vogais:
            contagem_vogais += 1
    return contagem_vogais

quantidade_palavras = int(input("Quantas palavras deseja digitar? "))

palavras = []

i = 0
while i < quantidade_palavras:
    palavra = input(f"Digite a palavra {i + 1}: ")
    palavras.append(palavra)
    i += 1

total_vogais = 0
i = 0
while i < len(palavras):
    total_vogais += contador_vogais(palavras[i])
    i += 1

print(f"O total de vogais é: {total_vogais}")
