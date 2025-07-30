lista = []

fim = int(input("Digite o número que deseja verificar:"))
contador = 2


for i in range(2, fim +1):
   lista.append(i)

while contador <= fim ** 0.5:
    for i in lista:
        if i % contador == 0 and i != contador:
            lista.remove(i)
    contador += 1


if i in lista:
    print(f"Número {i} é primo")
else:
    print(f"Número {i} não é primo")
