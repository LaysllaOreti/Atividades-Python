def operacao():
    contador = 60 #variável local
    contador += 2
    return contador

print(operacao()) #agora o valor retornado foi 62

# print - ele só vai imprimir o valor, mostrar o resultado
# return - você consegue reutilizar ela, ele fica armazenado

# função não recursiva - ela não se repete
# função recursiva - que repete infinitamente, ela retorna nela própria