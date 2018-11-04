import pickle

class SnapshotMemento(object):
  def __init__(self, maximo=10):
    self.estados = []
    self.maximo = maximo

  def criar_snapshot(self, estado):
    if len(self.estados) < self.maximo:
      self.estados.append(pickle.dump(estado))
    else:
      self.estados.pop(0)
      self.estados.append(pickle.dump(self.estados))

  def restaurar_ultimo_snapshot(self):
    try:
      return pickle.loads(self.estados.pop())
    except:
      print("Não há estados para restaurar")
  
