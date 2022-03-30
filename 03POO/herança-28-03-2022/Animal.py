class Pessoa():
    nome = ""
    documento = ""
    localidade = ""
    def setnome(self, nome):
      Pessoa.nome = nome

    def getnome(self):
      return Pessoa.nome
    
    def setdocumento(self, documento):
      Pessoa.documento = documento

    def getdocumento(self):
      return Pessoa.documento

    def setlocalidade(self, localidade):
      Pessoa.localidade = localidade

    def getlocalidade(self):
      return Pessoa.localidade

    def dar_entrada(self):
        print("Entrando")

class PessoaJuridica(Pessoa):
    data_fundacao = ""

class PessoaFisica(Pessoa):
    data_nascimento = ""



pf = PessoaFisica()
pf.dar_entrada()
pf.setnome("Jeff")
pf.setdocumento("1233123")
pf.data_nascimento = "01/01/2000"
print(f"Documento da pessoa: {pf.getdocumento()} ")

pj = PessoaJuridica()
pj.dar_entrada()
pj.setnome("Jeff Company")
pj.setdocumento("1233123/0002-4")
pj.data_fundacao = "01/01/2000"
print(f"Documento da empresa: {pj.getdocumento()} ")

        