#Entrada de dados

nome_pessoa1 = input("Para a primeira pessoa, digite o seu nome: ")
idade_pessoa1= float(input("Para a primeira pessoa, digite a sua idade: "))

nome_pessoa2 = input("Para a segunda pessoa, digite o seu nome: ")
idade_pessoa2 = float(input("Para a segunda pessoa, digite a sua idade: "))

#Cálculo média
media = (idade_pessoa1 + idade_pessoa2) /2

#Saída dos dados
print(f"O nome da primeira pessoa é {nome_pessoa1},\n e o nome da segunda pessoa é {nome_pessoa2}.\n A média entre as suas idades é: {media: .1f}")
