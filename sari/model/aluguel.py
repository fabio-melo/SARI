
class Aluguel(object):
  """ Entidade-Relacionamento Aluguel """
  def __init__(self, id_transacao, id_produto, id_alugador, data_aluguel):
    """ Chave Primaria/Estrangeira = ID_Produto X ID_Alugador"""
    self.id_transacao = id_transacao
    self.id_produto = id_produto
    self.id_alugador = id_alugador
    self.data_aluguel = data_aluguel

  def __repr__(self): return f'{self.__dict__}'