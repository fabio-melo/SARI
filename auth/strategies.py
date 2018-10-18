# para o protótipo funcional, usamos session_ids para autenticação
from abc import ABCMeta, abstractmethod

class Strategy(object):

  __metaclass__ = ABCMeta

  @abstractmethod  
  def entrar(self, login, senha): pass
    
  @abstractmethod
  def sair(self): pass
