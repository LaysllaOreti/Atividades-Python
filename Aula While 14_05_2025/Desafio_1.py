maior = 0  # Guardar o maior palíndromo e os dois números que geram ele
num1 = 0
num2 = 0

contador = 999  # Começamos o contador com o maior número de 3 dígitos
while contador >= 100:
    contador_2 = contador  # Usado para não repetir números
    while contador_2 >= 100:
        resultado = contador * contador_2
        resultado_str = str(resultado)

        if resultado_str == resultado_str[::-1]:  # Verifica se é palíndromo
            if resultado > maior:
                maior = resultado
                num1 = contador
                num2 = contador_2
        contador_2 -= 1
    contador -= 1

print(f"Maior palíndromo de dois números com 3 dígitos é {maior} = {num1} x {num2}")
