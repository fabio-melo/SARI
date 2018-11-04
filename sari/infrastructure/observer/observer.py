class MainObserver(object):
  def __init__(self, nome, observado):
    """ na nosso implementação, 
    todo objeto observavel vai ter um receiver por 
    composição ao invés de herança, com nome receiver """
    self.nome = nome
    if isinstance(observado,list):
      for x in observado:
        x.receiver.registrar(self)
    else:
      observado.receiver.registrar(self)  # REGISTRAR O OBSERVADOR NO OBSERVADO

  def notify(self, args):
    print(f"OBS:{self.nome}: {args}")
    
