# Mock Autenticação por Senha
# quando se utiliza  banco de dados, autenticamos por session ID do flask

from sari.infrastructure.auth.strategies import Strategy
from sari.infrastructure.observer.receiver import Receiver


class AuthPassword(Strategy):
  def __init__(self):
    self.receiver = Receiver()

  def entrar(self, login, senha):
    """ Mock de Autenticação por senha """
    try:
      if login == 'admin' and senha == 'admin':
        magic_cookie = True
        self.receiver.notificar_todos("autenticado com sucesso usando senha")
        return magic_cookie
      else:
        raise Exception('Usuario / Senha Invalido')
    except Exception as e:
      self.receiver.notificar_todos(e)

  def sair(self):
    try:
      magic_cookie = False
      self.receiver.notificar_todos("deslogado com sucesso")
      return magic_cookie
    except Exception as e:
      self.receiver.notificar_todos(e)
