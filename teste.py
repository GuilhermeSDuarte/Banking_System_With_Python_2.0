pessoas = []


def cadastrar(pessoas):
    identificador = input('Id? ')
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    pessoas.append((identificador, nome, idade))

while True:
    cadastrar(pessoas)
    sair = int(input("Digite 0"))
    if sair == 0:
        break

print(pessoas)