from sari.controller.control.abstract import ControlAbstract
from sari.model.usuario import Usuario
from sari.model.aluguel import Aluguel
from sari.model.produto import Produto
import pickle

class LocalController(ControlAbstract):

  def __init__(self):
    self.usuarios = {}
    self.produtos = {}
    self.alugueis = {}
    self.prox_usuario = 0
    self.prox_produto = 0
    self.prox_aluguel = 0

  def carregar_arquivo(self, a_usuarios, a_produtos, a_alugueis):
    with open(a_usuarios,'rb') as a_usuarios:
      self.usuarios = pickle.load(a_usuarios)
    with open(a_produtos,'rb') as a_produtos:
      self.produtos = pickle.load(a_produtos)
    with open(a_alugueis,'rb') as a_alugueis:
      self.alugueis = pickle.load(a_alugueis)
    self.prox_usuario = len(self.usuarios)
    self.prox_produto = len(self.produtos)
    self.prox_aluguel = len(self.alugueis)

  def salvar_arquivo(self, a_usuarios, a_produtos, a_alugueis):
    with open(a_usuarios,'wb') as a_usuarios:
      pickle.dump(self.usuarios, a_usuarios)
    with open(a_produtos,'wb') as a_produtos:
      pickle.dump(self.produtos, a_produtos)
    with open(a_alugueis,'wb') as a_alugueis:
      pickle.dump(self.alugueis, a_alugueis)

  def criar_usuario(self, nome, email, senha, bio):
    id_usuario = self.prox_usuario
    self.prox_usuario += 1
    
    usr = Usuario(id_usuario, email, nome, senha, bio)
    self.usuarios[id_usuario] = usr
    
  
  def excluir_usuario(self, email):
    try:
      for key, value in self.usuarios:
        if value.email == email:
          self.usuarios.pop(key)
    except:
      print(f'Usuario {email} não encontrado')

  def criar_produto(self, id_dono, nome, preco, descricao):
    raise NotImplementedError
  
  def excluir_produto(self): 
    raise NotImplementedError

  def criar_aluguel(self): 
    raise NotImplementedError

  def excluir_aluguel(self): 
    raise NotImplementedError