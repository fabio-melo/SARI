# Classes de Usuário

class Usuario(object):
  """Entidade Usuários"""
  def __init__(self, id_usuario, email, nome, senha, bio):
    self.id_usuario = id_usuario
    self.email = email # unique ID
    self.nome = nome
    self.senha= senha
    self.bio = bio

  def __repr__(self):
    return f'{self.__dict__}'