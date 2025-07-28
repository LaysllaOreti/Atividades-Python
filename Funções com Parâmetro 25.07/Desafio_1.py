def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

lista_termos = []

def gerar_lista(n, lista_termos, indice=0):
    if indice == n:
        print(lista_termos)
        return

    lista_termos.append(fibonacci(indice))
    gerar_lista(n, lista_termos, indice + 1)

n = int(input("Digite o número de termos da sequência Fibonacci que você deseja: "))

gerar_lista(n, lista_termos)
