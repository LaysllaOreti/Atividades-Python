quantidade_numeros = int(input("Digite a quantidade de números que você deseja inserir na lista: "))
numeros = []

#receber o número do usuário
i = 0
while i < quantidade_numeros:
    numero = float(input(f"Digite um número: "))
    numeros.append(numero)
    i += 1
    
numero_especifico = float(input("Digite o número que deseja verificar: "))

#vai verificar se o número em específico está na lista
i = 0
especifico = False

while i <len(numeros):
    if numeros[i] == numero_especifico:
        especifico = True
        break
    i += 1
    
if especifico:
    print("O número está presente nessa lista!")
else: 
    print("O número não está presente nessa lista!")