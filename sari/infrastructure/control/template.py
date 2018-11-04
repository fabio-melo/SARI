from abc import ABCMeta, abstractmethod

class ControlAbstract(object):
  __metaclass__ = ABCMeta

  def inicializar_persistencia(self):
    """ Método Template """
    self.inicializar_sistema()
    self.notificar_admin()

  def finalizar_persistencia(self):
    self.finalizar_sistema()
    self.notificar_admin_final()

  @abstractmethod
  def inicializar_sistema(self): pass

  @abstractmethod
  def notificar_admin(self): pass
  
  @abstractmethod
  def finalizar_sistema(self): pass
  
  @abstractmethod
  def notificar_admin_final(self): pass
    
  @abstractmethod
  def criar_usuario(self): pass
  
  @abstractmethod
  def excluir_usuario(self): pass
  
  @abstractmethod
  def criar_produto(self): pass
  
  @abstractmethod
  def excluir_produto(self): pass

  @abstractmethod
  def criar_aluguel(self): pass

  @abstractmethod
  def excluir_aluguel(self): pass

  @abstractmethod
  def criar_snapshot(self): pass

  @abstractmethod
  def restaurar_estado(self): pass
