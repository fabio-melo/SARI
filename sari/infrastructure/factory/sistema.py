from sari.infrastructure.auth import password, context, oauth
from sari.infrastructure.control import template, mariadb, localstorage
import sari.infrastructure.control.template


class SistemaSARI(object):
  # Escolher o tipo de Persistencia e o tipo de  Autenticacao
  def __init__(self, control, auth):
    self.control, self.auth = None, None
    self.iniciar_sistema(control, auth)

  #DESTRUTOR
  def __del__(self):
    self.finalizar_sistema()

  def iniciar_sistema(self, control, auth):
    try:
      #persistencia
      if control == 'db':
        self.control = mariadb.MariaDBController()
        self.control.inicializar_persistencia() # template method
      elif control == 'local':
        self.control = localstorage.LocalController()
        self.control.inicializar_persistencia() 
      else: 
        raise Exception("Método de Persistencia não Selecionado")
      #autenticação
      if auth == 'password':
        self.auth = password.AuthPassword()
      elif auth == 'oauth':
        self.auth = oauth.AuthOAUTH()
      else:
        raise Exception("Método de Autenticação não Selecionado")

    except Exception as e:
      print(e)
  
  def finalizar_sistema(self):
    self.control.finalizar_persistencia()


