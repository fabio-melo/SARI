from abc import ABCMeta, abstractmethod

class BaseCommand(object):
  
  __metaclass__ = ABCMeta
  
  def __init__(self, core, args): 
    self.args = args
    self.core = core

  def __repr__(self):
    return f"{type(self).__name__}: {self.args}"

  @abstractmethod
  def execute(self): pass

class CriarUsuarioCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    #  nome, email, senha, bio
    self.core.control.criar_usuario(self.args[0], self.args[1], self.args[2], self.args[3])


class ExcluirUsuarioCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    #  email
    self.core.control.excluir_usuario(self.args[0])

class CriarProdutoCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    #  id_dono, nome, preco, descricao
    self.core.control.criar_produto(self.args[0], self.args[1], self.args[2], self.args[3])

class ExcluirProdutoCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    #  id_produto
    self.core.control.excluir_produto(self.args[0])

class CriarAluguelCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    #  id_produto, id_alugador, data_aluguel
    self.core.control.criar_aluguel(self.args[0], self.args[1],self.args[2])

class ExcluirAluguelCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    #  id_aluguel
    self.core.control.excluir_aluguel(self.args[0])


# AUTENTICACAO
class EntrarCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    self.core.auth.entrar(self.args[0], self.args[1])

class SairCommand(BaseCommand):
  def __init__(self, core, *args):
    super().__init__(core, args)
  def execute(self):
    self.core.auth.sair()
