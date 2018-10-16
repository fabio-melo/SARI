import MySQLdb as mariadb

from core.configuration.config import DATABASE_CONFIG
from core.controller.interface import ControlAbstract
from core.controller.utils import check_value
from core.database.queries import *

def init_db():
  try:
    db = mariadb.connect(**DATABASE_CONFIG)
    cursor = db.cursor()
    cursor.execute(open('core/database/schema.sql', mode='r',encoding="utf8").read())
    print("Banco de Dados Inicializado")
  except Exception as e:
    print("Erro na Importacao"); print(e)

# DECORADORES

def reconnect(func):
  def wrapper(self, *args, **kwargs):
    self._db = mariadb.connect(**DATABASE_CONFIG)
    self._cursor = self._db.cursor()
    self._cursor.execute("USE sari;")
    
    original_func = func(self,*args, **kwargs)
    
    self._db.commit()

    return original_func
  return wrapper


# SINGLETON

class MariaDBConnector(ControlAbstract):

  def __init__(self):
    self._db, self._cursor = None, None
      
  def _reload(self):
    """Recarrega a conexão com a db e renova o db e o cursor """    
    self.db = mariadb.connect(**DATABASE_CONFIG)
    self.cursor = self._db.cursor()
    self.cursor.execute("USE sari;")

  @reconnect
  def criar_usuario(self, nome, email, senha, bio):
    try:
      self._cursor.execute(DB_PROCURAR_USUARIO_POR_EMAIL, (email,))
      user = self._cursor.fetchall()
      user = list(*zip(*zip(*user)))
      if user: raise Exception('Usuario Já Existe')

      check_value(nome, min=3, max=64)
      check_value(email, regex='[A-Za-z0-9@.]+$')
      check_value(senha, regex='[A-Za-z0-9@.\+\-\*_\-\,]+$')
      
      self._cursor.execute(DB_CRIAR_USUARIO, (nome, email, senha, bio,))
      print(f"Usuário Adicionado: {nome} {email} {senha} {bio}")
    
    except Exception as e:
      print(e)

  def excluir_usuario(self): pass
  def criar_produto(self): pass
  def excluir_produto(self): pass

  def criar_aluguel(self): pass

  def excluir_aluguel(self): pass

