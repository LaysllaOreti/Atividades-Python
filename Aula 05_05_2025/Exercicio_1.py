#Entrada de dados
import math

base = int(input("Digite o tamanho da base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

#Cálculos
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"A área desse retângulo é {area: .4f}, o perímetro é igual a {perimetro: .4f} e a diagonal é {diagonal: .4f}")