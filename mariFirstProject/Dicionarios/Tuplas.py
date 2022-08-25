"""
Tuplas são delimitadas por (), são como listas, podem ter vários dados dentro, porem seu diferencial é que são imutáveis,
ou seja, não podemos alterar uma tupla; nem todos os métodos podem ser usados em tuplas, porem quando queremos um resultado
ele pode retornar em formas de tupla

Tuplas não aceitam alterações sobre os dados já inserido nela, mesmo não sendo muito utilizadas em programas devemos saber
como usar e manipular, por exemplo, tuplas podem ser chaves de um dicionário, pois as chaves não vão mudar; vou explicar
exemplo, se temos um dado na chave que são dois dados isso daria um erro, porem se for uma tupla contendo esses dados ai ok.

"""

usuarios = {}
emails = ["teste@teste.com", "teste2@teste.com"]

tupla = list(enumerate(emails))
# print(tupla)

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome"), input("Digite o nível")]

for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ", chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])

"""
Até o momento a maior preocupação foi te mostrar as estruturas de dados básicas, como manipular e utilizar esses recursos,
com esse básico você desenvolve algo, mas agora vem o divisor de águas, aqui vai ser o momento de se tornar algo a mais,
então estude bastante, treine o que foi feito até agora, se precisar veja a documentação do python.
"""