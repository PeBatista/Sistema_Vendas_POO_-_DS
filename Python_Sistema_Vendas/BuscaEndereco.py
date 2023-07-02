import requests
class BuscaEndereco:
  def __init__(self,cep):
    cep = str(cep)
    if self.cep_e_valido(cep):
      self.cep = cep
      print('CEP cadastrado')
    else:
      raise ValueError("CEP inválido")

  def __str__(self):
    return self.formata_cep()

  def formata_cep(self):
    return f"{self.cep[:5]}-{self.cep[5:]}"

  def acessa_via_cep(self):
    r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
    dados = r.json()
    return dados

  def cep_e_valido(self,cep):
    if len(cep) == 8:
      return True
    else:
      return False