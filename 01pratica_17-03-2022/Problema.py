# 1-) Entender o problema
# 2-) Planejar a solução

# - Cria um menu no console com 3 opções:
#       - Sair
#       - Cadastrar
#       - Listar
# 3-) Dividir/Planejar Tarefas
#       - Preparar um arquivo Python (Este aqui mesmo)
#       - Criar Loop para o menu principal
#       - Criar "Tela" Cadastrar
#           - Perguntar campo Nome
#           - Perguntar campo Data Nascimento
#           - Perguntar campo Endereço
#       - Criar "Tela" Listar
#           - Prepara Prints Dicionario
#       - Criar funcionalidade Sair
# 4-) Estimar tempo de desenvolvimento (Até o final da aula)

from time import sleep


usuario = input("Entre com o seu nome: ")
print(f"\nSeja Bem-vindo {usuario}!")
sleep(2)

lista = []

while True:
    
    print("\nSelecione uma opção: ")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = int(input(""))

    if opcao in [1,2,3]:
        if opcao == 1:      #Cadastrar

            nome = ""
            data_nasc = ""
            endereco = ""

            while nome == "" :
                nome = input("\nColoque o nome: ")
            while data_nasc == "":
                data_nasc = input("Coloque a data de nascimento: ")
            while endereco == "":
                endereco = input("Coloque o endereço: ")
                sleep(1)
                print("\n==== Cadastrado com sucesso! ====" )
                sleep(2)

                registro = {
                    'Nome': nome,
                    'Data_Nascimento': data_nasc,
                    'Endereco': endereco
                }

                lista.append(registro)

        elif opcao == 2:    #Listar
            for item in lista:
                print(f"\n{item}")
                sleep(2)
        elif opcao == 3:    #Sair
            print("\nSaindo do sistema...")
            break
    else:
        print("\n==== Opção Inválida ====")



