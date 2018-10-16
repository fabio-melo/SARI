# Classes de Usuário e suas Subclasses
import re

class User(object):
  """Classe-Base de Usuários"""
  

  def __init__(self, email, username, password, details={}):
    self.email = self.set_value(email, regex='[A-Za-z0-9@.]+$') # unique ID
    self.username = self.set_value(username)
    self.password = self.set_value(password, regex='[A-Za-z0-9@.\+\-\*_\-]+$')
    self.details = details # TODO: dicionario com mais informações opcionais
    
  def __repr__(self):
    return f'{self.__dict__}'

  def set_value(self, value, min = 3, max = 64, regex = '[A-Za-z0-9]+$'):
    """ Checagem simples, para inicialização de valores """
    try:
      if not isinstance(value, str): 
        raise Exception('ERRO: Valor recebe apenas strings')
      if not bool(re.match(regex, value)):
        raise Exception('ERRO: String possui caracteres inválidos')
      elif len(value) < min or len(value) > max:
        raise Exception(f'ERRO: String deve possuir no mínimo {min} e no máximo {max} caracteres')
      else: 
        return value
    except Exception as e: print(e)

class Owner(User):
  """Classe dos Donos dos Produtos"""
  def __init__(self, email, username, password, details={}):
    super().__init__(email, username, password, details=details)

  def put_to_rent(self):
    pass

  def remove_from_rent(self):
    pass

class Renter(User):
  """Usuários que Alugam os Produtos"""
  def __init__(self, email, username, password, details={}):
    super().__init__(email, username, password, details=details)

  def rent_thing(self):
    pass

  def return_thing(self):
    pass