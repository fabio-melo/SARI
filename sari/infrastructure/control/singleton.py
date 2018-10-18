
class Singleton(object):
  """Classe Singleton: assegura que suas subclasses tenham instância única"""
  _instance = None
  def __new__(class_, *args, **kwargs): #método magico do python
    if not isinstance(class_._instance, class_): #se não for instanciada
      class_._instance = object.__new__(class_, *args, **kwargs) #intancia
    return class_._instance #retorna a instancia da classe