import requests

# id_personagem = input("Digite o ID do personagem: ")

#peço para o usuário digitar o ID do personagem
response = requests.get("https://potterhead-api.vercel.app/api/characters")

#pego e coloco o JSON para manipular
personagem = response.json()

#índice 0 para pegar a informação do nome
nome_personagem = personagem[7]["name"]

print(nome_personagem)
