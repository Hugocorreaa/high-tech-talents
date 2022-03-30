# Cadastro

from time import sleep

def Cadastro(nome, data_nasc, endereco):
        lista = []
        
        sleep(1)
        print("\n==== Cadastro realizado! ====" )
        sleep(1)

        registro = {
            'Nome': nome,
            'Data_Nascimento': data_nasc,
            'Endereco': endereco
        }

        lista.append(registro)
    
        for item in lista:
            print(f"\n{item}")
            sleep(2)


Cadastro("Hugo", "15/04/1996", "Av.Petra Kelly")