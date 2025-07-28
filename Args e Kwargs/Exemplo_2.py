def jogadas(nome, **kwargs):
    print(kwargs)
    for jogada in kwargs:
        print(kwargs[jogada])
        if kwargs[jogada] == 10:
            return f'{nome} ganhou!'
    return f'{nome} perdeu!'

# print(jogadas('Layslla', j1=10, j2=6, j3=4, j4=9, j5=2))
print(jogadas(nome='Layslla', j1=10, j2=6, j3=4, j4=9, j5=2))