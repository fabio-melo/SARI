class MainObserver(object):
  def __init__(self, observado):
    observado.register(self)  # REGISTRAR O OBSERVADOR NO OBSERVADO

  def notify(self, observado, *args):
    print(f"{type(self).__name__}: Recebeu Comando {args} de {observado}")
    