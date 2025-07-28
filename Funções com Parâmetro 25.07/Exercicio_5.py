def contar_palavras_com_a(lista):
    contador = 0
    for palavra in lista:
        if palavra.lower().startswith('a'):
            contador += 1
    return contador

print("Por favor, digite as palavras separadas por espaço:")
entrada = input()
palavras = entrada.split()

quantidade = contar_palavras_com_a(palavras)

print(f"A quantidade de palavras que começam com a letra 'a': {quantidade}")
