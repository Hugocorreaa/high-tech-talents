# Fazer um programa que imprima a tabuada do 0 até o 10 no console


def Tabuada(opcao):    
        for c in range(11):
            resultado = opcao * c
            print(f"{opcao} x {c} = {resultado}")


Tabuada()
