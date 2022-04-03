#Fazer a herança das seguintes classes:
#MeioTransporte
#Terrestre            / Aquatico           / Aereo
#Carro / Caminhao     Remo / Barco       Avião / Helicóptero
#Use a imaginação para criar e separar os seus atributos

class MeioTransporte():
    def __init__(self, marca, modo_transporte, combustivel):
        self.marca = marca
        self.modo_transporte = modo_transporte
        self.combustivel = combustivel
        
    def __str__(self):
        return(
            f'Marca: {self.marca}\nModelo: {self.modelo}\nModo de Transporte: {self.modo_transporte}\nCombustivel: {self.combustivel}\nQuantidade de rodas: {self.qtd_rodas}\n'
    )


# --------- Classe Terrestre ---------
class Terrestre(MeioTransporte):
    def __init__(self, marca, modo_transporte, combustivel, modelo, qtd_rodas, vias):
        super().__init__(marca, modo_transporte, combustivel)
        self.modelo = modelo
        self.qtd_rodas = qtd_rodas
        self.vias = vias
        
class Carro(Terrestre):
    def __init__(self, marca, modo_transporte, combustivel, modelo, qtd_rodas, vias, horas_alugado):
        super().__init__(marca, modo_transporte, combustivel, modelo, qtd_rodas, vias)
        self.horas_alugado = horas_alugado
        
    def __str__(self):
        return (
            f'Marca: {self.marca}\nModo de Transporte: {self.modo_transporte}\nModelo: {self.modelo}\nCombustivel: {self.combustivel}\nQuantidade de Rodas: {self.qtd_rodas}\nVias: {self.vias}\nHoras Alugado: {self.horas_alugado}\n'
    )
        
class Caminhao(Terrestre):
    def __init__(self, marca, modo_transporte, combustivel, modelo, qtd_rodas, vias, local_saida, local_chegada):
        super().__init__(marca, modo_transporte, combustivel, modelo, qtd_rodas, vias)
        self.local_saida = local_saida
        self.local_chegada = local_chegada
        
    def __str__(self):
        return (
            f'Marca: {self.marca}\nModo de Transporte: {self.modo_transporte}\nModelo: {self.modelo}\nCombustivel: {self.combustivel}\nQuantidade de Rodas: {self.qtd_rodas}\nVias: {self.vias}\nLocal de Saida: {self.local_saida}\nLocal de Chegada: {self.local_chegada}\n'
    )
        
# Instânciamentos
carro00 = Carro("Volksvagem", "Privado", "Gasolina", "Gol", "4", "Municipais", "48 horas")
print(carro00)

caminhao00 = Caminhao("Volvo", "Comercial", "Diesel", "Volvo FH 420", "6", "Nacionais", "Oiapoque", "Chui")
print(caminhao00)


# --------- Classe Aquatico ---------   
class Aquatico(MeioTransporte):
    def __init__(self, marca, modo_transporte, combustivel, localidade_circulacao, velocidade_max):
        super().__init__(marca, modo_transporte, combustivel)
        self.localidade_circulacao = localidade_circulacao
        self.velocidade_max = velocidade_max

class BarcoARemo(Aquatico):
    def __init__(self, marca, modo_transporte, combustivel, localidade_circulacao, velocidade_max, tipo_remo, qtd_remar):
        super().__init__(marca, modo_transporte, combustivel, localidade_circulacao, velocidade_max)
        self.tipo_remo = tipo_remo
        self.qtd_remar = qtd_remar
        
    def __str__(self):
        return (
            f'Marca: {self.marca}\nModo de Transporte: {self.modo_transporte}\nCombustivel: {self.combustivel}\nlocalidade de Circulacao: {self.localidade_circulacao}\nVelocidade Maxima: {self.velocidade_max}\nTipo de Remo: {self.tipo_remo}\nQuantidade de Pessoas para Remar: {self.qtd_remar}\n'
        )

class Barco(Aquatico):
    def __init__(self, marca, modo_transporte, combustivel, localidade_circulacao, velocidade_max, tipo_viagem, com_piscina):
        super().__init__(marca, modo_transporte, combustivel, localidade_circulacao, velocidade_max)
        self.tipo_viagem = tipo_viagem
        self.com_piscina = com_piscina
        
    def __str__(self):
        return (
            f'Marca: {self.marca}\nModo de Transporte: {self.modo_transporte}\nCombustivel: {self.combustivel}\nlocalidade de Circulacao: {self.localidade_circulacao}\nVelocidade Maxima: {self.velocidade_max}\nTipo de Viagem: {self.tipo_viagem}\nTem piscina: {self.com_piscina}\n')

# Instânciamentos
remo00 = BarcoARemo("Artesanal", "Privado", "Nenhum", "Rios e Lagoas", "10km/h", "Concavo", "1 pessoa")
print(remo00)

barco00 = Barco("Maersk", "Comercial", "Oleo combustivel", "Mares", "100km/h", "Internacional", "Sim")
print(barco00)


# --------- Classe Aereo --------- 
class Aereo(MeioTransporte):
    def __init__(self, marca, modo_transporte, combustivel, supersonico, jato):
        super().__init__(marca, modo_transporte, combustivel)
        self.supersonico = supersonico
        self.jato = jato

class Aviao(Aereo):
    def __init__(self, marca, modo_transporte, combustivel, supersonico, jato, empresa_aerea, hora_saida, hora_chegada):
        super().__init__(marca, modo_transporte, combustivel, supersonico, jato)
        self.empresa_area = empresa_aerea
        self.hora_saida = hora_saida
        self.hora_chegada = hora_chegada
        
    def __str__(self):
        return (
            f'Marca: {self.marca}\nModo de Transporte: {self.modo_transporte}\nCombustivel: {self.combustivel}\nSuperconico: {self.supersonico}\nA jato: {self.jato}\nEmpresa Aerea: {self.empresa_area}\nHora de Saida: {self.hora_saida}\nHora de Chegada: {self.hora_saida}\n'
        )

class Helicoptero(Aereo):
    def __init__(self, marca, modo_transporte, combustivel, supersonico, jato, emisora, qtd_pessoas):
        super().__init__(marca, modo_transporte, combustivel, supersonico, jato)
        self.emisora = emisora
        self.qtd_pessoas = qtd_pessoas

    def __str__(self):
        return (
            f'Marca: {self.marca}\nModo de Transporte: {self.modo_transporte}\nCombustivel: {self.combustivel}\nSuperconico: {self.supersonico}\nA jata: {self.jato}\nEmisora de Tv: {self.emisora}\nQuantidade de Pessoas: {self.qtd_pessoas}\n'
    )
   
# Instânciamentos
aviao00 = Aviao("Boeing 787", "Comercial", "QAV-1", "Nao", "Nao", "Varig", "12h", "16h")
print(aviao00)

helicoptero00 = Helicoptero("Sikorsky VH-92A", "Militar", "QAV-1", "Nao", "Nao", "Estatal", "8 pessoas",)
print(helicoptero00)