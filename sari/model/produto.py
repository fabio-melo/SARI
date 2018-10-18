
class Produto(object):
  """ Classe Produto """

  def __init__(self, id_produto, id_dono, nome, preco, descricao):
    """ Chaves Primária: id_produto, Estrangeira: id_dono
    """
    self.id_produto = id_produto
    self.id_dono = id_dono
    self.nome = nome
    self.preco = preco
    self.descrica = descricao

  def __repr__(self): return f"{self.__dict__}"
