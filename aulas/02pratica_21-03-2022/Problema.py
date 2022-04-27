# Fazer um programa que imprima a tabuada do 0 até o 10 no console

# 1-) Entender o problema
#       Gerar as tabuadas de 0 até 10 no console
# 2-) Planejar a solução
#       Criar um sistema que tenho os seguintes menus:
#           -Login/Boas Vinda
#           -Menu
#               -Multiplicar
#               -Sair
# 3-) Dividir/Planejar Tarefas
#       - Criação tela login
#       - Criação Menu principal
#       - Criação funcionalidade sair
#       - Criação tela multiplicar
#           -Preparar loops
# 4-) Estimar tempo de desenvolvimento (Até o final da aula)


from time import sleep
print("="*8, "Tabuada de Multiplicação", "="*8)


usuario = input("Entre com o seu nome: ")
print(f"\nSeja Bem-vindo {usuario}!")
sleep(2)

lista = []

while True: # Menu

    print("\nSelecione uma opção: ")
    print("1 - Multiplicar")
    print("2 - Sair")

    opcao = int(input(""))

    if opcao in [1, 2]:
        if opcao == 1:  # Multiplicar
            for i in range(11):
                print("\n")
                for c in range(11):
                    resultado = i * c
                    print(f"{i} x {c} = {resultado}")
        elif opcao == 2:  # Sair
            print("\nSaindo do sistema...")
            break
    else:
        print("\n==== Opção Inválida ====")
