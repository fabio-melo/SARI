#MOCK de Relatorios
from abc import ABCMeta, abstractmethod


class RelatorioAbstract(metaclass=ABCMeta):
  @abstractmethod
  def gerar_relatorio_de_usuario(self): pass

  @abstractmethod
  def gerar_relatorio_de_sistema(self): pass
