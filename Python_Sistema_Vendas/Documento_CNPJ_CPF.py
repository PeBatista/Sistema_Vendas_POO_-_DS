from validate_docbr import CPF,CNPJ

class Documento:  
  @staticmethod
  def cria_documento(documento):
    if len(documento) == 11:
      return DocCpf(documento)
    elif len(documento) == 14:
      return DocCnpj(documento) 
    else:
      print('AVISO: Não foi passado o documento !')

class DocCpf:
  def __init__(self,documento):
    self.cpf = documento
    
  def __str__(self):
    return self.formata()

  def formata(self): # só é necessário o nosso SELF, pois usará o cpf da própria instância
      mascara = CPF() 
      return str(mascara.mask(self.cpf))

class DocCnpj:
  def __init__(self,documento):
    self.cnpj = documento

  def __str__(self):
      return self.formata()

  def formata(self): # só é necessário o nosso SELF, pois usará o cpf da própria instância
      mascara = CNPJ()
      return str(mascara.mask(self.cnpj))

