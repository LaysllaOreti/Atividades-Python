def encontrar_maior_elemento(lista):
    if not lista:
        return None
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

print("Digite os elementos da lista separados por espaço:")
entrada = input()
lista = list(map(int, entrada.split()))

maior = encontrar_maior_elemento(lista)

if maior is not None:
    print(f"O maior elemento da lista é: {maior}")
else:
    print("A lista está vazia. Não há elementos para comparar.")
