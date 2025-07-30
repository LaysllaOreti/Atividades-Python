ano = int(input("Digite o ano que desejar verificar:"))

bissexto = ano % 100 == 0 and ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0

if bissexto:
    print("Ano bissexto")
else:
    print("Ano não é bissexto")