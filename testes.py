def Imprimir_Nome(nome):
    if nome is None:
        nome = "Não tenho nome"
    elif nome == "":
        nome = "Ainda não tenho nome"
    return nome

print(Imprimir_Nome(""))