def apresentarNotas(Layslla, Joao, Daniel):
    print(f"Layslla: {Layslla}, Joao: {Joao}, Daniel: {Daniel}")

notas = {"Layslla": 10, "Joao": 9, "Daniel": 8}
apresentarNotas(**notas)