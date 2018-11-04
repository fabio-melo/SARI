from sari.infrastructure.command.invoker import CommandInvoker
from sari.infrastructure.command.command import * #pylint: disable=W0614
from sari.infrastructure.observer.receiver import Receiver
from sari.infrastructure.observer.observer import MainObserver


class CommandInterface(object):
  def __init__(self, core):
    self.core = core
    self.invoker = CommandInvoker()
    self.receiver = Receiver()

  def add(self, texto):
    try:
      if texto[0] == "CRIARUSUARIO":
        self.invoker.enfileirar(CriarUsuarioCommand(self.core, texto[1], texto[2], texto[3], texto[4]))
      elif texto[0] == "EXCLUIRUSUARIO":
        self.invoker.enfileirar(ExcluirUsuarioCommand(self.core, texto[1]))
      elif texto[0] == "CRIARPRODUTO":
        self.invoker.enfileirar(CriarProdutoCommand(self.core, texto[1], texto[2], texto[3], texto[4]))
      elif texto[0] == "EXCLUIRPRODUTO":
        self.invoker.enfileirar(ExcluirProdutoCommand(self.core, texto[1]))
      elif texto[0] == "CRIARALUGUEL":
        self.invoker.enfileirar(CriarAluguelCommand(self.core, texto[1], texto[2]))
      elif texto[0] == "EXCLUIRALUGUEL":
        self.invoker.enfileirar(ExcluirAluguelCommand(self.core, texto[1]))
      elif texto[0] == "ENTRAR":
        self.invoker.enfileirar(EntrarCommand(self.core, texto[1],texto[2]))
      elif texto[0] == "SAIR":
        self.invoker.enfileirar(SairCommand(self.core))
    except:
        self.receiver.notificar_todos(f"Erro Executando  {texto}")

  def rodar(self):
    self.invoker.executar_fila()