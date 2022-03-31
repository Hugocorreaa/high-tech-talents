from cadastro import cadastro, listagem

print("="*8, "Cadastro de Usuário", "="*8)

while True:
    
    print("\nSelecione uma opção: ")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = int(input(""))

    if opcao in [1,2,3]:
        if opcao == 1:      #Cadastrar
            cadastro()
        elif opcao == 2:    #Listar
            listagem()
        elif opcao == 3:    #Sair
            print("\nSaindo do sistema...")
            break
        else:
            print("\n==== Opção Inválida ====")
        