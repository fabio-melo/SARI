import MySQLdb as mariadb

from sari.configuration.config import DATABASE_CONFIG 
from sari.infrastructure.control.template import ControlAbstract
from sari.infrastructure.utils.checking import check_value
from sari.database.queries import * #pylint: disable=W0614
from sari.infrastructure.control.singleton import Singleton


def init_db():
  try:
    db = mariadb.connect(**DATABASE_CONFIG)
    cursor = db.cursor()
    cursor.execute(open('core/database/schema.sql', mode='r',encoding="utf8").read())
    print("Banco de Dados Inicializado")
  except Exception as e:
    print("Erro na Importacao"); print(e)

# DECORADORES

def db_read(func):
  def wrapper(self, *args, **kwargs):
    self._db = mariadb.connect(**DATABASE_CONFIG)
    self._cursor = self._db.cursor()
    self._cursor.execute("USE sari;")
    
    original_func = func(self,*args, **kwargs)

    return original_func
  return wrapper

def db_write(func):
  def wrapper(self, *args, **kwargs):
    self._db = mariadb.connect(**DATABASE_CONFIG)
    self._cursor = self._db.cursor()
    self._cursor.execute("USE sari;")
    
    original_func = func(self,*args, **kwargs)

    self._db.commit()
    return original_func
  return wrapper



class MariaDBController(ControlAbstract, Singleton):

  def __init__(self):
    self._db, self._cursor = None, None
      
  def _reload(self):
    """Recarrega a conexão com a db e renova o db e o cursor """    
    self.db = mariadb.connect(**DATABASE_CONFIG)
    self.cursor = self._db.cursor()
    self.cursor.execute("USE sari;")


  def inicializar_sistema(self):
    self._reload()

  def notificar_admin(self):
    print("SISTEMA SARI INICIADO - MODO BANCO DE DADOS")

  def finalizar_sistema(self):
    self.db.close()

  def notificar_admin_final(self):
    print("SISTEMA SARI FINALIZADO - MODO BANCO DE DADOS")

  @db_write
  def criar_usuario(self, nome, email, senha, bio):
    try:
      self._cursor.execute(DB_PROCURAR_USUARIO_POR_EMAIL, (email,))
      user = self._cursor.fetchall()
      user = list(*zip(*zip(*user)))
      if user: raise Exception('Usuario Já Existe')

      check_value(nome, min=2, max=64)
      check_value(email, regex=r'[A-Za-z0-9@.]+$')
      check_value(senha, regex=r'[A-Za-z0-9@.\+\-\*_\-\,]+$')
      check_value(bio, max=256, regex=False)
      
      self._cursor.execute(DB_CRIAR_USUARIO, (nome, email, senha, bio,))
      print(f"DB: Usuário Adicionado: {nome} {email} {senha} {bio}")
    
    except Exception as e:
      print(e)

  @db_write
  def excluir_usuario(self,email): 
    try:
      self._cursor.execute(DB_PROCURAR_USUARIO_POR_EMAIL, (email,))
      user = self._cursor.fetchall()
      user = list(*zip(*zip(*user)))
      if user: 
        self._cursor.execute(DB_EXCLUIR_USUARIO_POR_EMAIL, (email,))
        print(f"DB: Usuário Excluido: {email}")
      else:
        raise Exception("Usuario Não Existe")
    except Exception as e: 
      print(e)
      
  @db_write
  def criar_produto(self, id_dono, nome, preco, descricao):
    try:
      check_value(id_dono, min=1, regex=r'[0-9]+$')
      check_value(nome)
      check_value(preco, regex=r'[A-Za-z0-9\@\.\$]+$')
      check_value(descricao, max=256, regex=False)

      self._cursor.execute(DB_PROCURAR_USUARIO_POR_ID, (id_dono,))
      dono_existe = self._cursor.fetchall()
      print(dono_existe)

      if dono_existe:
        self._cursor.execute(DB_CRIAR_PRODUTO, (id_dono, nome, preco, descricao,))
        print(f"DB: PRODUTO Adicionado: {nome} {preco} {descricao} {id_dono}")
      else:
        raise Exception('Usuario Não Existe')

    except Exception as e:
      print(e)

  def excluir_produto(self): 
    pass

  def criar_aluguel(self): pass

  def excluir_aluguel(self): pass

