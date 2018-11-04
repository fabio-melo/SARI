from sari.infrastructure.observer.receiver import Receiver

class CommandInvoker():
  def __init__(self):
    self.__fila_comandos = []
    self.receiver = Receiver()

  
  def enfileirar(self, comando):
    '''Adiciona um Comando na fila '''
    self.__fila_comandos.append(comando)

  def executar_fila(self):
    ''' Executa tudo que está na fila e zera a fila '''
    for comando in self.__fila_comandos:
      self.receiver.notificar_todos(f"Executando {comando}")
      comando.execute()

    self.__fila_comandos = []
  
  def executar_imediatamente(self, comando):
    self.receiver.notificar_todos(f"Executando {comando}")
    comando.execute()


