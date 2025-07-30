def coletar_dados():
    habitantes = [
        {"nome": "Eduardo", "genero": "M", "esporte": "Natação", "idade": 25},
        {"nome": "Maria", "genero": "F", "esporte": "Futebol", "idade": 19},
        {"nome": "Daniel", "genero": "M", "esporte": "Tênis", "idade": 20},
        {"nome": "Letícia", "genero": "F", "esporte": "Natação", "idade": 28}
    ]
    return habitantes
def aviso_nenhum_homem_natacao():
    print("Aviso: Não há homens que gostam de natação.")

def calcular_idade_media_natacao(habitantes):
    homens_natacao = [h for h in habitantes if h["genero"] == "M" and h["esporte"] == "Natação"]

    if homens_natacao:
        soma_idades = sum(h["idade"] for h in homens_natacao)
        media = soma_idades / len(homens_natacao)
        print(f"Idade média dos homens que gostam de natação: {media:.2f} anos")
    else:
        aviso_nenhum_homem_natacao()


habitantes = coletar_dados()
calcular_idade_media_natacao(habitantes)
