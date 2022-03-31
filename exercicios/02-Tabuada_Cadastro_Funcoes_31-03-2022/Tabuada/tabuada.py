def tabuada_completa():
        for i in range(11):
            print("\n")
            for c in range(11):
                resultado = i * c
                print(f"{i} x {c} = {resultado}")


def tabuada_especifica(opcao):    
        for c in range(11):
            resultado = opcao * c
            print(f"{opcao} x {c} = {resultado}")

