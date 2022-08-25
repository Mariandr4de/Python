# import plataform
import getpass
#from datetime import datetime

# print("Usuário.......: ", getpass.getuser())
# print("Data Completa.: ", datetime.now())
# print("Dia...........: ", datetime.now().day)
# print("Mês...........: ", datetime.now().month)
# print("Ano...........: ", datetime.now().year)
# print("Hora..........: ", datetime.now().hour)
# print("Minuto........: ", datetime.now().minute)
# print("Segundo.......: ", datetime.now().second)

# usuario=input("Digite o usuário: ").upper()
# senha= input("Digite a senha: ")
# if usuario== "BITMED" and senha == "FiAp1222":
#     print("Usuário logado")else:
#     print("Login Negado")
#

print(getpass.getuser())
print(getpass.getpass("Digite sua senha..."))


usuario = input("\nDigite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")
if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado"