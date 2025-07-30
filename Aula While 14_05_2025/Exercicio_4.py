numero = int(input("Digite um número:"))
fatorial = 1
i = numero #Começa no número digitado

while i > 1:
    fatorial *= i
    i -= 1 #Vai diminuindo até chegar em 1

print(f"Fatorial de {numero} é {fatorial}")
