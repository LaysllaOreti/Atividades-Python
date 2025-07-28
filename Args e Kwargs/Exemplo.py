# Kwargs é um dicionário que permite passar um número variável de argumentos nomeados para uma função.
# Args permite passar um número variável de argumentos posicionais para uma função.

#exemplo kwargs
"""
def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

minha_funcao(nome="Layslla", idade=19, cidade="Hortolândia")

"""

#exemplo args
"""
def minha_funcao(*args):
    for arg in args:
        print(arg)


minha_funcao(1, 2, 3)
minha_funcao("a", "b")
"""