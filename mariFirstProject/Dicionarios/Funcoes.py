def perguntar():
    return input("O que deseja realizar?\n" +
        "<I> -Para Inserir um usuário\n"+
        "<P> -Para Pesquisar um usuário\n"+
        "<E> -Para Excluir um usuário\n"+
        "<L> -Para Listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]

    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
