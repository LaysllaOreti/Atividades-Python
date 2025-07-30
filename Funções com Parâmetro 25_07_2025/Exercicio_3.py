def contar_caractere(texto, caractere):
    contador = 0
    for c in texto:
        if c == caractere:
            contador += 1
    return contador

print("Digite uma string:")
texto = input()

print("Digite o caractere que deseja contar:")
caractere = input()

if len(caractere) != 1:
    print("Erro: você deve digitar apenas um caractere.")
else:
    quantidade = contar_caractere(texto, caractere)
    print(f"O caractere '{caractere}' aparece {quantidade} vezes na string.")
