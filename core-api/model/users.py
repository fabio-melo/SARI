# Classes de Usuário e suas Subclasses
import re

class User(object):
  

  def __init__(self, email, username, password, details={}):
    self.email = self.set_value(email, regex='[A-Za-z0-9@.]+$') # unique ID
    self.username = self.set_value(username)
    self.password = self.set_value(password)
    self.details = details # dicionario com mais informações
    
  def __repr__(self):
    return f'{self.__dict__}'

  def set_value(self, value, min = 3, max = 64, regex = '[A-Za-z0-9]+$'):
    try:
      if not isinstance(value, str): 
        raise Exception('ERRO: Valor recebe apenas strings')
      if not bool(re.match(regex, value)):
        raise Exception('ERRO: String possui caracteres inválidos')
      elif len(value) < min or len(value) > max:
        raise Exception(f'ERRO: String deve possuir no mínimo {min} e no máximo {max} caracteres')
      else: 
        return value

    except Exception as e:
      print(e)

eu = User("12@com.com","265", "1234")
print(eu)


  