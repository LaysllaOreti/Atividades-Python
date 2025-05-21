lista_produtos = []
lista_precos = []

for i in range(1,6):
    produtos = str(input(f"Adicione o produto: "))
    lista_produtos.append(produtos)
    
    precos = float(input(f"Digite o preço do {i} produto: R$"))
    lista_precos.append(precos)
    
soma_preco = sum(lista_precos)
print(f"Os produtos listados são: {lista_produtos}")
print(f"O preço dos produtos é igual a: {lista_precos}")
print(f"A soma total dos preços dos produtos é: {soma_preco}")