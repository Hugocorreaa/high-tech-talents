class grafite():   #classe
    
    #método construtor ()
    def __init__(self, cor):
        # Atributos/Propriedades
        self.cor = cor

    # Métodos
    def sair_grafite(self):
        print("Saindo grafite...")

    def verificar_cor(self):
        print(f"A cor é {self.cor}")


    #   Objeto é a instância de uma classe. "O momento que a classe existe na memória."
    #   "A classe é a definição de como deve ser um objeto."

#Objeto da classe
lapiseira = grafite("Vermelha")


lapiseira.verificar_cor()

