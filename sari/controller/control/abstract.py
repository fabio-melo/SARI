from abc import ABCMeta, abstractmethod

class ControlAbstract(object):
  __metaclass__ = ABCMeta

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
