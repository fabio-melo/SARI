#MOCK de autenticação OAUTH

# Mock Autenticação por Senha
# quando se utiliza  banco de dados, autenticamos por session ID do flask

from sari.infrastructure.auth.strategies import Strategy
from sari.infrastructure.observer.receiver import Receiver


class AuthOAUTH(Strategy):
  def __init__(self):
    self.receiver = Receiver()
    self.lista_usuarios = []


  def entrar(self, login, senha):
    """ Mock de Autenticação por OAUTH """
    try:
      hash_da_senha = f'{login}{senha}'
      if hash_da_senha == 'adminadmin':
        oauth_cookie = True
        self.receiver.notificar_todos("autenticado com sucesso usando oauth")
        return oauth_cookie
      else:
        raise Exception('TOKEN OAUTH INVALIDO')
    except Exception as e:
      self.receiver.notificar_todos(e)

  def sair(self):
    try:
      oauth_cookie = False
      return oauth_cookie
    except Exception as e:
      self.receiver.notificar_todos(e)
