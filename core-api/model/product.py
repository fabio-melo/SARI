
class Product:
  """ Classe Product: 
    @params:
  """

  def __init__(self, id_, name, features):
    self.name = name
    self.id = id_
    self.details = {}


  def __repr__(self):
    return f"{self.__dict__}"

  def add_detail(self, key, value): 
    self.details[key] = value

  def del_detail(self, key):
    if self.details.get(key): self.details.pop(key)

