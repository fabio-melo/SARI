# Mock Autenticação por Senha
# quando se utiliza  banco de dados, autenticamos por session ID do flask

from sari.infrastructure.auth.strategies import Strategy

class AuthPassword(Strategy):

  def entrar(self, login, senha):
    """ Mock de Autenticação por senha """
    try:
      if login == 'admin' and senha == 'admin':
        magic_cookie = True
        return magic_cookie
      else:
        raise Exception('Usuario / Senha Invalido')
    except Exception as e:
      print(e)

  def sair(self):
    try:
      magic_cookie = False
      return magic_cookie
    except Exception as e:
      print(e)
