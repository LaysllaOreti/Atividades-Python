numero = int(input("Digite um número:"))
lista_divisor = []

for i in range(1, numero + 1):
    if numero % i == 0:
        lista_divisor.append(i)
        print(lista_divisor)

soma = sum(lista_divisor)
print(f"A soma dos divisores é igual a: {soma}")
