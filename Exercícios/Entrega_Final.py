# Importa o módulo sys para utilizar o sys.exit() caso precise encerrar o programa
import sys

#lista com os nomes dos jogos disponíveis
jogos = ["GTA V", "The Last Of Us - Part II", "Minecraft", "God Of War Ragnarök", "Hogwarts Legacy", "It Takes Two"]

#lista com o preço de venda (preço final para o cliente)
preco_venda = [200, 152, 138, 225, 134, 100]

#lista com a quantidade de jogos disponíveis no estoque
quantidade_estoque = [25, 40, 20, 10, 18, 12]

#lista com os preços dos jogos de fábrica (valor que a loja paga para o fornecedor)
precos_fabrica = [160, 100, 90, 187, 89, 60]

#lista para registrar as vendas(cada item será uma tupla: (jogo, quantidade, valor total))
vendas_registradas = []

#lista para registrar as compras de estoque(tupla: (jogo, quantidade, custo total))
compras_estoque = []

#função principal (menu interativo)
def menu():
    #laço de repetição para manter o menu ativo até o usuário escolher a opção 'sair'
    while True:
        print("\n -- Bem-vindo ao 🧝🔮🧟 NerdGames 🧙🎮🧌 --  ")
        print("\n📋 Menu da Loja de Jogos")
        print("\nEscolha uma opção para prosseguir: ")
        print("1. Registrar venda 💰")
        print("2. Comprar mais jogos para o estoque 🛒")
        print("3. Resumo da loja 🏢")
        print("4. Sair ➡️")
        
        opcao = input("Digite o número da opção desejada: ")

        #estrutura de decisão para executar a função que foi escolhida
        match opcao:
            case "1":
                registrar_venda()
            case "2":
                compra_estoque()
            case "3":
                resumo_loja()
            case "4":
                print("\n🔒 Caixa fechado. Obrigado por usar o sistema da  🧝🔮🧟 NerdGames 🧙🎮🧌")
                print("\nAté mais!")
                break
            case _:
                print("\nOpção inválida. Por favor, digite um número entre 1 e 4.")

#função para registrar venda
def registrar_venda():
    print("\n🧾 Registro de Venda - Jogos disponíveis:")

    #exibe os jogos disponíveis e suas respectivas informações
    for i, jogo in enumerate(jogos):
        print(f"{i + 1}. {jogo}")
        print(f"\nPreço de venda: R${preco_venda[i]}")
        print(f"\nQuantidade em estoque: {quantidade_estoque[i]} unidade(s)\n")

    try:
        escolha = int(input("Digite o número do jogo que foi vendido: ")) - 1

        if 0 <= escolha < len(jogos):
            while True:
                try:
                    quantidade = int(input(f"Quantas unidade(s) do jogo '{jogos[escolha]}' foi/foram vendidas? "))
                    if 0 < quantidade <= quantidade_estoque[escolha]:
                        total = quantidade * preco_venda[escolha]
                        quantidade_estoque[escolha] -= quantidade  #usado para atualizar o estoque
                        vendas_registradas.append((jogos[escolha], quantidade, total))  #registra a venda
                        print(f"\n✅ Venda registrada com sucesso!")
                        print(f"\nJogo: {jogos[escolha]} | Quantidade: {quantidade} | Valor total: R${total}")
                        return
                    else:
                        print(f"\n❌ Estoque insuficiente. Nosso estoque  possui apenas {quantidade_estoque[escolha]} unidades disponíveis.")
                except ValueError:
                    print("\nEntrada inválida. Digite um número inteiro para a quantidade.")
        else:
            print("❌ Opção inválida. Escolha um número que corresponde a um jogo da lista.")
    except ValueError:
        print("Por favor, digite um número válido para escolher o jogo.")

#função compra de estoque
def compra_estoque():
    print("\n🛒 Compra de Estoque - Reponha seu inventário com os jogos de maior qualidade!")

    for i, jogo in enumerate(jogos):
        print(f"{i + 1}. {jogo}")
        print(f"\nPreço de fábrica: R${precos_fabrica[i]}")
        print(f"\nQuantidade atual em estoque: {quantidade_estoque[i]} unidade(s)\n")

    try:
        escolha = int(input("Digite o número do jogo que deseja comprar (ou 0 para cancelar a compra): "))
        
        if escolha == 0:
            print("Retornando ao menu principal.")
            return
        
        if 1 <= escolha <= len(jogos):
            while True:
                try:
                    quantidade = int(input(f"Quantas unidade(s) do jogo '{jogos[escolha - 1]}' deseja comprar? "))
                    if quantidade > 0:
                        custo = quantidade * precos_fabrica[escolha - 1]
                        quantidade_estoque[escolha - 1] += quantidade  #atualiza o estoque
                        compras_estoque.append((jogos[escolha - 1], quantidade, custo))  #registra a compra
                        print(f"\nCompra registrada com sucesso!")
                        print(f"\nJogo: {jogos[escolha - 1]} | Quantidade: {quantidade} | Custo total: R${custo}")
                        return
                    else:
                        print("A quantidade deve ser maior que zero.")
                except ValueError:
                    print("Digite um número inteiro válido para a quantidade.")
        else:
            print("❌ Opção inválida. Escolha um número da lista apresentada. ")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

#função para exibir o resumo da loja
def resumo_loja():
    print("\nResumo da Loja 🧝🔮🧟 NerdGames 🧙🎮🧌")
    
    #exibe o estoque atual de todos os jogos disponíveis
    print("\nO estoque atual é:")
    for i in range(len(jogos)):
        print(f"\n{jogos[i]} Preço: R${preco_venda[i]} | Em estoque: {quantidade_estoque[i]} unidade(s)")

    #calcula o total de vendas e compras
    total_vendas = sum(venda[2] for venda in vendas_registradas)
    total_compras = sum(compra[2] for compra in compras_estoque)

    #resumo financeiro
    print(f"\nO Total de vendas realizadas é: R${total_vendas}")
    print(f"\nO Total gasto com compras de estoque é: R${total_compras}")
    print(f"\nO Lucro bruto estimado é igual a: R${total_vendas - total_compras}")

#execução do programa
menu()  # Inicia o programa chamando o menu principal
