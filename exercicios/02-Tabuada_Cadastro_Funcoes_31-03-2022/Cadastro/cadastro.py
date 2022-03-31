from time import sleep

lista = []

def cadastro():
    nome = ""
    data_nasc = ""
    endereco = ""

    while nome == "" :
        nome = input("\nCadastre o nome: ")
    while data_nasc == "":
        data_nasc = input("Cadastre a data de nascimento: ")
    while endereco == "":
        endereco = input("Cadastre o endereço: ")
        sleep(1)
        print("\n==== Cadastrado com sucesso! ====" )
        sleep(1)

        registro = {
            'Nome': nome,
            'Data_Nascimento': data_nasc,
            'Endereco': endereco
        }

        lista.append(registro)
    return lista


def listagem():
    for item in lista:
        print(f"\n{item}")
        sleep(1)