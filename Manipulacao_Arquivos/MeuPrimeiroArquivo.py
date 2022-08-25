'''arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo! Ai que festa!")

arquivo.close()
'''

with open("primeiro_arquivo.txt", "r") as arquivo:
    #arquivo.write("\nHakuna Matata!!")
    #conteudo = arquivo.read()
    #print(conteudo)
    for linha in arquivo.readlines():
        print(linha)
