from tabuada import tabuada_especifica, tabuada_completa

print("="*8, "Tabuada de Multiplicação", "="*8)
       
nome = input("Entre com o seu nome: ")
print(f"\nSeja Bem-vindo {nome}!")

while True:

    print("\n","="*4, "Selecione uma opção:", "="*4)
    print("1 - Tabuada específica")
    print("2 - Tabuada completa de 0 à 10")
    print("3 - Sair")
    
    opcao = int(input(""))

    if opcao in [1, 2, 3]:
        if opcao == 1:  # Multiplicar
            numero = int(input("\nVocê deseja saber a tabuada de qual número: "))
            tabuada_especifica(numero)  
        elif opcao == 2:
          tabuada_completa()
        elif opcao == 3:  # Sair
            print("\nSaindo do sistema...")
            break
    else:
        print("\n==== Opção Inválida ====")

