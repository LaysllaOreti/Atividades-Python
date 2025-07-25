def mostrar_menu():
    print("=== Calculadora DS18 ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calcular():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '5':
            print("Saindo da calculadora. Até logo!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.\n")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.\n")
            continue

        if escolha == '1':
            resultado = num1 + num2
            operacao = '+'
        elif escolha == '2':
            resultado = num1 - num2
            operacao = '-'
        elif escolha == '3':
            resultado = num1 * num2
            operacao = '*'
        elif escolha == '4':
            if num2 == 0:
                print("Erro: divisão por zero.\n")
                continue
            resultado = num1 / num2
            operacao = '/'

        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}\n")

# Para executar a calculadora:
calcular()
