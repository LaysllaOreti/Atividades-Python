'''var1 = 10
var2 = 1.1
var3 = "Hoje vai ser um bom dia!"
var4 = True

print("\nTipos de variáveis")
print(f"Tipo: {type(var1)}")
print(f"Tipo: {type(var2)}")
print(f"Tipo: {type(var3)}")
print(f"Tipo: {type(var4)}")

#Testando END - final do print
print("\nEnd")
print("Layslla e Daniel", end="S2")

#Testando o SEP - substituição de vírgulas
print("\nSEP")
print("Python", "Layslla", sep="--------")

cor = input("Escolha uma cor: ")
print(f"A cor é: {cor}")

altura = float(input("Digite a sua altura: "))
print(f"Sua altura é: {altura: .2f}")

numero = int(input("Insira um número: "))
print(f"O número escolhido foi: {numero})'''

#Entrada de dados - INPUT
largura = float(input("Digite o valor da largura: "))
comprimento = float(input("Digite o valor do comprimento: "))
valor = float(input("Digite o valor do metro quadrado: "))

#Lógica
area = largura * comprimento
preco = area * valor

#Saída dos dados
print(f"A área do terreno é de: {area: .2f} e o preço é: {preco: .2f}")