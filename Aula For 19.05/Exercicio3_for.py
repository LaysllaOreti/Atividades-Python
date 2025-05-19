quantidade_numeros = int(input("Digite a quantidade de números que deseja multiplicar: "))
numeros = []

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o número {i + 1}"))
    numeros.append(numero)
    
multiplicacao = 0
for numero in numeros:
    multiplicacao += numero
    
print(f"A multiplicação dos números é igual a: {multiplicacao}")