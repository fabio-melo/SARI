class Receiver(object):
  def __init__(self):
    self.__observadores = []

  def registrar(self, observador):
    """Registrando Observador"""
    self.__observadores.append(observador)

  def desregistrar(self, observador):
    self.__observadores.pop(observador)

  def notificar_todos(self, notification):
    if self.__observadores:
      for obs in self.__observadores:
        obs.notify(notification)
