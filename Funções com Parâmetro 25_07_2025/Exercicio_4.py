def calcular_media(lista):
    if not lista:
        return None
    soma = sum(lista)
    media = soma / len(lista)
    return media

print("Por favor, digite os números separados por espaço:")
entrada = input()
lista = list(map(float, entrada.split()))

media = calcular_media(lista)

if media is not None:
    print(f"A média aritmética é: {media}")
else:
    print("A lista está vazia. Não é possível calcular a média.")
