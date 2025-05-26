import sys #vai interromper o código por completo

#Criar as principais listas da Loja
jogos = ["GTA V", "The Last Of Us - Part II", "Minecraft", "God Of War Ragnarök", "Hogwarts Legacy", "It Takes Two"]
preco_venda = [200, 152, 138, 225, 134, 100]
quantidade_estoque = [25, 40, 20, 10, 18, 12]
precos_fabrica = [160, 100, 90, 187, 89, 60]
vendas_registradas = []  # Cada item será uma tupla - jogo, quantidade e valor total
compras_estoque = []     # Cada item será uma tupla - jogo, qauntidade e valor total


def menu():
    while True:
        print("\n -- Bem-vindo ao 🧝🔮🧟 NerdGames 🧙🎮🧌 -- ")
        print("\n--- MENU DA LOJA DE JOGOS ---")
        print("\n Escolha uma das opções abaixo e aproveite a experiência: ")
        print("1. Registrar venda 📋")
        print("2. Compra de estoque 🛒")
        print("3. Resumo da loja 🏢")
        print("4. Sair 🏃‍➡️")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                registrar_venda()
            case "2":
                compra_estoque()
            case "3":
                resumo_loja()
            case "4":
                print("Caixa fechado, obrigada por acessar nossa loja. Até mais!")
                break
            case _:
                print("Opção inválida.")

def registrar_venda():
    print("\n--- REGISTRAR VENDA 🗃️ ---")
    for i, jogo in enumerate(jogos):
        print(f"{i + 1}. {jogo}\n Preço de venda: R${preco_venda[i]}\n"
              f" Preço de fábrica: R$ {precos_fabrica[i]}\n Quantidade em estoque: {quantidade_estoque[i]} unidade(s)")

    try:
        escolha = int(input("Escolha o número do jogo vendido: ")) - 1
        if 0 <= escolha < len(jogos):
            while True:
                try:
                    quantidade = int(input("Insira quantas unidades desse jogo foram vendidas: "))
                    if quantidade <= quantidade_estoque[escolha]:
                        total = quantidade * preco_venda[escolha]
                        quantidade_estoque[escolha] -= quantidade
                        vendas_registradas.append((jogos[escolha], quantidade, total))
                        print(f"Venda registrada com sucesso 🎉: {quantidade} unidade(s) do jogo: {jogos[escolha]}\nO valor total da venda foi: R${total}")
                        print("Obrigada por registrar a sua venda em nossos sistema. Até mais!")
                        sys.exit()
                    else:
                        print(f"Erro ❌: Quantidade insuficiente! O estoque possui apenas {quantidade_estoque[escolha]} unidade(s).")
                except ValueError:
                    print("Erro ❌: Entrada inválida. Digite um número inteiro para a quantidade.")
        else:
            print("Erro ❌: Escolha inválida!")
    except ValueError:
        print("Erro ❌: Entrada inválida. Digite o número do jogo corretamente.")

def compra_estoque():
    #essa função serve para comprar um jogo
    print("\n--- COMPRA DE ESTOQUE 🛒 ---")
    while True:
        for i, jogo in enumerate(jogos):
            print(f"{i + 1}. {jogo}\n Preço de venda: R${preco_venda[i]}")
            print(f"Quantidade disponível no Estoque: {quantidade_estoque[i]} unidade(s)")

        try:
            escolha = int(input("\nDigite o número do jogo que deseja comprar (ou a opção 0 para sair do menu de compras): "))
            if escolha == 0:
                print("Saindo do menu de compras. obrigado por visitar a 🧝🔮🧟 NerdGames 🧙🎮🧌.")
                break

            if 1 <= escolha < len(jogos):
                while True:
                    try:
                        quantidade = int(input("Quantidade a comprar: "))
                        if quantidade > 0:
                            custo = quantidade * precos_fabrica[escolha]
                            quantidade_estoque[escolha] += quantidade
                            compras_estoque.append((jogos[escolha], quantidade, custo))
                            print(f"Compra registrada: {quantidade} unidade(s) do jogo {jogos[escolha]}\nValor total: R${custo}")
                            print("Agradecemos por comprar na 🧝🔮🧟 NerdGames 🧙🎮🧌. Volte sempre!")
                            sys.exit()
                        else:
                            print("Por favor, digite uma quantidade maior que zero.")
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número inteiro.")
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def resumo_loja():
    print("\n--- RESUMO DA LOJA 🏢 ---")
    print("Estoque atual:")
    for i in range(len(jogos)):
        print(f"{jogos[i]} - R${preco_venda[i]} | Quantidade: {quantidade_estoque[i]}")

    total_vendas = sum(venda[2] for venda in vendas_registradas)
    total_compras = sum(compra[2] for compra in compras_estoque)

    print(f"\nTotal em vendas: R${total_vendas}")
    print(f"Total gasto em estoque: R${total_compras}")
    print(f"Lucro bruto estimado: R${total_vendas - total_compras}")

# Executar o menu principal
menu()