
class Product(object):
  """ Classe Produto"""

  def __init__(self, product_id, owner_id, name, price, description):
    """ Chaves Primária: Product ID, Chave Estrangeira: Owner ID"""
    self.product_id = product_id
    self.owner_id = owner_id
    self.name = name
    self.price = price
    self.description = description

  def __repr__(self):
    return f"{self.__dict__}"
