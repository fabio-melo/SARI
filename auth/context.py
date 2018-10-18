#O Contexto no qual aplicamos a Strategy

class AuthContext(object):
  """ Interface de Contexto de Autenticação"""

  def __init__(self, estrategia):
    self._estrategia = estrategia

  def entrar(self, login, senha):
    self._estrategia.entrar(login, senha)
  def sair(self):
    self._estrategia.sair()
