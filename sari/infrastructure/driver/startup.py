from sari.infrastructure.auth import password, context, oauth
from sari.infrastructure.control import template, mariadb, localstorage
import sari.infrastructure.control.template


class SistemaSARI(object):
  # Escolher o tipo de Persistencia e o tipo de 
  def __init__(self):
    self.control = None
    self.auth = None

  def iniciar_sistema(self, control, auth):
    try:
      #persistencia
      if control == 'db':
        self.control = mariadb.MariaDBController()
        self.control.inicializar_sistema()
      elif control == 'local':
        self.control = localstorage.LocalController()
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


