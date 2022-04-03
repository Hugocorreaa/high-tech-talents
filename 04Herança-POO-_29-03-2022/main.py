
##### ----- Classe Pessoa -----
class Pessoa():
   def __init__(self, nome, documento, localidade):
      self.nome = nome
      self.documento = documento
      self.localidade = localidade

   # -- Metodos -- 
   def dar_entrada(self):
      print("Entrando")


##### ----- Classe PessoaJuridica -----
class PessoaJuridica(Pessoa):
   def __init__(self, nome, documento, localidade, data_fundacao):
       super().__init__(nome, documento, localidade)
       self.data_fundacao = data_fundacao

   # -- Metodos --
   def fundar(self):
      print("Fundando")


##### ----- Classe PessoaFisica -----
class PessoaFisica(Pessoa):
   def __init__(self, nome, documento, localidade, data_nascimento):
       super().__init__(nome, documento, localidade)
       self.data_nascimento = data_nascimento

   # -- Metodos --
   def nascer(self):
      print("Nascendo")

   def __metodoPrivado(self): ## Metodo privado. ELE SÓ PODE SER USADO DENTRO DA CLASSE. O ESCOPO É PRIVADO.
      print("metodo")





# --------------- Instanciamentos --------------------

# Instaciamento de objeto pj
pj = PessoaJuridica("Jeff Company", "123321/111", "RJ", "01/01/2000")
pj.dar_entrada()
pj.fundar()

print(pj.documento)

# Instaciamento de objeto pf
pf = PessoaFisica("Jeff", "123321", "RJ", "01/01/2000")
pf.dar_entrada()
pf.nascer()
# pf.__metodoPrivado() ## Teste de escopo privado

print(pf.documento)






